# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b4 on Mon Mar  4 00:24:41 2019
#

import wx
import subprocess
import threading
from multiprocessing import Process

import util.toolBox as tb
import net.sshconn
import util.credread
import util.settingread

from ui.AboutDialog import AboutDialog
from ui.FilenameDialog import FilenameDialog
from ui.SettingFrame import SettingFrame
from ui.FileTransferFrame import FileTransferFrame
from util.update import AsyncUpdateCheck

from paramiko.ssh_exception import NoValidConnectionsError, AuthenticationException
from wx.lib.pubsub import pub

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade

class MainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        ### Internationalization ###
        # Language dictionary
        lang = [wx.LANGUAGE_ENGLISH, wx.LANGUAGE_CHINESE_SIMPLIFIED, wx.LANGUAGE_CHINESE_TRADITIONAL]
        self.locale = wx.Locale(lang[int(util.settingread.GetLangSetting())])
        if self.locale.IsOk():
            self.locale.AddCatalogLookupPathPrefix('locale')
            self.locale.AddCatalog('vncssh')
        ### Class variable ###
        self.sshc = None
        ### Multiprocess Subscribe ###
        pub.subscribe(self.AfterConnection, 'Connected')
        pub.subscribe(self.EnableInfomationChange, 'Fail')

        # begin wxGlade: MainFrame.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((600, 350))
        
        # Menu Bar
        self.frame_menubar = wx.MenuBar()
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu_sub = wx.Menu()
        item = wxglade_tmp_menu_sub.Append(wx.ID_ANY, _(u"Shell\tCtrl+T"), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_shell, id=item.GetId())
        item = wxglade_tmp_menu_sub.Append(wx.ID_ANY, _(u"File Transfer\tCtrl+F"), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_filetrans, id=item.GetId())
        wxglade_tmp_menu.Append(wx.ID_ANY, _(u"&Tools"), wxglade_tmp_menu_sub, _(u""))
        wxglade_tmp_menu.AppendSeparator()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _(u"Check for Updates..."), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_checkUpdate, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _(u"E&xit\tAlt+F4"), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_close, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, _(u"&File"))
        wxglade_tmp_menu = wx.Menu()
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _(u"Help Document\tF1"), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_helpLink, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _(u"Settings"), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_setting, id=item.GetId())
        item = wxglade_tmp_menu.Append(wx.ID_ANY, _(u"About"), _(u""))
        self.Bind(wx.EVT_MENU, self.Menu_about, id=item.GetId())
        self.frame_menubar.Append(wxglade_tmp_menu, _(u"&Help"))
        self.SetMenuBar(self.frame_menubar)
        # Menu Bar end
        self.frame_statusbar = self.CreateStatusBar(1)
        self.comboBoxIP = wx.ComboBox(self, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.textBoxUsr = wx.TextCtrl(self, wx.ID_ANY, _(u""))
        self.authChoice = wx.RadioBox(self, wx.ID_ANY, _(u"Authentication method:"), choices=[_(u"Password"), _(u"Public Key")], majorDimension=1, style=wx.RA_SPECIFY_ROWS)
        self.labelKey = wx.StaticText(self, wx.ID_ANY, _(u"SSH Key File: "), style=wx.ALIGN_LEFT)
        self.choiceKey = wx.Choice(self, wx.ID_ANY, choices=[])
        self.buttonKeyFile = wx.Button(self, wx.ID_ANY, _(u"Add Key"))
        self.labelPswd = wx.StaticText(self, wx.ID_ANY, _(u"Password:"))
        self.textBoxPswd = wx.TextCtrl(self, wx.ID_ANY, _(u""), style=wx.TE_PASSWORD)
        self.textBoxPswdShow = wx.TextCtrl(self, wx.ID_ANY, _(u""))
        self.checkBoxShowPswd = wx.CheckBox(self, wx.ID_ANY, _(u"Show Password"))
        self.buttonConn = wx.Button(self, wx.ID_ANY, _(u"Connect"))
        self.buttonVNC = wx.Button(self, wx.ID_ANY, _(u"Connect to VNC"))

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_RADIOBOX, self.authChoice_onChoose, self.authChoice)
        self.Bind(wx.EVT_BUTTON, self.buttonKeyFile_onClick, self.buttonKeyFile)
        self.Bind(wx.EVT_TEXT_ENTER, self.textBoxPswd_PressEnter, self.textBoxPswd)
        self.Bind(wx.EVT_TEXT_ENTER, self.textBoxPwsdShow_PressEnter, self.textBoxPswdShow)
        self.Bind(wx.EVT_CHECKBOX, self.checkBox_onChange, self.checkBoxShowPswd)
        self.Bind(wx.EVT_BUTTON, self.buttonConn_onClick, self.buttonConn)
        self.Bind(wx.EVT_BUTTON, self.buttonVNC_onClick, self.buttonVNC)
        # end wxGlade

        ### Additional event ###
        self.textBoxUsr.Bind(wx.EVT_KEY_DOWN, self.textBoxUsr_PressTab )
        self.comboBoxIP.Bind(wx.EVT_KEY_DOWN, self.comboBoxIP_PressTab )

    def __set_properties(self):
        # begin wxGlade: MainFrame.__set_properties
        self.SetTitle(_(u"VNC over SSH"))
        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_MENU))
        self.frame_statusbar.SetStatusWidths([-1])
        
        # statusbar fields
        frame_statusbar_fields = [_(u"Not connected")]
        for i in range(len(frame_statusbar_fields)):
            self.frame_statusbar.SetStatusText(frame_statusbar_fields[i], i)
        self.authChoice.SetSelection(0)
        self.labelKey.Hide()
        self.choiceKey.Hide()
        self.buttonKeyFile.Hide()
        self.textBoxPswdShow.Hide()
        self.buttonVNC.Enable(False)
        # end wxGlade

        # Windows icon attachment 
        icon = wx.Icon(wx.IconLocation('./res/remote.ico'))
        self.SetIcon(icon)

    def __do_layout(self):
        # begin wxGlade: MainFrame.__do_layout
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_6 = wx.BoxSizer(wx.VERTICAL)
        sizer_7 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_5 = wx.BoxSizer(wx.VERTICAL)
        sizer_8 = wx.FlexGridSizer(2, 2, 8, 5)
        labelIp = wx.StaticText(self, wx.ID_ANY, _(u"IP Address:"))
        sizer_8.Add(labelIp, 0, wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_8.Add(self.comboBoxIP, 0, wx.ALL | wx.EXPAND, 0)
        labelUsr = wx.StaticText(self, wx.ID_ANY, _(u"Username: "), style=wx.ALIGN_LEFT | wx.ALIGN_RIGHT)
        sizer_8.Add(labelUsr, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 0)
        sizer_8.Add(self.textBoxUsr, 0, wx.ALL | wx.EXPAND, 0)
        sizer_8.AddGrowableCol(1)
        sizer_9.Add(sizer_8, 1, wx.ALL, 10)
        sizer_5.Add(self.authChoice, 0, wx.ALL | wx.EXPAND, 5)
        sizer_9.Add(sizer_5, 2, wx.ALL | wx.EXPAND, 0)
        sizer_1.Add(sizer_9, 0, wx.EXPAND, 0)
        sizer_7.Add(self.labelKey, 0, wx.ALL, 8)
        sizer_7.Add(self.choiceKey, 0, wx.ALL, 5)
        sizer_7.Add(self.buttonKeyFile, 0, wx.ALL, 5)
        sizer_7.Add(self.labelPswd, 0, wx.ALL, 8)
        sizer_7.Add(self.textBoxPswd, 0, wx.ALL, 5)
        sizer_7.Add(self.textBoxPswdShow, 0, wx.ALL, 5)
        sizer_7.Add(self.checkBoxShowPswd, 0, wx.BOTTOM | wx.RIGHT | wx.TOP, 9)
        sizer_1.Add(sizer_7, 1, wx.ALL | wx.EXPAND, 0)
        sizer_6.Add(self.buttonConn, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_6.Add(self.buttonVNC, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)
        sizer_1.Add(sizer_6, 0, wx.EXPAND, 0)
        self.SetSizer(sizer_1)
        self.Layout()
        # end wxGlade

    def Menu_shell(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.sshc == None:
            tb.MBox(_(u_(u_(u"Sever not connected"))), _(u_(u_(u"Not Connected"))), 2)
        else:
            self.sshc.OpenTerminal()
        
    def Menu_filetrans(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.sshc == None:
            tb.MBox(_(u_(u_(u"Sever not connected"))), _(u_(u_(u"Not Connected"))), 2)
        else:
            self.sshc.StartConn()
            fd = FileTransferFrame(self)
            fd.FormInit(self.sshc, self.textBoxUsr.Value)
            fd.Show()

    def Menu_close(self, event):  # wxGlade: MainFrame.<event_handler>
        self.Destroy()

    def Menu_about(self, event):  # wxGlade: MainFrame.<event_handler>
        about = AboutDialog(self)
        about.SetVersionControl(self.version)
        about.ShowModal()
        

    def buttonKeyFile_onClick(self, event):  # wxGlade: MainFrame.<event_handler>
        fileDialog = wx.FileDialog(self, _(u_(u_(u"Open SSH Key File"))), wildcard='SSH key (*.pem)|*.pem', style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        fileDialog.ShowModal()
        pathname = fileDialog.GetPath()
        fileDialog.Destroy()
        if pathname != '':
            newKeyDialog = FilenameDialog(self)
            if (newKeyDialog.ShowModal() == wx.ID_OK):
                newkeypath = newKeyDialog.dTextName.Value
                print(newkeypath)
                if (newkeypath != ''):
                    if (util.credread.CopyPem(pathname, newkeypath)):
                        self.choiceKey.Append(newkeypath)
                else:
                    wx.MessageDialog(
                        None, _(u_(u_(u"Name cannot be an empty string"))), _(u_(u_(u"Info"))), wx.OK).ShowModal()
            newKeyDialog.Destroy()

    def buttonConn_onClick(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.buttonConn.GetLabel() == _(u_(u_(u"Disconnect"))):
            if self.sshc != None:
                self.sshc = None
            self.buttonConn.SetLabel(_(u_(u_(u"Connect"))))
            self.buttonVNC.Disable()
            self.EnableInfomationChange()
            return

        # using domain is allowed
        if self.comboBoxIP.Value == '':
            tb.MBox(_(u_(u_(u"IP address is illegal"))), _(u_(u_(u"Error"))), 2)
            return
        if self.textBoxUsr.Value == '':
            tb.MBox(_(u_(u_(u"Username cannot be empty"))), _(u_(u_(u"Error"))), 2)
            return
        self.buttonConn.Disable()
        self.comboBoxIP.Disable()
        self.textBoxUsr.Disable()
        self.textBoxPswd.Disable()
        self.textBoxPswdShow.Disable()
        self.checkBoxShowPswd.Disable()
        self.choiceKey.Disable()
        self.authChoice.Disable()
        self.buttonConn.Disable()
        # make sure the password is copied
        if self.checkBoxShowPswd.IsChecked():
            self.textBoxPswd.Value = self.textBoxPswdShow.Value
        self.frame_statusbar.SetStatusText(_(u_(u_(u"Connecting..."))))

        keyfile = None
        if self.authChoice.GetSelection() == 1:
            keyfile = util.credread.GetAppData() + self.choiceKey.GetString(self.choiceKey.GetSelection()) + '.pem'
            self.sshc = net.sshconn.SSHConn(self.comboBoxIP.Value, self.textBoxUsr.Value, None, keyfile)
        else:
            self.sshc = net.sshconn.SSHConn(self.comboBoxIP.Value, self.textBoxUsr.Value, self.textBoxPswd.Value,  None)
        
        connThread = AsyncConnectionCheck(self.sshc, self.comboBoxIP.Value)
        connThread.start()
        

    def AfterConnection(self):
        util.credread.ChangeUser(self.textBoxUsr.Value)
        util.credread.UpdateIPList(self.comboBoxIP.Value)
        self.sshc.CloseConn()
        self.buttonVNC.Enable()
        self.buttonConn.Enable()
        self.buttonConn.SetLabel(_(u_(u_(u"Disconnect"))))
        self.frame_statusbar.SetStatusText(_(u_(u_(u"Connected to "))) + self.comboBoxIP.Value)

    def EnableInfomationChange(self):
        self.comboBoxIP.Enable()
        self.textBoxUsr.Enable()
        self.textBoxPswd.Enable()
        self.textBoxPswdShow.Enable()
        self.checkBoxShowPswd.Enable()
        self.choiceKey.Enable()
        self.authChoice.Enable()
        self.buttonConn.Enable()
        self.frame_statusbar.SetStatusText(_(u_(u_(u"Not connected"))))

    def buttonVNC_onClick(self, event):  # wxGlade: MainFrame.<event_handler>
        localport = 5901
        useBuiltIn, RealVNC, portString = util.settingread.GetVNCSetting()
        port = int(portString)
        if self.buttonVNC.Label == _(u_(u_(u"Connect to VNC"))):
            self.sshc.OpenVNCTunnel(localport, port)
            self.buttonVNC.Label = _(u_(u_(u"Disconnect VNC")))
            if useBuiltIn:
                from vnc.vncviewer import InternalCall
                internalVnc = Process(target=InternalCall, args=('localhost', localport, 32))
                internalVnc.daemon = True
                internalVnc.start()
            else:
                subprocess.Popen([RealVNC, 'localhost:{0}'.format(localport)])
        else:
            try:
                self.sshc.StopTunnel(port)
            except KeyError as key:
                print(key)
            finally:
                self.buttonVNC.Label = _(u_(u_(u"Connect to VNC")))

    def authChoice_onChoose(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.authChoice.GetSelection() == 1:
            self.labelKey.Show()
            self.choiceKey.Show()
            self.buttonKeyFile.Show()
            self.labelPswd.Hide()
            self.textBoxPswd.Hide()
            self.textBoxPswdShow.Hide()
            self.checkBoxShowPswd.Hide()
            self.Layout()
        else:
            self.labelKey.Hide()
            self.choiceKey.Hide()
            self.buttonKeyFile.Hide()
            self.labelPswd.Show()
            self.textBoxPswd.Show()
            self.textBoxPswdShow.Hide()
            self.checkBoxShowPswd.Show()
            self.Layout()

    def Menu_helpLink(self, event):  # wxGlade: MainFrame.<event_handler>
        tb.OpenALink('https://vncssh.tdhydro.com/')

    def Menu_setting(self, event):  # wxGlade: MainFrame.<event_handler>
        setting = SettingFrame(self)
        setting.LoadSetting()
        setting.Show()

    def checkBox_onChange(self, event):  # wxGlade: MainFrame.<event_handler>
        if self.checkBoxShowPswd.IsChecked():
            self.textBoxPswd.Hide()
            self.textBoxPswdShow.Show()
            self.textBoxPswdShow.Value = self.textBoxPswd.Value
            self.Layout()
        else:
            self.textBoxPswd.Show()
            self.textBoxPswdShow.Hide()
            self.textBoxPswd.Value = self.textBoxPswdShow.Value
            self.Layout()

    def textBoxPswd_PressEnter(self, event):  # wxGlade: MainFrame.<event_handler>
        self.buttonConn_onClick(event)

    def textBoxPwsdShow_PressEnter(self, event):  # wxGlade: MainFrame.<event_handler>
        self.buttonConn_onClick(event)

    def Menu_checkUpdate(self, event):  # wxGlade: MainFrame.<event_handler>
        updateCheck = AsyncUpdateCheck(self.version, True)
        updateCheck.start()


    def CurrentVersion(self, version):
        self.version = version
    
    ##### Tab #####

    def textBoxUsr_PressTab(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_TAB:
            if self.checkBoxShowPswd.IsChecked():
                self.textBoxPswdShow.SetFocus()
            else:
                self.textBoxPswd.SetFocus()
        event.Skip()
    def comboBoxIP_PressTab(self, event):
        key = event.GetKeyCode()
        if key == wx.WXK_TAB:
            self.textBoxUsr.SetFocus()
        event.Skip()
    
# end of class MainFrame


class AsyncConnectionCheck(threading.Thread):
    def __init__(self, sshc, ip):
        threading.Thread.__init__(self)
        self.sshc = sshc
        self.ip = ip
    def run(self):
        try:
            self.sshc.StartConn()
            wx.CallAfter(pub.sendMessage, 'Connected')
        except NoValidConnectionsError as nce:
            tb.MBox(_(u_(u_(u"Connect to server "))) + self.ip + _(u_(u_(u" failed: \n"))) + str(nce),_(u_(u_(u"Error"))), 2)
            wx.CallAfter(pub.sendMessage,'Fail')
        except TimeoutError as te:
            tb.MBox(_(u_(u_(u"Connect to server "))) + self.ip + _(u_(u_(u" failed: \n"))) + str(te),_(u_(u_(u"Error"))), 2)
            wx.CallAfter(pub.sendMessage,'Fail')
        except AuthenticationException as ae:
            tb.MBox(_(u_(u_(u"Connect to server "))) + self.ip + _(u_(u_(u" failed: \n"))) + str(ae),_(u_(u_(u"Error"))), 2)
            wx.CallAfter(pub.sendMessage,'Fail')
        except Exception as e:
            tb.MBox(_(u_(u_(u"Connect to server "))) + self.ip + _(u_(u_(u" failed: \n"))) + str(e),_(u_(u_(u"Error"))), 2)
            wx.CallAfter(pub.sendMessage, 'Fail')