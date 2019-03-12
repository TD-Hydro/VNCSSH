# SSHVNC
## VNC over SSH and many more

A GUI program for easy control of your remote host/cloud with VNC through SSH.

Basically, this project puts what used to need two to three different programs into one.

Of course, if you need achieve more dedicated tasks, you still need [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), 
[Filezilla](https://filezilla-project.org/) and 
[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).
However, if you just want the simple VNC through ssh, this is your best choice. It is also good for people who just start to learn and access basic cloud computing concepts.

## VNC over SSH
### Why VNC over ssh

- VNC may not be secure. Many information are transmitted in plain text.
- Your ports are blocked: you do not have access to certain port, due to security reasons etc.

<https://www.cl.cam.ac.uk/research/dtg/attarchive/vnc/sshvnc.html>

## Functions
- Support SSH key file login and password login.

### Terminal

Currently the program is using PowerShell (on Windows) as the terminal.  Powershell requires OpenSSH installed on Windows. For Windows version prior to windows 10 fall 2018 update, please check [OpenSSH for Windows](https://www.mls-software.com/opensshd.html) for options, as you may want to install it.

A simple terminal is under development

<!--
There are two ways using terminal: PowerShell (on Windows) or simple terminal offered in the program. Powershell requires OpenSSH installed on Windows. For Windows version prior to windows 10 fall 2018 update, check [OpenSSH for Windows](https://www.mls-software.com/opensshd.html) for options. Simple terminal should not need OpenSSH installed.
-->

### File Transfer

The program comes with a simple file transfer using SFTP. For now, this is the only way for easy file transferring other than terminal. Consider adding supports on WinSCP or Filezilla in the future.

### VNC Viewer

There does exist a python based [viewer](https://github.com/TD-Hydro/python-vnc-viewer) 
that can achieve basic tasks. However, the efficiency and functionalities are not as good as the RealVNC® VNC Viewer. The program, however, does support user to use RealVNC® VNC Viewer of there own.

Due to the copyright and license issue, I cannot offer RealVNC Viewer binary files. You need to download or purchase RealVNC Viewer based on your situations (personal and commercial). You can download if from [here](https://www.realvnc.com/en/connect/download/viewer/).

RealVNC® VNC Viewer is not a freeware. RealVNC®, VNC® and RFB® are trademarks of RealVNC® Limited.

## Limitations

Windows 7 and above are required.

Python 3.5 and above is needed if using the source code. Python 2 is not supported.

Linux and Mac support are under development. (Actually, if you are using linux, I do not think this is for you. Terminal is much better than this. Anyhow, I will still work on this.)

## How to use

### Python 3

First, install required package.
```
wx, paramiko, pygame, twisted
```
You can use
```
pip3 install wx paramiko pygame twisted
```
to install these packages. If you cannot install twisted, check [this](https://www.lfd.uci.edu/~gohlke/pythonlibs/).

Use command:
```
python3 sshvnc.py
```
This will start the user interfaces.

<!--
### Binaries
Download installation or binary files here.

If you want to use zip packets in Windows, make sure you install the Microsoft Visual C++ Redistributable 2015 or 2017 (x86/x64, depending on your system and download packets).

32-bit version should support Windows on ARM, however, this is not tested. Please use the installation version.
-->

### Known issues
Repeating password for powershell


### Using

To bo done

## License

Released under the MIT License.