#!/usr/bin/python           # This is client.py file

import socket               # Import socket module
import struct

def float_to_hex(f):
    #return hex(struct.unpack('<I', struct.pack('<f', f))[0])
    return struct.pack('>f',f)
def hex_to_float(s):
    return struct.unpack('>f',s)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = '192.168.0.88'#'2A02:908:1069:6D00:89B5:7A9C:6062:E1DA'
port = 21347             # Reserve a port for your service.

s.connect((host, port));
#print (s.recv(1024).decode());

s.send(bytes(3))
#s.send(str.encode('Down'));
#setpoint = (s.recv(1024))
#setpointfloat = hex_to_float(setpoint)
#print(setpointfloat)
#print('',setpoint)
s.close                     # Close the socket when done