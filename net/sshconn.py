import paramiko
from multiprocessing import Process
import subprocess
from net.forward import forward_tunnel

class SSHConn:
    def __init__(self, ip, username, password, keyfile):
        self.IP = ip
        self.Username = username
        self.Password = password
        self.Key = keyfile
        self.sshc = paramiko.SSHClient()
        self.sshc.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.t = {}
        self.ssht = paramiko.SSHClient()
        self.ssht.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    def OpenVNCTunnel(self, localPort, remotePort):
        t0 = Process(target = self.TunnelThread, args=(localPort,remotePort))
        t0.daemon = True
        t0.start()
        self.t[remotePort] = t0
        return True

    def StopTunnel(self,remotePort):
        self.t[remotePort].terminate()
        self.ssht.close()

    def TunnelThread(self, localPort, remotePort):
        if self.Password == None:
            self.ssht.connect(self.IP, 22, username=self.Username, key_filename=self.Key)
        else:
            self.ssht.connect(self.IP, 22, username=self.Username, password=self.Password)
        transport = self.ssht.get_transport()
        forward_tunnel(localPort, "localhost", remotePort, transport)


    def OpenTerminal(self):
        if self.Password == None:
            subprocess.call("start powershell ssh {0}@{1} -i {2} -t" \
            .format(self.Username, self.IP, self.Key), shell=True)
        else:
            subprocess.call("start powershell ssh {0}@{1} -t" \
            .format(self.Username, self.IP), shell=True)
    
    def ListRemoteFile(self, remotePath):
        stdin, stdout, stderr = self.sshc.exec_command('ls -FA {0}'.format(remotePath))
        outread = stdout.read().decode("utf-8")
        directories = outread.split("\n")
        folders = []
        files = []
        for di in directories:
            if di == "":
                continue
            elif di[-1] == "/":
                folders.append(di[:-1])
            elif di[-1] == "*" or di[-1] == "@":
                files.append(di[:-1])
            elif di[-1] != "|" and di[-1] != "=":
                files.append(di)
        return (folders, files)
    
    def SendFile(self, source, filename, sink, callback):
        ft = self.sshc.open_sftp()
        ft.put(source, sink + filename, callback)
        return True

    def GetFile(self, source, filename, sink, callback):
        ft = self.sshc.open_sftp()
        ft.get(source, sink + filename, callback)
        return True
    

    def CloseConn(self):
        self.sshc.close()
    def StartConn(self):
        if self.Password == None:
            self.sshc.connect(self.IP, 22, username=self.Username, key_filename=self.Key)
        else:
            self.sshc.connect(self.IP, 22, username=self.Username, password=self.Password)
