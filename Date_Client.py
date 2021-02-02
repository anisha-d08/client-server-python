import socket

s=socket.socket()
host=socket.gethostname()
port=1444

s.connect((host,port))
dt= s.recv(1024).decode()
print("From Server: ", dt)
    
s.close()
