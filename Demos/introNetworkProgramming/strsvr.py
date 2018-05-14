# strsvr.py: simple illustration of nonblocking sockets

# Multiple clients connect to server; each client repeatedly sends a letter
# letter k, which the server adds to a global string v and echos back to the
# client; k = '' means the client is dropping out; when all clients are gone,
# server prints file value of v

# This is the server; usage is
#   pyhon strsvr.py server_port_number

import socket, sys

# Set up the listening socket
lstn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Initialize the port number
port = int(sys.argv[1])

# Bind lstn socket to this port
lstn.bind(('',port))
lstn.listen(5)

# Initialize total, v
v = ''

# Initialize client socket list
cs = []

# In this example, a fixed number of clients
nc = 2

# Accept connections from the clietns
for i in range(nc):
    (clnt,ap) = lstn.accept()

    # Diplay the connection information
    print "Client is at ", ap


    # Set this new socket to nonblocking mode
    clnt.setblocking(0)
    cs.append(clnt)

# Now loop, always accepting input from whoever is ready, if any, until
# no clients are left
while (len(cs) > 0):
    # Get next client, with effect of a circular queue
    clnt = cs.pop(0)
    cs.append(clnt)

    # Can read from clnt? clnt closed connection?
    try:
        k = clnt.recv(1)
        if k == '':
            clnt.close()
            cs.remove(clnt)
        v += k
        clnt.send(v)
        print "Sending: ", v
    except:
        pass

# CLose the socket
lstn.close()

# Display the final value
print "The final value of v is: ", v
