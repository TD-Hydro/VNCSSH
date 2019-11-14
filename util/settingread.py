import shutil
from configparser import ConfigParser
import os
import json

def GetAppData():
    return os.environ["LOCALAPPDATA"] + "\\VNCSSH\\"

def GetSettings():
    config = ConfigParser()
    config.read(GetAppData()+"settings.ini")
    return config

def GetVNCSetting(config):
    localmark = config.get('vnc','local')
    local = True if localmark=='1' else False
    realVNCPath = config.get('vnc','realpath')
    port = config.get('vnc','remoteport')
    return local, realVNCPath, port

def GetLangSetting(config):
    language = config.get('language','language')
    return language

def GetTerminalSetting(config):
    terminalMark = config.get('terminal', 'local')
    local = True if terminalMark=='1' else False
    return local

def SetVNCSetting(config,localMark,realPath,port):
    config['vnc']['local'] = '1' if localMark else '0'
    config['vnc']['realpath'] = realPath
    config['vnc']['remoteport'] = port
    
def SetLangSetting(config, langNum):
    config['language']['language'] = str(langNum)

def SetTerminalSetting(config, localMark):
    config['terminal']['local'] = '1' if localMark else '0'

def WriteSetting(config):
    with open(GetAppData()+"settings.ini", 'w') as configfile:
        config.write(configfile)