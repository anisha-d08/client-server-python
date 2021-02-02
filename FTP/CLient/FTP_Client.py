# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 13:47:29 2020

@author: USER
"""
import socket

s = socket.socket() 
host = socket.gethostname()
port = 6565 

s.connect((host, port))
filename=input(str('Give any name to file: '))

with open(filename, 'wb') as file:
    print ('File opened')
    print('Receiving data...')
    data = s.recv(1024)
    print('DATA -->', (data.decode()))
    #if not data:
        #break
    #write data to a file
    file.write(data)

#file.close()
print('Successfully received the file')
s.close()
print('Connection closed')