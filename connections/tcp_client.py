# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 08:07:42 2022

@author: raman
"""
import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10001)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    while True:
        # Send data, encoding string to a bite like string
        message = input("Enter message to send to server: ").encode()
        print(sys.stderr, 'sending "%s"' % message)
        sock.sendall(message)
    
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print(sys.stderr, 'received "%s"' % data)

finally:
    print(sys.stderr, 'closing socket')
    sock.close()