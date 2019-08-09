
import multiprocessing
import os
import sys
import ctypes
import builtins

import util.credread
import util.toolBox
import util.fakestd

from wx import App, GetTranslation
from configparser import ConfigParser
from ui.MainFrame import MainFrame
from util.update import AsyncUpdateCheck


if __name__ == '__main__':
    # Freeze support
    if getattr(sys, 'frozen', False):
        sys.stdout = util.fakestd.Fakestd()
        sys.stderr = util.fakestd.Fakestd()
    multiprocessing.freeze_support()

    #internationalization
    builtins.__dict__['_'] = GetTranslation
    
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass

    cwd = os.getcwd()
    appdataAppName = 'VNCSSH'
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

    # Check version
    appVersion = "0.3.3"
    updateCheck = AsyncUpdateCheck(appVersion, False)
    updateCheck.start()
    
    # Init app
    os.chdir(cwd)
    
    app = App()
    a = MainFrame(None)
    # init fill
    a.textBoxUsr.Value = util.credread.InitUser()
    a.choiceKey.AppendItems(list(util.credread.FindKey().keys()))
    a.comboBoxIP.AppendItems(util.credread.InitIPList())
    #
    a.CurrentVersion(appVersion)
    a.Show()
    app.MainLoop()
