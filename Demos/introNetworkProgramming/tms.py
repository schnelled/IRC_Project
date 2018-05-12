# Simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

# This is the TCP server
# Import the python libraries
import socket
import sys

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associate the socket with a port
host = socket.gethostname()                   # Can leave this blank on the server side
port = int(sys.argv[1])
s.bind((host, port))
print('Host name is ', host)

# Accept "call" from client
s.listen(1)
connection, addr = s.accept()
print('Client is at ', addr)

# Read stirng from client (assumed here to be so short that one call to
# revc() is enough), and make multiple copies (to show the need for the
# "while" loop on the client side)

data = connection.recv(1000000)
data = 10000 * data.decode()

# Wait for the go-ahead signal from the keyboard (show that recv() at
# the client will block until server side)
z = input()

# Now send
connection.send(data.encode())

# Close the connection
connection.close()
