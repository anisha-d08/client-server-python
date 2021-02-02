import socket

sock=socket.socket()
host=socket.gethostname()
port=4444
hostIP=socket.gethostbyname(host)

sock.connect((host,port))

ipAdd=input("IP address > ")
sock.send(ipAdd.encode())

print("IP address sent.")
mac = sock.recv(1024).decode()
print("MAC Address > ", mac)
sock.close()
