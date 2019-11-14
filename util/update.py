import threading
import wx
import urllib.request
import util.toolBox as tb

class AsyncUpdateCheck(threading.Thread):
    def __init__(self, appVersion, activeCheck):
        threading.Thread.__init__(self)
        self.appVersion = appVersion
        self.activeCheck = activeCheck
    def run(self):
        try:
            newestVersion = urllib.request.urlopen('https://raw.githubusercontent.com/TD-Hydro/VNCSSH/master/CHANGELOG.md').readline()[3:-1].decode('utf-8')
            print(newestVersion, self.appVersion, newestVersion > self.appVersion)
            if (newestVersion > self.appVersion):
                dlg = wx.MessageDialog(None, "A new version {0} of VNCSSH is avaliable. Download now?".format(newestVersion), "Update", wx.YES_NO | wx.ICON_QUESTION)
                if (dlg.ShowModal() == wx.ID_YES):
                    tb.OpenALink('https://github.com/TD-Hydro/VNCSSH/releases/tag/v.{0}'.format(newestVersion))
                dlg.Destroy()
            elif self.activeCheck:
                tb.MBox("Your VNCSSH is up to date.", "Update", 0)
        except:
            pass