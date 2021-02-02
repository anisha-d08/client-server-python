import socket
from datetime import datetime

s=socket.socket()
host=socket.gethostname()
port=1444

s.bind((host,port))

print("Waiting for Connection...")
s.listen(5)

conn,addr=s.accept()
print("Connected to ",addr)
d=datetime.now()
d=d.strftime("Date: %B %d, %Y  Time: %H:%M:%S")
conn.send(d.encode())
    
conn.close()
s.close()
