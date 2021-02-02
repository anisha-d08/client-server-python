# -*- coding: utf-8 -*-


import socket

s=socket.socket()
host=socket.gethostname()
port=1567

s.connect((host,port))


while True:
	r=s.recv(1024).decode()
	usr_cmd = input(r)
	s.send(usr_cmd.encode())
	if(usr_cmd == "exit"):
		break
	output = s.recv(1024).decode()
	print(output)    
    
s.close()