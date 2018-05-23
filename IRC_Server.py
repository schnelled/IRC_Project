# TCP Chat Server

# Import needed modules
import socket, sys, select, string
import IRC_Support
from IRC_Support import Lobby, Client

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':

    # Dislay server startup message
    print 'Starting up the server'

    # Create a TCP socket using IPv4
    serverSocket = IRC_Support.makeSocket()
    # Create and bind server socket
    serverSocket = IRC_Support.makeServerSocket(serverSocket)

    # Create a new instance of the lobby
    lobby = Lobby()

    while True:

        # Handle the socket list functions during connection
        read_clients, write_clients, error_sockets = select.select(IRC_Support.CONNECTION_LIST, [], [])

        # Wait for client wanting to read
        for client in read_clients:

            # Check for a new connection
            if client is serverSocket:
                # Handle the new connection
                clientfd, addr = serverSocket.accept()
                # Create a new instance of client
                newClient = Client(clientfd)
                # Append the new client to the connection list
                IRC_Support.CONNECTION_LIST.append(newClient.socket)
                # Display client connection information
                print 'Client (%s, %s) connected' %addr
                # Welcome the new client
                lobby.welcome(newClient)

            # Otherwise handle the new message
            else:
                # Recieve the message from the client
                message = newClient.socket.recv(IRC_Support.BUFFER)

                # Check for valid message
                if message:
                    # Decode and standardize the message
                    message = message.decode().lower()
                    # Handle the client message
                    lobby.handleMessage(newClient, message)

                # Otherwise kill the client
                else:
                    # Close the client socket
                    newClient.socket.close()
                    # Remove client from connection list
                    IRC_Support.CONNECTION_LIST.remove(client)

        #Wait for socket error
        for sock in error_sockets:
            # Close the socket
            sock.close()
            # Remove socket from connection list
            IRC_Support.CONNECTION_LIST(client)
