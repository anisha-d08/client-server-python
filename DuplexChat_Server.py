import socket

s=socket.socket()
host=socket.gethostname()
port=1444

s.bind((host,port))

print("Waiting for Connection...")
s.listen(5)

conn,addr=s.accept()
print("Connected to ",addr)
rply=conn.recv(1024).decode()

while True:
    if(rply != ''):
        print('Client: ', rply)
        m=input('Server: ')
        conn.send(m.encode())
        rply=conn.recv(1024).decode()
    else:
        break
    
    
conn.close()
s.close()
