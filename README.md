# urchin

Reverse shell that lets you connect to others computers through the shell when they run the client.

### Supported platforms:
> <h5>Windows</h5>
> <h5>MacOS</h5>
> <h5>Linux</h5>

## What is it?
Urchin is a reverse shell that is writen in `Python 2`. It uses `socket` to send commands over the Internet. Urchin is a reverse-shell, meaning that an attacker can host a server and get the victim to run a client. The client will connect the user to the server, which will grant the attacker shell access to the victim's computer.

## How to use it
> ### 1. Download
> Firstly, on any OS, you would navigate to https://github.com/keeganjk/urchin. Once on this page, click the button that says "Clone or Download" and then "Download as ZIP".
> <br />
> ![Clone or Download](https://github.com/keeganjk/urchin/blob/master/img/clone%20or%20download.gif?raw=true "")
> <br />
> If you are on Unix (Linux, macOS, or BSD), you can type <code>git clone https://github.com/keeganjk/urchin</code> into the terminal to 
> clone this repository and then <code>mv</code> into the directory. If you do this, skip to step 3.

<hr>

> ### 2. Extract files
> Nextly, extract the ZIP file and then move into the <code>urchin</code> folder.

<hr>

> ### 3. Download and install `Python 2` if not already installed
> Navigate to [Python Downloads](https://www.python.org/downloads/release/python-2713) and download `Python 2` for your OS.

<hr>

> ### 4. Run `urchin.py`
> To run `urchin.py`, the process is different depending on your operating system.
> On Windows:
>   1. Click on `urchin.py` and Python will run it.
> On MacOS/Linux:
>   1. Open the terminal.
>   2. Navigate to `urchin.py`
>   3. Type `chmod +x *` to allow e`x`ecution of all files in the directory.
>   4. You can run `urchin.py` by any of the below methods:
>        1. Click on `urchin.py`
>        2. Run `./urchin.py`
>        3. Run `python urchin.py`

<hr>

> ### 6. Build client
> Once you run the script, type `0` and then press enter.
> Next, type your (the server's) IP Address and press enter.
> Type a filename and the client should be generated almost instantly.

<hr>

> ### 7. Give the file to a victim.
> After building the client, you will need to give it to a victim.
> The victim will need to have `Python 2` installed, unless you use the methods below:
>   If the victim is using Windows:<br/>
>     1. Download and install [py2exe](https://sourceforge.net/projects/py2exe/ "py2exe"). <br/>
>     2. Open CMD and run this command: `python filename.py py2exe`<br/>
>     3. Send EXE to victim, put it in a ZIP file if you can't send an EXE.<br/>
>
>   If the victim is using MacOS:<br/>
>     1. Open the terminal and type `chmod +x filename.py`<br/>
>     2. Put the file in a folder<br/>
>     3. Open Disk Utility.<br/>
>     4. From the top menu, select `File` > `New Image` > `Image from Folder...`<br/>
>     5. A DMG will be generated.<br/>
>     6. Send it to your victim.<br/>
> 
>   If the victim is on Linux, you're just about out of luck on compilations. They'll have to `chmod` and run by themself.

<hr>

> ### 8. Allow connections
> Make sure that you allow connections before the client runs the file.
> Once the client has connected, you will pbe notified and you will have a command prompt.
> From here, you can enter commands.
>
> Happy hacking!
