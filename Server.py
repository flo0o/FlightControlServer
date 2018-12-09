#!/usr/bin/python           # This is server.py file
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import socket  # Import socket module
from time import ctime
import Servomotor
import struct
import sys
import select
def float_to_hex(f):
    #return hex(struct.unpack('<I', struct.pack('<f', f))[0])
    return struct.pack('>f',f)
def hex_to_float(s):
    return struct.unpack('>f',s)
def hex_to_int(s):
    return struct.unpack('>I',s)
def int_to_hex(i):
    return struct.pack('>I',i)


Servomotor.setup()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a socket object
host = socket.gethostname() # Get local machine name 2A02:908:1069:6D00:89B5:7A9C:6062:E1DA
port = 21346  # Reserve a port for your service. Seite
port2 = 21347  # Reserve a port for your service. Höhe
port3 = 21348  # Reserve a port for your service. Speed
BUFSIZE = 1024
ctrCmd = ['Up', 'Down']
s.bind((host, port))  # Bind to the port
print('host is', host)

s2.bind((host, port2))  # Bind to the port
print('host is', host)

s3.bind((host, port3))  # Bind to the port
print('host is', host)

s.listen(5)  # Now wait for client connection.
s2.listen(5)  # Now wait for client connection.
s3.listen(5)  # Now wait for client connection.

call = 0
while True:
 #if s == true:
 #####TEst
 to_read = [s, s2, s3]
 # Get the list sockets which are readable
 readers,_,_ = select.select(to_read,[],[],0.5)
 for reader in readers:
    if reader is s:
       c, addr = s.accept()
    else:
       bla = 1;