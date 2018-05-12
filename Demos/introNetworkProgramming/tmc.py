# Simple illustration client/server pair; client program sends a string
# to server, which echoes it back to the client (in multiple copies),
# and the latter prints to the screen

# This is the client
# Import the python libraries
import socket
import sys

# Create a TCP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
host = sys.argv[1]          # Server address
port = int(sys.argv[2])     # Server port
s.connect((host, port))

s.send(sys.argv[3].encode())         # Send test string

# Read echo
i = 0
while True:
    data = s.recv(1000000)  # Read up to 1000000 bytes
    i += 1
    if(i < 5):
        print(data.decode())
    if not data:
        break
    print('Received', len(data), 'bytes')

# Close the connection
s.close()
