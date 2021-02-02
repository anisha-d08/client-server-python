import socket
import getmac

s=socket.socket()
host=socket.gethostname();
hostName=socket.gethostbyname(host)
hostName=str(hostName)
port=4444

s.bind((host,port))
print("Waiting for IP address...")
s.listen(5)

while True:
	conn,addr=s.accept()
	ip=conn.recv(1024).decode()
	ip=str(ip)
	if(hostName==ip):
		mac = getmac.get_mac_address()
		mac=str(mac)
		conn.send(mac.encode())
		print("MAC/Ethernet Address > ", getmac.get_mac_address())
	break

conn.close()
s.close()
