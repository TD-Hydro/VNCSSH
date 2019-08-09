import shutil
from configparser import ConfigParser
import os
import json

def GetAppData():
    return os.environ["LOCALAPPDATA"] + "\\VNCSSH\\"

def GetVNCSetting():
    config = ConfigParser()
    config.read(GetAppData()+"settings.ini")
    localmark = config.get('vnc','local')
    local = True if localmark=='1' else False
    realVNCPath = config.get('vnc','realpath')
    port = config.get('vnc','remoteport')
    return local, realVNCPath, port

def SetVNCSetting(localMark,realPath,port):
    config = ConfigParser()
    config.read(GetAppData()+"settings.ini")
    config['vnc']['local'] = '1' if localMark else '0'
    config['vnc']['realpath'] = realPath
    config['vnc']['remoteport'] = port
    with open(GetAppData()+"settings.ini", 'w') as configfile:
        config.write(configfile)
    