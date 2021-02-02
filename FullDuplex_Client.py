import socket

s=socket.socket()
host=socket.gethostname()
port=1444

s.connect((host,port))

msg=input('Client ~> ')
s.send(msg.encode())

while True:
	r=s.recv(1024).decode()
	print("Server ~> ", r)
	msg=input('Client ~> ')
	if(msg == "exit"):
		break
	s.send(msg.encode())
    
s.close()