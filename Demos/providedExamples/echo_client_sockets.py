#!/usr/bin/python
# USAGE:   echo_client_sockets.py <HOST> <PORT> <MESSAGE>
#
# EXAMPLE: echo_client_sockets.py localhost 8000 Hello
import socket
import sys

if len(sys.argv) < 4:
    print "USAGE: echo_client_sockets.py <HOST> <PORT> <MESSAGE>";
    sys.exit(0)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])
s.connect((host,port))

s.send(sys.argv[3])

i = 0
data = s.recv(10000000)
print data
print 'received', len(data), ' bytes'
s.close()
