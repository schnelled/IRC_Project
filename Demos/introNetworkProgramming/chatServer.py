# TCP chat server

# Import needed modules
import socket   # For sockets
import select   # For select

# Function to broadcast messages to all connected clients
def broadcast_data(sock, message):
    # Broadcast the message to the connected clients
    for socket in CONNECTION_LIST:
        # Don't send to server or client supplying the message
        if socket != serverSocket and socket != sock:
            # Try to send the message
            try:
                socket.send(message)
            except:
                # Broken socket connection error
                socket.close()
                CONNECTION_LIST.remove(socket)

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':

    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    RECV_BUFFER = 4096
    PORT = 5000

    # Try to create a socket
    try:
        # Create an AF_INET, STREAM socket (TCP)
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        # Display the error code
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit()

    # Socket creation was successful
    print 'Socket created'

    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Try to bind the host and port socket
    try:
        serverSocket.bind(('0.0.0.0', PORT))
    except socket.error, msg:
        # Display binding error
        print 'Bind failed. Error Code : ' + str(msg[0]) + 'Message ' + msg[1]

    # Display bind was successful
    print 'Socket bind complete'

    # Listen for a connection
    serverSocket.listen(10)
    # Display the server is listening for connections
    print 'Socket now listening'

    #Add server socket to the list of readable connections
    CONNECTION_LIST.append(serverSocket)

    print 'Chat server started on port ' + str(PORT)

    while True:
        # Get the list sockets to the which are ready to be read through select
        read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST,[],[])

        for sock in read_sockets:
            # Check for new connection
            if sock == serverSocket:
                # Handle the new connection
                sockfd, addr = serverSocket.accept()
                # Display client information
                print 'Connected with ' + addr[0] + ':' + str(addr[1])

                # Append the connection to the list of current connections
                CONNECTION_LIST.append(sockfd)
                print 'Client (%s, %s) connected' %addr

                # Broadcast that a client has enter the room
                broadcast_data(sockfd, "[%s:%s] entered room\n" %addr)

            # Some incoming message from client
            else:
                # Try to received data from client
                try:
                    # Recieve the data
                    data = sock.recv(RECV_BUFFER)
                    # Check if valid data
                    if data:
                        # Broadcast the message
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '>' + data)
                except:
                    # Broadcast and display that the client is offline
                    broadcast_data(sock, "Client (%s, %s) is offline" %addr)
                    print "Client (%s, %s) is offline" % addr

                    # Close the socket
                    sock.close()

                    # Remove the connection form the connection list
                    CONNECTION_LIST.remove(sock)
                    continue

    #Close the socket
    serverSocket.close()
