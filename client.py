from socket import *

s = socket()
host = "127.0.0.1"
port = 12345
s.connect( (host,port) )
f = open("torecv.png","wb")
l = s.recv(1024)
while l:
	f.write(l)
	l = s.recv(1024)
f.close()
s.close()
	