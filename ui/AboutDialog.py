# -*- coding: UTF-8 -*-
#
# generated by wxGlade 0.8.0b4 on Mon Mar  4 00:24:41 2019
#

import wx
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class AboutDialog(wx.Dialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: AboutDialog.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE
        wx.Dialog.__init__(self, *args, **kwds)
        self.SetSize((320, 240))
        self.label_1 = wx.StaticText(self, wx.ID_ANY, "")
        self.button_1 = wx.Button(self, wx.ID_ANY, "OK")

        self.__set_properties()
        self.__do_layout()

        self.Bind(wx.EVT_BUTTON, self.aboutOK_onClick, self.button_1)
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: AboutDialog.__set_properties
        self.SetTitle("About")
        self.SetSize((320, 240))
        self.button_1.SetMinSize((90, 30))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: AboutDialog.__do_layout
        sizer_12 = wx.BoxSizer(wx.VERTICAL)
        sizer_13 = wx.BoxSizer(wx.VERTICAL)
        sizer_16 = wx.BoxSizer(wx.HORIZONTAL)
        bitmap_1 = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("./res/remote.png", wx.BITMAP_TYPE_ANY))
        bitmap_1.SetMinSize((64, 64))
        sizer_16.Add(bitmap_1, 0, wx.ALL, 25)
        sizer_16.Add(self.label_1, 0, wx.TOP, 25)
        sizer_12.Add(sizer_16, 1, wx.EXPAND, 0)
        sizer_13.Add(self.button_1, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.BOTTOM | wx.RIGHT, 25)
        sizer_12.Add(sizer_13, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT, 0)
        self.SetSizer(sizer_12)
        self.Layout()
        # end wxGlade
    
    def SetVersionControl(self, version):
        self.label_1.SetLabel("VNC over SSH\n{0} Beta\n\nCopyright (C) 2019\nTD-Hydro".format(version))

    def aboutOK_onClick(self, event):  # wxGlade: AboutDialog.<event_handler>
        self.Destroy()

# end of class AboutDialog