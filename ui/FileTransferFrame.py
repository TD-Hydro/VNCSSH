# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b4 on Mon Mar  4 00:24:41 2019
#

import wx
import os
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class FileTransferFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: FileTransferFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((808, 603))
        self.buttonLocalBack = wx.Button(self, wx.ID_ANY, u"\u2190")
        self.buttonLocalUp = wx.Button(self, wx.ID_ANY, u"\u2191")
        self.buttonLocalRefresh = wx.Button(self, wx.ID_ANY, u"\u27f3")
        self.textLocalDir = wx.TextCtrl(self, wx.ID_ANY, "")
        self.buttonRemoteBack = wx.Button(self, wx.ID_ANY, u"\u2190")
        self.buttonRemoteUp = wx.Button(self, wx.ID_ANY, u"\u2191")
        self.buttonRemoteRefresh = wx.Button(self, wx.ID_ANY, u"\u27f3")
        self.textRemoteDir = wx.TextCtrl(self, wx.ID_ANY, "")
        self.listLocalDir = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT)
        self.listRemoteDir = wx.ListCtrl(self, wx.ID_ANY, style=wx.LC_REPORT)
        self.buttonUpload = wx.Button(self, wx.ID_ANY, "Upload")
        self.buttonDownload = wx.Button(self, wx.ID_ANY, "Download")
        self.progressBar = wx.Gauge(self, wx.ID_ANY, 1)

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.localBack_onClick, self.buttonLocalBack)
        self.Bind(wx.EVT_BUTTON, self.localUp_onClick, self.buttonLocalUp)
        self.Bind(wx.EVT_BUTTON, self.localRefresh_onClick, self.buttonLocalRefresh)
        self.Bind(wx.EVT_TEXT_ENTER, self.localDir_enterPress, self.textLocalDir)
        self.Bind(wx.EVT_BUTTON, self.remoteBack_onClick, self.buttonRemoteBack)
        self.Bind(wx.EVT_BUTTON, self.remoteUp_onClick, self.buttonRemoteUp)
        self.Bind(wx.EVT_BUTTON, self.remoteRefresh_onClick, self.buttonRemoteRefresh)
        self.Bind(wx.EVT_TEXT_ENTER, self.remoteDir_enterPress, self.textRemoteDir)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.listLocalDir_onClick, self.listLocalDir)
        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.listRemoteDir_onClick, self.listRemoteDir)
        self.Bind(wx.EVT_BUTTON, self.buttonUpload_Click, self.buttonUpload)
        self.Bind(wx.EVT_BUTTON, self.buttonDownload_onClick, self.buttonDownload)
        # end wxGlade

        self.Bind(wx.EVT_CLOSE, self.onClose)

    def __set_properties(self):
        # begin wxGlade: FileTransferFrame.__set_properties
        self.SetTitle("File Transfer")
        _icon = wx.NullIcon
        _icon.CopyFromBitmap(wx.Bitmap("./res/remote.ico", wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        self.buttonLocalBack.SetMinSize((35, 35))
        self.buttonLocalBack.SetToolTip("Go back")
        self.buttonLocalUp.SetMinSize((35, 35))
        self.buttonLocalUp.SetToolTip("Go up")
        self.buttonLocalRefresh.SetMinSize((35, 35))
        self.buttonRemoteBack.SetMinSize((35, 35))
        self.buttonRemoteBack.SetToolTip("Go back")
        self.buttonRemoteUp.SetMinSize((35, 35))
        self.buttonRemoteUp.SetToolTip("Go up")
        self.buttonRemoteRefresh.SetMinSize((35, 35))
        self.listLocalDir.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=30)
        self.listLocalDir.AppendColumn("File", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.listLocalDir.AppendColumn("Type", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.listRemoteDir.AppendColumn("", format=wx.LIST_FORMAT_LEFT, width=30)
        self.listRemoteDir.AppendColumn("File name", format=wx.LIST_FORMAT_LEFT, width=-1)
        self.listRemoteDir.AppendColumn("Type", format=wx.LIST_FORMAT_LEFT, width=-1)
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: FileTransferFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        grid_sizer_3 = wx.FlexGridSizer(3, 2, 0, 0)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(self.buttonLocalBack, 0, 0, 0)
        sizer_2.Add(self.buttonLocalUp, 0, 0, 0)
        sizer_2.Add(self.buttonLocalRefresh, 0, 0, 0)
        sizer_2.Add(self.textLocalDir, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(sizer_2, 1, wx.EXPAND, 0)
        sizer_3.Add(self.buttonRemoteBack, 0, 0, 0)
        sizer_3.Add(self.buttonRemoteUp, 0, 0, 0)
        sizer_3.Add(self.buttonRemoteRefresh, 0, 0, 0)
        sizer_3.Add(self.textRemoteDir, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(sizer_3, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.listLocalDir, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.listRemoteDir, 1, wx.EXPAND, 0)
        grid_sizer_3.Add(self.buttonUpload, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.Add(self.buttonDownload, 0, wx.ALIGN_CENTER, 0)
        grid_sizer_3.AddGrowableRow(1)
        grid_sizer_3.AddGrowableCol(0)
        grid_sizer_3.AddGrowableCol(1)
        sizer_1.Add(grid_sizer_3, 1, wx.EXPAND, 0)
        sizer_1.Add(self.progressBar, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def onClose(self, event):
        self.sshc.CloseConn()
        self.Destroy()

    def FormInit(self, sshc):
        if not hasattr(self, "pathHistory"):
            self.pathHistory = []
        if not hasattr(self, "remotePathHistory"):
            self.remotePathHistory = []
        self.sshc = sshc
        path = ""
        self.ShowLocalDir(path)
        pathRemote = "/root/"
        self.ShowRemoteDir(pathRemote)

    def TransferProgressSend(self, transferred, remaining):
        self.progressBar.SetValue(transferred/2/remaining)

    def TransferProgressRecv(self, transferred, remaining):
        self.progressBar.SetValue(transferred/2/remaining + 0.5)

    def GetWindowsDirStructure(self, path):
        dirList = []
        if path == "" or path == "\\":
            dl = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
            drives = ['%s:' % d for d in dl if os.path.exists('%s:' % d)]
            for d in drives:
                dirList.append(("\U0001f4c1", d, "Folder"))
        else:
            for df in os.listdir(path):
                if df[0] == "$":
                    continue
                elif not os.path.isfile(path + df):
                    dirList.append(("\U0001f4c1", df, "Folder"))
            for df in os.listdir(path):
                if df[0] == "$":
                    continue
                elif os.path.isfile(path + df):
                    dt = "File"
                    if len(df.split(".")) > 1:
                        dt = df.split(".")[-1].upper() + " file"
                    dirList.append(("\U0001f5cb", df, dt))
        return dirList
        
    def GetUnixDirStructure(self, pathFolder, pathFile):
        dirList = []
        for f1 in pathFolder:
            dirList.append(("\U0001f4c1", f1, "Folder"))
        for f2 in pathFile:
            dt = "File"
            if len(f2.split(".")) > 1:
                dt = f2.split(".")[-1].upper() + " file"
            dirList.append(("\U0001f5cb", f2, dt))
        return dirList

    def ShowLocalDir(self, path):
        self.listLocalDir.DeleteAllItems()
        self.pathHistory.append(path)
        # To prevent too much history
        if len(self.pathHistory) > 10:
            self.pathHistory.pop(0)
        try:
            dirList = self.GetWindowsDirStructure(path)
            for d in dirList:
                self.listLocalDir.Append(d)
        except PermissionError:
            dial = wx.MessageDialog(
                None, 'Permission is denied: \'' + path + '\'', 'Error', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()
            
        finally:
            self.textLocalDir.Value = path

    def ShowRemoteDir(self, path):
        self.listRemoteDir.DeleteAllItems()
        if path == "":
            path = "/"
        self.remotePathHistory.append(path)
        (pathFolder, pathFile) = self.sshc.ListRemoteFile(path)
        # To prevent too much history
        if len(self.remotePathHistory) > 10:
            self.remotePathHistory.pop(0)
        try:
            dirlist = self.GetUnixDirStructure(pathFolder, pathFile)
            for d in dirlist:
                self.listRemoteDir.Append(d)
        except PermissionError:
            dial = wx.MessageDialog(
                None, 'Permission is denied: \'' + path + '\'', 'Error', wx.OK | wx.ICON_ERROR)
            dial.ShowModal()
        finally:
            self.textRemoteDir.Value = path

    def listLocalDir_onClick(self, event): # wxGlade: FileTransferFrame.<event_handler>
        dirType = self.listLocalDir.GetItem(event.GetIndex(), 2).GetText()
        if dirType == "Folder":
            if self.pathHistory[-1] != "\\":
                path = self.pathHistory[-1] + \
                    self.listLocalDir.GetItem(
                        event.GetIndex(), 1).GetText() + "\\"
            else:
                path = self.listLocalDir.GetItem(
                    event.GetIndex(), 1).GetText() + "\\"
            self.ShowLocalDir(path)
        else:
            self.buttonUpload_Click(event)

    def localUp_onClick(self, event):  # wxGlade: FileTransferFrame.<event_handler>
        path = self.pathHistory[-1][:-1]
        upId = path.rfind("\\")
        path = path[:upId+1]
        self.ShowLocalDir(path)

    def localBack_onClick(self, event):  # wxGlade: FileTransferFrame.<event_handler>
        try:
            self.pathHistory.pop()
            path = self.pathHistory.pop()
        except IndexError:
            self.pathHistory.append(self.textLocalDir.Value)
            return
        self.ShowLocalDir(path)

    def buttonUpload_Click(self, event): # wxGlade: FileTransferFrame.<event_handler>
        self.progressBar.SetValue(0)
        fileName = self.listLocalDir.GetItem(
            self.listLocalDir.FocusedItem, 1).GetText()
        filePath = self.pathHistory[-1]
        remotePath = self.remotePathHistory[-1]
        result = self.sshc.SendFile(
            filePath + fileName, fileName, remotePath, self.TransferProgressSend)
        if (result):
            self.progressBar.SetValue(1)
            self.remoteRefresh_onClick(event)
    
    def localRefresh_onClick(self, event): # wxGlade: FileTransferFrame.<event_handler>
        path = self.pathHistory[-1]
        if path[-1] != "\\":
            path += "\\"
        self.ShowLocalDir(path)

    def localDir_enterPress(self, event): # wxGlade: FileTransferFrame.<event_handler>
        path = self.textLocalDir.Value
        if path[-1] != "\\":
            path += "\\"
        self.ShowLocalDir(path)

    def remoteBack_onClick(self, event): # wxGlade: FileTransferFrame.<event_handler>
        try:
            self.remotePathHistory.pop()
            path = self.remotePathHistory.pop()
        except IndexError:
            self.remotePathHistory.append(self.textRemoteDir.Value)
            return
        self.ShowRemoteDir(path)

    def remoteUp_onClick(self, event):  # wxGlade: FileTransferFrame.<event_handler>
        path = self.remotePathHistory[-1][:-1]
        upId = path.rfind("/")
        path = path[:upId+1]
        self.ShowRemoteDir(path)

    def remoteRefresh_onClick(self, event): # wxGlade: FileTransferFrame.<event_handler>
        path = self.remotePathHistory[-1]
        if path[-1] != "/":
            path += "/"
        self.ShowRemoteDir(path)

    def remoteDir_enterPress(self, event): # wxGlade: FileTransferFrame.<event_handler>
        path = self.textRemoteDir.Value
        if path[-1] != "/":
            path += "/"
        self.ShowRemoteDir(path)

    def buttonDownload_onClick(self, event): # wxGlade: FileTransferFrame.<event_handler>
        self.progressBar.SetValue(0)
        fileName = self.listRemoteDir.GetItem(
            self.listRemoteDir.FocusedItem, 1).GetText()
        filePath = self.remotePathHistory[-1]
        localPath = self.pathHistory[-1]
        self.sshc.GetFile(filePath + fileName, fileName, localPath, self.TransferProgressRecv)
        self.localRefresh_onClick(event)

    def listRemoteDir_onClick(self, event): # wxGlade: FileTransferFrame.<event_handler>
        dirType = self.listRemoteDir.GetItem(event.GetIndex(), 2).GetText()
        if dirType == "Folder":
            path = self.remotePathHistory[-1] + \
                self.listRemoteDir.GetItem(event.GetIndex(), 1).GetText() + "/"
            self.ShowRemoteDir(path)
        else:
            self.buttonDownload_onClick(event)

# end of class FileTransferFrame