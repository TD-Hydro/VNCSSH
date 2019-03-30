import wx
import multiprocessing
import os
import sys
import ctypes

import util.credread
import util.toolBox
import util.fakestd

from configparser import ConfigParser
from ui.MainFrame import MainFrame


#import net.keyread
if __name__ == '__main__':
    if getattr(sys, 'frozen', False):
        sys.stdout = util.fakestd.Fakestd()
        sys.stderr = util.fakestd.Fakestd()
    multiprocessing.freeze_support()
    
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass

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
        config["ip"] = {"ip": "[]"}
        with open(appdataAppName + '\\credential.ini', 'w') as configfile:
            config.write(configfile)
    if not os.path.exists(appdataAppName + '\\settings.ini'):
        open(appdataAppName + '\\settings.ini', 'a').close()
    util.toolBox.CheckAndAddSetting('vnc',[('local','1'), ('realpath',''), ('remoteport','5901')])

    # Init app
    os.chdir(cwd)
    app = wx.App()
    a = MainFrame(None)
    # init fill
    a.textBoxUsr.Value = util.credread.InitUser()
    a.choiceKey.AppendItems(list(util.credread.FindKey().keys()))
    a.comboBoxIP.AppendItems(util.credread.InitIPList())
    #
    a.CurrentVersion("0.3.2")
    a.Show()
    app.MainLoop()
