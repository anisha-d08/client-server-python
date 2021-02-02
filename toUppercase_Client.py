import socket

s=socket.socket()
host=socket.gethostname()
port=1441

s.connect((host, port))
x=input("Enter your message: ")
s.send(x.encode())
print(s.recv(1024))

s.close()
