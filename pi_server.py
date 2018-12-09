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
    to_read = [s, s2, s3]
    # Get the list sockets which are readable
    readers, _, _ = select.select(to_read, [], [], 0.5)
    for reader in readers:
        if reader is s:

            c, addr = s.accept()  # Establish connection with client.
            print('Got connection from', addr)


            try:
                #while True:
                datapoint = -1
                datapoint = c.recv(1024)

                data = ''
                data = datapoint.decode()
                if not data:
                    break
                if data == ctrCmd[0]:
                    Servomotor.ServoUp()
                    print('Increase: ', Servomotor.cur_X)
                    sendx = Servomotor.cur_X
                    sendxstrg = float_to_hex(sendx)
                    c.send(sendxstrg)

                if data == ctrCmd[1]:
                    Servomotor.ServoDown()
                    print('Decrease: ', Servomotor.cur_X)
                    sendx = Servomotor.cur_X
                    sendxstrg = float_to_hex(sendx)
                    c.send(sendxstrg)

                if (type(datapoint) == bytes and ((data == ctrCmd[1]) == False) and  ((data == ctrCmd[0]) == False)):
                    setpoint = hex_to_int(datapoint)

                    x = np.arange(0, 100, 50)
                    y = np.arange(Servomotor.servo_min, Servomotor.servo_max, (Servomotor.servo_max - Servomotor.servo_min) / 2)
                    f = interpolate.interp1d(x, y, fill_value='extrapolate')
                    setpointfinal = f(setpoint)  # use interpolation function returned by `interp1d`

                    Servomotor.ServoSetpoint(setpointfinal)
                    print('Decrease: ', Servomotor.cur_X)
                    sendx = Servomotor.cur_X
                    sendxstrg = float_to_hex(sendx)
                    c.sendall(sendxstrg)
                    call = call + 1
                    if call > 100:
                        call = 0
                    #c.sendall(int_to_hex(call))
            except KeyboardInterrupt:
                Servomotor.close()
                print('Stop: ', Servomotor.cur_X)
                c.send(Servomotor.cur_X)
                c.close()  # Close the connection

        if reader is s2:

            c2, addr = s2.accept()  # Establish connection with client.
            print('Got connection from', addr)
            try:
                    datapoint2 = 0
                    datapoint2 = c2.recv(1024)
                    data2 = ''
                    data2 = datapoint2.decode()

                    if data2 == ctrCmd[0]:
                        Servomotor.ServoUp()
                        print('Increase: ', Servomotor.cur_X2)
                        sendx2 = Servomotor.cur_X2
                        sendxstrg2 = float_to_hex(sendx2)
                        c2.send(sendxstrg2)

                    if data2 == ctrCmd[1]:
                        Servomotor.ServoDown()
                        print('Decrease: ', Servomotor.cur_X2)
                        sendx2 = Servomotor.cur_X2
                        sendxstrg2 = float_to_hex(sendx2)
                        c2.send(sendxstrg2)


                    if (type(datapoint2) == bytes ):
                        setpoint2 = hex_to_int(datapoint2)

                        x2 = np.arange(0, 100, 50)
                        y2 = np.arange(Servomotor.servo_min2, Servomotor.servo_max2,
                                  (Servomotor.servo_max2 - Servomotor.servo_min2) / 2)
                        f2 = interpolate.interp1d(x2, y2, fill_value='extrapolate')
                        setpointfinal2 = f2(setpoint2)  # use interpolation function returned by `interp1d`

                        Servomotor.ServoSetpoint2(setpointfinal2)
                        print('Decrease: ', Servomotor.cur_X2)
                        sendx2 = Servomotor.cur_X2
                        sendxstrg2 = float_to_hex(sendx2)
                        c2.sendall(sendxstrg2)
            except KeyboardInterrupt:
                    Servomotor.close()

                    print('Stop: ', Servomotor.cur_X2)
                    c2.send(Servomotor.cur_X2)
                    c2.close()  # Close the connection

        if reader is s3:

            c3, addr = s3.accept()  # Establish connection with client.
            print('Got connection from', addr)
            # c.send(str.encode('Thank you for connecting'))
            try:
                    datapoint3 = 0
                    datapoint3 = c3.recv(1024)
                    if (type(datapoint3) == bytes ):
                        setpoint3 = hex_to_int(datapoint3)

                        x3 = np.arange(0, 100, 50)
                        y3 = np.arange(Servomotor.servo_min3, Servomotor.servo_max3,
                                  (Servomotor.servo_max3 - Servomotor.servo_min3) / 2)
                        f3 = interpolate.interp1d(x3, y3, fill_value='extrapolate')
                        setpointfinal3 = f3(setpoint3)  # use interpolation function returned by `interp1d`

                        Servomotor.ServoSetpoint3(setpointfinal3)
                        print('Decrease: ', Servomotor.cur_X3)
                        sendx3 = Servomotor.cur_X3
                        sendxstrg3 = float_to_hex(sendx3)
                        c3.sendall(sendxstrg3)
            except KeyboardInterrupt:
                Servomotor.close()
                print('Stop: ', Servomotor.cur_X3)
                c3.send(Servomotor.cur_X3)
                c3.close()  # Close the connection
