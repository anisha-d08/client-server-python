import socket

s=socket.socket()
host=socket.gethostname()
port=1444

s.bind((host,port))

print("Waiting for Connection...")
s.listen(5)

conn,addr=s.accept()
print("Connected to ",addr)

while True:
    rply=conn.recv(1024).decode()
    print('From Client: ', rply)
    #conn.send(r.encode())
    
conn.close()
s.close()
