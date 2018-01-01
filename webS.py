
from socket import *

severport=12000

severSocket=socket(AF_INET,SOCK_STREAM)#Creat a welcome socket to receive any TCP connection request.
severSocket.bind(('',severport))#Binding your IP address with you program port.

severSocket.listen(1)#Listening if there is a TCP connection requestcoming.

while True:
	try:
		connectionSocket,addr=severSocket.accept()#Accept TCP connection and creat an exclusive socket for this TCP connection.
		print('A TCP connection is already built with client:{}'.format(addr[0]))
		messageB=connectionSocket.recv(1024)#Accept TCP message(binarystream) from socket.
		message=messageB.decode()
		print('The request HTTP message is:')
		print(message)
		messageL=message.split()
		filename=messageL[1]
		f=open(filename)
		Status='HTTP/1.1 200 OK\n\n'
		StatusB=Status.encode()
		connectionSocket.send(StatusB)
		lines=f.readlines()
		for i in lines:
			iB=i.encode()
			connectionSocket.send(iB)
		f.close()
		connectionSocket.close()
		severSocket.close()
	except IOError:
		pass
	except OSError:
		pass
	break
