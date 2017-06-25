#!/usr/bin/python
import socket, os, sys, platform

if 'Windows' in platform.system():
	os.system('cls')
	print "                     |     |   | ,---` ,---` |   | ----- ,---`"
	print "                   \ * /   |   | |   | |     |   |   |   |   |"
	print "                   -*+*-   |   | |---, |     |---|   |   |   |"
	print "                   / * \   |   | |  \  |     |   |   |   |   |"
	print "                     |     `___, |   \ `___, |   | ----- |   |"
	print ""
	print "                         Made by Keegan Kuhn (keeganjk)"
	print "                                 Version: 1.0"
else:
	os.system("clear")
	col = os.popen("echo $COLUMNS", "r").read()
	col = int(col)
	string = "                     |     |   | ,---` ,---` |   | ----- ,---`"
	string = string.center(col)
	print string
	string = "                   \ * /   |   | |   | |     |   |   |   |   |"
	string = string.center(col)
	print string
	string = "                   -*+*-   |   | |---, |     |---|   |   |   |"
	string = string.center(col)
	print string
	string = "                   / * \   |   | |  \  |     |   |   |   |   |"
	string = string.center(col)
	print string
	string = "                     |     `___, |   \ `___, |   | ----- |   |"
	string = string.center(col)
	print string
	string = ""
	string = string.center(col)
	print string
	string = "                         Made by Keegan Kuhn (" + "\033[1;31m" + "keeganjk" + "\033[0;0m" + ")"
	string = string.center(col)
	print string
	string = "                                 Version: 1.0"
	string = string.center(col)
	print string

port = 31337
s = socket.socket()
s.bind(('', port))
print ""
print "                           Waiting for connection ..."
s.listen(1)
while True:
	c, addr = s.accept()
	print "                 Accepted connection from", addr, "!"
        print ""
	while True:
		cmd = raw_input("$ ")
		if cmd == "python":
			while cmd != "exit()":
				cmd = raw_input(">>> ")
				if cmd == "exit":
					print "Use exit() to exit"
				cmd = "python -c '" + cmd + "'"
				c.send(cmd)
				print c.recv(1024)
				
		elif cmd == "bash":
			while True:
				cmd = raw_input("bash$ ")
				cmd = "bash -c '" + cmd + "'"
				c.send(cmd)
				print c.recv(1024)
		
		elif cmd == "quit" or cmd == "exit":
			c.send('quit')
			s.close()
		        sys.exit(1)
		else:
		        c.send(cmd)
			print c.recv(1024)
