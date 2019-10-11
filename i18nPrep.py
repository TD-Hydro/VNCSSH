import sys

def ChangeFile(fileName):
    f = open(fileName, "r", encoding="utf-8")

    lines = []

    for l in f:
        lx = l.split("\"")
        if len(lx) == 1:
            nl = l
        elif lx[1] == "style":
            nl = l
        elif lx[0][-1] == "u":
            nl = l
        else:
            nl = lx[0]
            leftbr = True
            for ls in lx[1:]:
                if leftbr:
                    nl = nl + "_(u\"" + ls
                    leftbr = False
                else:
                    nl = nl + "\")" + ls
                    leftbr = True

        lines.append(nl)
    f.close()

    f = open(fileName, "w")
    for l in lines:
        f.write(l)
    f.close()

def ReverseFile(fileName):
    f = open(fileName, "r")

    lines = []

    for l in f:
        l = l.replace("\")\r\n","\"\r\n")
        l = l.replace("\"):","\":")
        l = l.replace("_(u\"","\"")
        l = l.replace("\")","\"")

        lines.append(l)
    f.close()

    f = open(fileName, "w")
    for l in lines:
        f.write(l)
    f.close()

if len(sys.argv) >= 3:
    if sys.argv[1] == "replace":
        ChangeFile(sys.argv[2])
    elif sys.argv[1] == "reverse":
        ReverseFile(sys.argv[2])
elif len(sys.argv) == 2:
    if sys.argv[1] == "replace":
        ChangeFile("ui/MainFrame.py")
        #ChangeFile("ui/FileTransferFrame.py")
        ChangeFile("ui/FileNameDialog.py")
        ChangeFile("ui/AboutDialog.py")
        ChangeFile("ui/SettingFrame.py")
        ChangeFile("util/update.py")
    elif sys.argv[1] == "reverse":
        ReverseFile("ui/MainFrame.py")
        ReverseFile("ui/FileTransferFrame.py")
        ReverseFile("ui/FileNameDialog.py")
        ReverseFile("ui/AboutDialog.py")
        ReverseFile("ui/SettingFrame.py")
        ReverseFile("util/update.py")
else:
    ReverseFile("ui/MainFrame.py")
    ReverseFile("ui/FileTransferFrame.py")
    ReverseFile("ui/FileNameDialog.py")
    ReverseFile("ui/AboutDialog.py")
    ReverseFile("ui/SettingFrame.py")
    ReverseFile("util/update.py")
    ChangeFile("ui/MainFrame.py")
    ChangeFile("ui/FileTransferFrame.py")
    ChangeFile("ui/FileNameDialog.py")
    ChangeFile("ui/AboutDialog.py")
    ChangeFile("ui/SettingFrame.py")
    ChangeFile("util/update.py")

    
            
