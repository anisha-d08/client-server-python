# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:46:50 2020

@author: USER
"""
import socket               

s = socket.socket()            
host = socket.gethostname() 
port = 6565                    
   
s.bind((host, port))
print ('Waiting for Connection...')
s.listen(5)


conn, addr = s.accept() 
print(addr, 'has connected')

filename=input(str('Enter name of the file to be tranferred: '))
with open(filename, 'rb') as file:
    fData = file.read(1024)
    while (fData):
        conn.send(fData)
        fData = file.read(1024)

print('Data trasmitted successfully!')
conn.close()
s.close()
print('Connection closed')