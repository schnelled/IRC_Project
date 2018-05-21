import IRC_Support, select
from IRC_Support import Lobby, Room, Client

# Create the server socket
serverSocket = IRC_Support.makeSocket('')

# Create a lobby object
lobby = Lobby()

# Add the server to the list on live connections
IRC_Support.CONNECTION_LIST.append(serverSocket)

# Diplay server success message
print 'Chat server started on port ' + str(IRC_Support.PORT)

while True:
    # Get the list sockets to the which are ready to be read through select
    read_sockets, write_sockets, error_sockets = select.select(IRC_Support.CONNECTION_LIST,[],[])

    # Loop through the clients currently reading from the server
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
            data = client.recv(IRC_Support.CLIENT_BUFFER)

            # Check for valid data (message) sent from client
            if data:
                # Decode and standardize the client's data (message)
                data = data.decode().lower()

                # Handle the client data (message)
                lobby.handleData(client, data)

            # Otherwise close the connection to the client
            else:
                # Handle the connection closing
                client.socket.close()
                IRC_Support.CONNECTION_LIST.remove(client)

# Close the socket
serverSocket.close()
