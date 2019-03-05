import wx
import os
import webbrowser
from configparser import ConfigParser

def MBox(content, title, label):
    '''
    Messagebox wrapper
    @param label [0:NONE,1:EXCLAMATION,2:ERROR,3:HAND,4:QUESTION,5:INFORMATION,6:AUTH NEEDED] 
    '''
    iconLabel = {0:wx.ICON_NONE,1:wx.ICON_EXCLAMATION,2:wx.ICON_ERROR,3:wx.ICON_HAND,4:wx.ICON_QUESTION,5: wx.ICON_INFORMATION,6:wx.ICON_AUTH_NEEDED}
    dial = wx.MessageDialog(None, content, title, wx.OK | iconLabel[label])
    dial.ShowModal()

def ValidIP(address):
    try:
        host_bytes = address.split('.')
        valid = [int(b) for b in host_bytes]
        valid = [b for b in valid if b >= 0 and b<=255]
        return len(host_bytes) == 4 and len(valid) == 4
    except:
        return False

def OpenALink(link):
    if os.name == 'nt':
        os.system("start \"\" " + link)
    else:
        webbrowser.open(link)

def CheckAndAddSetting(setName, itemList):
    '''
    Add setting if not
    @param setName of the set :str
    @param itemList item list [(itemName:str, defaultValue:str)]
    '''
    appdataAppName = 'SSHVNCP'

    config = ConfigParser()
    config.read(appdataAppName + "\\settings.ini")
    changed = False
    if setName not in config.sections():
        config[setName] = {}
        changed = True        
    for i in itemList:
        if i[0] not in config[setName]:
            config[setName][i[0]] = i[1]
            changed = True
    if changed:
        with open(appdataAppName + "\\settings.ini", 'w') as configfile:
            config.write(configfile)