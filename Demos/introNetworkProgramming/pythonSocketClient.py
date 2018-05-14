# Socket client example in python

import socket   #for sockets
import sys      #for exit

# Try to create a socket
try:
    # Create an AF_INET, STREAM socket (TCP)
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    # Display the error code
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

# Socket creation was successful
print 'Socket Created'

# Initialize the host name
host = 'www.google.com'
port = 80

# Try to obtain
try:
    remote_ip = socket.gethostbyname(host)
except socket.giaerror:
    # Could not resolve
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

# Display the host and IP address of the connection
print 'Ip address of ' + host + ' is ' + remote_ip

# Connect to remote server
clientSocket.connect((remote_ip, port))

print 'Socket Connected to ' + host + ' on ip ' + remote_ip

# Send some data to remote server
message = "GET / HTTP/1.1\r\n\r\n"

try:
    # Set the whole string
    clientSocket.sendall(message)
except socket.error:
    # Send failed
    print 'Send failed'
    sys.exit()

# Diplay that the message was successful
print 'Message send successfully'

# Now receive data
reply = clientSocket.recv(4096)

# Display the reply message
print reply
