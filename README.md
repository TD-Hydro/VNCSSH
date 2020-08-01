# VNCSSH
## VNC over SSH and many more

A GUI program for easy control of your remote host/cloud with VNC through SSH.

Basically, this project puts what used to need two to three different programs into one.

Of course, if you need to achieve more dedicated tasks, you still need [Putty](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html), 
[Filezilla](https://filezilla-project.org/) and 
[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/).
However, if you just want the simple VNC through ssh, this is your best choice. It is also good for people who just start to learn and access basic cloud computing concepts.

## VNC over SSH
### Why VNC over ssh

- VNC may not be secure. Information is transmitted in plain text.
- Your ports are blocked: you do not have access to a certain port, due to security reasons, etc.

<https://www.cl.cam.ac.uk/research/dtg/attarchive/vnc/sshvnc.html>

## Functions
- Support SSH key file (OpenSSH key) login and password login.

### Terminal

There are two ways to use the terminal: PowerShell (on Windows) or the simple terminal offered in the program. Powershell requires OpenSSH installed on Windows. For Windows version prior to Windows 10 fall 2018 update, check [OpenSSH for Windows](https://www.mls-software.com/opensshd.html) for options. The simple terminal does not need OpenSSH installed.

The simple terminal is in early beta and **DO NOT** use in the production environment. Tests for problems are welcome.
Limitations include but not limited to: no TAB auto-completion, no two key functions (e.g., Ctrl-C), no up/down arrows support.

Using PowerShell in Windows is recommended for terminal applications.

### File Transfer

The program comes with a simple file transfer using SFTP. For now, this is the only way for easy file transferring other than the terminal. Consider adding supports on WinSCP or Filezilla in the future.

### VNC Viewer

There does exist a python based [viewer](https://github.com/TD-Hydro/python-vnc-viewer) 
that can achieve basic tasks and is the **default** VNC viewer offered. However, efficiency and functionality are not as good as the RealVNC® VNC Viewer. The program **does** support both python-based VNC viewer and RealVNC® VNC Viewer from users.

Due to the copyright and license issues, I cannot offer RealVNC Viewer binary files. You need to download or purchase RealVNC Viewer based on your situations (personal and commercial). You can download it from [here](https://www.realvnc.com/en/connect/download/viewer/).

RealVNC® VNC Viewer is not a freeware. RealVNC®, VNC®, and RFB® are trademarks of RealVNC® Limited.

## Limitations

Windows 7 and above are required.

Python 3.5 and above is needed if using the source code. Python 2 is not supported.

Linux and Mac versions are under development. (Actually, if you are using Linux, I do not think this is for you. The terminal is much better than this. Anyhow, I will still work on this.)

### Known issues

Repeating password for Powershell. The SSH key management is optional software and needs to be installed independently. It is not easy to detect if the SSH key management related tools are installed.

## License

Released under the LGPL 3.0 License.