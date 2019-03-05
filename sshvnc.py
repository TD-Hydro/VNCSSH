import wx
from ui.MainFrame import MainFrame
import multiprocessing
import os
from configparser import ConfigParser

#import net.keyread
if __name__ == '__main__':
    multiprocessing.freeze_support()

    cwd = os.getcwd()
    appdataAppName = 'SSHVNCP'
    # Write appdata
    appdataPath = os.environ["LOCALAPPDATA"]
    os.chdir(appdataPath)
    if not os.path.isdir(appdataAppName):
        os.mkdir(appdataAppName)
    if not os.path.exists(appdataAppName + '\\credential.ini'):
        config = ConfigParser()
        config["key"] = {"keyfile": "{}"}
        config["user"] = {"username": ""}
        with open(appdataAppName + '\\credential.ini', 'w') as configfile:
            config.write(configfile)
    if not os.path.exists(appdataAppName + '\\settings.ini'):
        open(appdataAppName + '\\settings.ini', 'a').close()

    # Init app
    os.chdir(cwd)
    app = wx.App()
    a = MainFrame(None)
    # init fill
    #a.textBoxUsr.Value = net.keyread.InitUser()
    # a.choiceKey.AppendItems(net.keyread.FindKey())
    #
    a.Show()
    app.MainLoop()
