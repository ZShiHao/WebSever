
from socket import *

severport=12000

#创建欢迎套接字
severSocket=socket(AF_INET,SOCK_STREAM)
severSocket.bind(('192.168.123.226',severport))

severSocket.listen(1)#聆听是否有TCP连接请求

while True:
	try:
		connectionSocket,addr=severSocket.accept()#创建连接套接字，完成三次握手
		print('A TCP connection is already built with client:{}'.format(addr[0]))
		messageB=connectionSocket.recv(1024)#接收通过TCP发来的报文
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
