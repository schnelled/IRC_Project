#Internet Chat Relay Utilities

#Import needed libraries
import socket, select
import Utilities
from Class import Lobby, Client

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':

    #Server startup message
    print "Staring up the server"

    #Create a TCP socket using IPv4
    serverSocket = Utilities.createSocket()
    #Setup the server socket for connection
    serverSocket = Utilities.serverSetup(serverSocket)

    #Display the connection list
    Utilities.displayConnections()

    #Create an lobby instance and initail connection list
    lobby = Lobby()

    while True:
        #Handle the socket list functions during the connection
        readClients, writeClients, errorSockets =  select.select(Utilities.CONNECTION_LIST, [], [])

        #Wait for socket to read
        for client in readClients:
            #Check for new connection
            if client is serverSocket:
                #Handle the new connection
                sockfd, addr =  serverSocket.accept()
                #Create a new client instance
                newClient = Client(sockfd)
                #Add the new client to the connection list
                Utilities.CONNECTION_LIST.append(newClient)
                #Display new connection information
                Utilities.newConnection(sockfd, addr)
                #Display the connection list
                Utilities.displayConnections()
                #Send the welcome message
                lobby.lobbyWelcome(newClient)

            #Otherwise connection is from known socket
            else:
                #Receive the message
                msg = client.socket.recv(Utilities.RECV_BUFFER)

                #Check for a valid message
                if msg:
                    #Handle the received message
                    lobby.handleMsg(client, msg.decode().lower())

                else:
                    #Clean/close the socket connection
                    client.socket.close()
                    Utilities.deleteConnection(client)
                    continue

        #Wait for socket error
        for sock in errorSockets:
            #Clean/close the socket connection
            sock.close()
            Utilities.deleteConnection(sock)
