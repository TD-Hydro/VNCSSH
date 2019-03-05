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

    def OpenVNCWindow(self, localPort, remotePort):
        t0 = Process(target = self.TunnelThread, args=(localPort,remotePort))
        t0.daemon = True
        t0.start()
        self.t[remotePort] = t0
        subprocess.Popen(["bin/vncviewer.exe", "localhost:{0}".format(localPort)])
        return True

    def StopTunnel(self,remotePort):
        self.t[remotePort].terminate()
        self.ssht.close()

    def TunnelThread(self, localPort, remotePort):
        self.ssht.connect(self.IP, 22, username=self.Username, key_filename=self.Key)
        transport = self.ssht.get_transport()
        forward_tunnel(localPort, "localhost", remotePort, transport)


    def OpenTerminal(self):
        subprocess.call("start powershell ssh {0}@{1} -i {2} -t" \
        .format(self.Username, self.IP, self.Key), shell=True)
    
    def ListRemoteFile(self, remotePath):
        stdin, stdout, stderr = self.sshc.exec_command('ls -FA {0}'.format(remotePath))
        outread = stdout.read().decode("utf-8")
        directories = outread.split("\n")
        folders = []
        files = []
        for dir in directories:
            if dir == "":
                continue
            elif dir[-1] == "/":
                folders.append(dir[:-1])
            elif dir[-1] == "*" or dir[-1] == "@":
                files.append(dir[:-1])
            elif dir[-1] != "|" and dir[-1] != "=":
                files.append(dir)
        return (folders, files)
    
    def SendFile(self, source, filename, sink, callback):
        pass
        # ft = self.sshc.open_sftp()
        # ft.put(source, "/home/{0}/{1}".format(self.Username, filename), callback)
        # stdin, stdout, stderr = self.sshc.exec_command('scp /home/{0}/{1} root@{2}:{3}{4} &echo success'.format(self.Username, filename, ipad, sink, filename))
        # outread = stdout.read().decode("utf-8")
        # err = stderr.read().decode("utf-8")
        # print(err)
        # if outread.strip() == "success":
        #     self.sshc.exec_command('rm /home/{0}/{1}'.format(self.Username, filename))
        #     return True
    

    def GetFile(self, source, filename, sink, callback):
        pass
        # stdin, stdout, stderr = self.sshc.exec_command('scp root@{0}:{1} /home/{2}/{3} &echo success'.format(ipad, source, self.Username, filename))
        # outread = stdout.read().decode("utf-8")
        # err = stderr.read().decode("utf-8")
        # print(err)
        # if outread.strip() == "success":
        #     ft = self.sshc.open_sftp()
        #     ft.get("/home/{0}/{1}".format(self.Username, filename), sink + filename, callback)
        #     self.sshc.exec_command('rm /home/{0}/{1}'.format(self.Username, filename))
    

    def CloseConn(self):
        self.sshc.close()
    def StartConn(self):
        if self.Password == None:
            self.sshc.connect(self.IP, 22, username=self.Username, key_filename=self.Key)
        else:
            self.sshc.connect(self.IP, 22, username=self.Username, password=self.Password)