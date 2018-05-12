# strclnt.py: Simple illustration of nonblocking socket

# Two client connect to server; each client repeatedly send a letter k,
# which the server appends to a global string v and reports it to the
# client; k = '' means the client is dropping out; when all clients are
# gone, server prints the final string v

# This is the client; usage is
#   python strclnt.py server_address server_port

import socket, sys

# Create a TCP socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 # Initialize the host name and port
 host = sys.arg[1]                  # Server address
 port = int(sys.arg[2])             # Server port

 # Create a TCP connection
 clientSocket.connect((host, port))

 while True:
     # Obtain the letter
     k = raw_input('enter a letter')
     clientSocket.send(k)           # Send k to the server

     # if stop signal, then leave loop
     if k == '':
         break

    # Recieve v from server (up to 1024 bytes)
    v = clientSocket.recv(1024)

    # Display the letter
    print v

#Close the socket
clientSocket.close()
