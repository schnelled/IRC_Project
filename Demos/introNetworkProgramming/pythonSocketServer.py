# Socket server example in python

import socket   #for sockets
import sys      #for exit

HOST = ''       #symbolic name meaning all available interfaces
PORT = 8888     #arbitrary non-privileged port

# Try to create a socket
try:
    # Create an AF_INET, STREAM socket (TCP)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    # Display the error code
    print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
    sys.exit()

# Socket creation was successful
print 'Socket Created'

# Try to bind the host and port socket
try:
    serverSocket.bind((HOST, PORT))
except socket.error, msg:
    # Display binding error
    print 'Bind failed. Error Code : ' + str(msg[0]) + 'Message ' + msg[1]

# Display bind was successful
print 'Socket bind complete'

# Listen for a connection
serverSocket.listen(10)
# Display the server is listening for connections
print 'Socket now listening'

# Keep talking with the client connection
while True:
    # Wait to accept a connection - blocking call
    conn, addr = serverSocket.accept()
    # Display client information
    print 'Connected with ' + addr[0] + ':' + str(addr[1])

    # Receive data from the client
    data = conn.recv(1024)
    reply = 'OK...' + data

    # Make sure the data isn't NULL
    if not data:
        break

    # Reply to the client
    conn.sendall(reply)

conn.close()
serverSocket.close()
