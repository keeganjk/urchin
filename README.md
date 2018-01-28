# urchin
[![Donate](https://img.shields.io/badge/donate-%24-green.svg)](https://keeganjk.github.io/donate/)

 ~~~
   |     |  | ,--` ,--` |  | --- ,--`
\ * /   |  | |  | |    |  |  |  |  |
-*+*-   |  | |--, |    |--|  |  |  |
/ * \   |  | | \  |    |  |  |  |  |
   |     `__, |  \ `__, |  | --- |  |

Developer : keeganjk
Version   : v1.4 (Pickelhelm)
~~~
 
Reverse shell that lets you connect to others computers through the shell when they run the client.
 
### Supported platforms:
> <h5>Windows</h5>
> <h5>MacOS</h5>
> <h5>Linux</h5

# Contents
- [What is it?](#what-is-it)
- [How to use it](#use)
  - [Run Urchin](#run-urchin)
  - [Building client](#build)
    - [Installing PyInstaller](#dipyinstaller)
    - [Using PyInstaller](#piuse)
  - [Allow connections/Give file to client](#listen)
    - [Custom commands](#custom-cmd)
- [Download and Install](#dli)
  - [Download](#dl)
  - [Extract files](#extract)
  - [Download/Install Python](#dlipy)
 
## What is it? <a id="what-is-it">
Urchin is a reverse shell that is writen in `Python 2`. It uses `socket` to send commands over the Internet. Urchin is a reverse-shell, meaning that a server can host a server and get the client to run the client script. The client will connect the user to the server, which will grant the server shell access to the client's computer.
 
## How to use it <a id="use"> 
 
> ### 1. Run `urchin.py` <a id="run-urchin">
> To run `urchin.py`, the process is different depending on your operating system.
> On Windows:
>   1. Click on `urchin.py` and Python will run it.
> On MacOS/Linux:
>   1. Open the terminal.
>   2. Navigate to `urchin.py`
>   3. Type `chmod +x *` to allow e`x`ecution of all files in the directory.
>   4. You will have to remove the `.py` extension or replace it with `.command`.
>   5. You can run `urchin` by any of the below methods:
>        1. Click on `urchin`
>        2. Run `./urchin`
>        3. Run `python urchin` <br/>
>
> <i><b>If you have an error when opening `urchin`, kill any `Python` background processes with Task Manager on Windows or `kill` in Unix.</b></i>

<hr>

> ### 2. Build client <a id="build">
> Once you ran `urchin.py`, type `0` to `Build client file`. It will ask you for the server's (mostly likey your) IP Address. If the `client` is on the same network as you, open a terminal and type `ifconfig` (`ipconfig` if you are on Windows) and it will output some text. Your local IP should start with `192.168.`, `172.16.`, or `10.`.  If the `client` is not on the same network as you, use the address found on `icanhazip.com`.
> You can choose to generate a Python file or a BASh/nc "blind" file. The Python file will work on any OS if Python 2 is installed or if you compile it for their device with [PyInstaller](http://www.pyinstaller.org/ "Pyinstaller"). BASh/nc should work on Mac/Linux and instead of the person connecting to you, you connect to them, but you can't see the output of any commands.
> Next, it will ask for a filename. Enter the name you want the `client` file to be called.
> If you are using the Python file, you can edit the `client.py` file. Find the line that says `host = '127.0.0.1'`. Replace `'127.0.0.1'` with  the server's IP Address surrounded by single quotes. If you're using the BASh/nc method, you can simply use `listener.command`.
> 
> Here are the steps to install PyInstaller: <a id="dipyinstaller">
>
> Windows:
> 1. Open CMD
> 2. Enter the following commands:
~~~
cd C:\Python27\Scripts
pip install --upgrade pip
pip install pyinstaller
~~~
>             
> MacOS:
> 0. Log into admin profile or any profile in `/etc/sudoers`
> 1. Open Terminal
> 2. Enter `sudo python -m easy_install pip` and type your password
> 3. Enter `sudo python -m pip install pyinstaller`
>
> Linux:
> 0. Log into admin profile or any profile in `/etc/sudoers`
> 1. Open Terminal
> 2. Enter `sudo python -m pip install pyinstaller`
>
> If the client is using MacOS, they have `Python 2` installed already. You can use PyInstaller (instructions above) or package the `client` into an app like so:<br/>
>
> 1. Open the terminal and type `chmod +x filename`<br/>
> 2. Put the file in a folder<br/>
> 3. Open Disk Utility.<br/>
> 4. From the top menu, select `File` > `New Image` > `Image from Folder...`<br/>
> 5. A DMG will be generated.<br/>
> 
> If the client is on Linux, they probably have `Python` installed already. You can use PyInstaller anyway. <br />
>
> Using PyInstaller: <a id="piuse">
>     To use PyInstaller, type this into Terminal/CMD<sup>0</sup><sup>1</sup><sup>2</sup>:
>          `pyinstaller -F filename`
>
> <sup>0</sup> If you are using Windows, use `C:\Python27\Scripts\pyinstaller.exe -F filename` <br/>
> <sup>1</sup> If you are using Windows or MacOS, you can use `--nowindowed` after `-F` to make no console window appear. <br/>
> <sup>2</sup> The executable will be held in the `dist` folder which is created if it doesn't exist.
 
<hr>
 
> ### 3. Allow connections and give the file to the client. <a id="listen">
> If using the Python method, select 1 or 2. Once listening for connections, give the client the file: email, FTP, USB, etc. should work. If you can't send the file, put it in a `ZIP` file.
> If the user is on Windows, you can make the connection persist like so:
> 1. Press Windows Key + R and enter `shell:startup`.
> 2. If you get the `client` file in the directory thtat opens up, it will start every time the user logs in.
>
> Once the `client` has connected, you will be notified and you will have a command prompt of `$ `.
> From here, you can enter commands to run on the client. There are also custom commands which only exist in `Urchin`, listed below.
<a id="custom-cmd">
<code>bash</code> : Opens a BASh shell if possible <br/>
<code>browser</code> : Allows you to open a web browser on clients machine(s) <br/>
<code>exit</code> or <code>quit</code> : Closes connection <br/>
<code>flood</code> : Allows you to flood a specified URL with GET requests <br/>
<code>help</code> : Displays help menu <br/>
<code>info</code> : Finds info about target, including OS, node, and processor <br/>
<code>list</code> : Lists connected machines <br/>
<code>python</code> : Opens a Python shell <br/>
> If using the BASh/nc method, select 3. From here, it is simply a blind BASh shell. The listener will have had to run the listener before you connect. You can give the file with email, FTP, USB, etc. should work. If you can't send the file, you can put it in a `ZIP` file.

## Download and Install <a id="dli">
> ### 1. Download <a id="dl">
> Firstly, on any OS, you would navigate to https://github.com/keeganjk/urchin. Once on this page, click the button that says "Clone or Download" and then "Download as ZIP".
> <br />
> ![Clone or Download](https://github.com/keeganjk/urchin/blob/master/img/clone%20or%20download.gif?raw=true "")
> <br /> If you are on Unix (Linux, macOS, or BSD), you can type <code>git clone https://github.com/keeganjk/urchin</code> into the terminal to 
> clone this repository and then <code>mv</code> into the directory. If you do this, skip to step 3.

<hr>

> ### 2. Extract files <a id="extract">
> Nextly, extract the ZIP file and then move into the `urchin` folder.

<hr>

> ### 3. Download and install `Python 2` if not already installed <a id="dlipy">
> Navigate to [Python Downloads](https://www.python.org/downloads/release/python-2713) and download `Python 2` for your OS.
