import socket

s=socket.socket()
host=socket.gethostname()
port=1444

s.connect((host,port))

while True:
    msg=input('client : ')
    s.send(msg.encode())
    msg=input('From Client : ')
    if(msg == "exit"):
        break
    s.send(msg.encode())
    
s.close()
