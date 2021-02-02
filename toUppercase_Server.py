import socket

#socket.socket (family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None)
s=socket.socket()
host=socket.gethostname()
port=1441

s.bind((host, port))

print("Waiting for Connection...")
s.listen(5)
conn, addr=s.accept()
print("Connected to ", addr)
r=conn.recv(1024)
upper_r=r.upper()
conn.send(upper_r)

conn.close()
s.close()
