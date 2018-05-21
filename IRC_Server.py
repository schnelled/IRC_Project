import IRC_Support, socket, select
from IRC_Support import Lobby, Room, Client

# Attempt to create a socket
try:
    # Make a TCP socket with an IPv4
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Socket error has occured
except socket.error as msg:
    # Display and handle the error
    print 'Failed to create a socket. Error code: ' + str(msg[0]) + ' , Error message: ' + str(msg[1])
    sys.exit()

# Set socket options
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Attempt to bind the socket
try:
    # Bind the socket
    serverSocket.bind(('', IRC_Support.PORT))
# Binding error has occured
except socket.error as msg:
    # Display and handle the error
    print 'Bind failed. Error code: ' + str(msg[0]) + ' ,Error message: ' + str(msg[1])
    serverSocket.close()
    sys.exit()

# Listen for a connection
serverSocket.listen(IRC_Support.MAX_CLIENTS)

# Create a lobby object
lobby = Lobby()

# Add the server to the list on live connections
IRC_Support.CONNECTION_LIST.append(serverSocket)

# Diplay server success message
print 'Chat server started on port ' + str(IRC_Support.PORT)

while True:
    # Get the list sockets to the which are ready to be read through select
    read_sockets, write_sockets, error_sockets = select.select(IRC_Support.CONNECTION_LIST,[],[])

    # Handle a socket read
    for client in read_sockets:

        # Check for a new connection
        if client == serverSocket:
            # Handle the addition on a new client connection
            clientfd, addr = serverSocket.accept()
            newClient = Client(clientfd)
            IRC_Support.CONNECTION_LIST.append(newClient)
            lobby.welcomeClient(newClient)
        # Incoming data (message) from the client
        else:
            # Recieve the incoming data (message)
            data = client.recv(IRC_Support.BUFFER)

            # Check for valid data (message) sent from client
            if data:
                # Decode, standardize, and handle the client's data (message)
                data = data.decode().lower()
                lobby.handleData(client, data)
            # Otherwise close the connection to the client
            else:
                # Handle the connection closing
                client.socket.close()
                IRC_Support.CONNECTION_LIST.remove(client)

# Close the socket
serverSocket.close()
