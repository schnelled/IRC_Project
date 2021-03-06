#Internet Chat Relay Utilities - Containing support function for the IRC project
#List of functions:
#   print_machine_info() - Displays the machines host name & ip address
#       information for client connection.
#
#   createSocket() - Create a default socket object that can then be used to
#       setup as a client or a server for the internet chat relay.
#
#   serverSetup(sock) - Sets up the server using a pre-created socket object.
#
#   clientSetup(sock, host) - Sets up the client for connection using a
#       pre-created socket object.
#
#   clientPrompt() - Displays the command prompt to the client.
#
#   displayConnections() - Display the socket connections connected to the
#       server for debug.
#
#   deleteConnection(client) - Remove the socket connection from the server
#       connections list.
#
#   newConnection(sockfd, addr) - Display the address and socket file descriptor
#       information for debug.

#Import needed libraries
import socket, sys, string

#Define globals for utilities module
CONNECTION_LIST = []
STATIC_ROOM = ['red', 'blue', 'yellow', 'green', 'purple', 'orange']
DEFAULT_NUMBER = 6
RECV_BUFFER = 4096
PORT = 5000
MAX_CLIENT = 10
QUIT = "<quit>"

#-------------------------------------------------------------------------------
#Function:      print_machine_info
#Input:         none
#Output:        none
#Description:   Displays the machines host name & ip address
#-------------------------------------------------------------------------------
def print_machine_info():
    # Obtain hostname and IP address
    host = socket.gethostname()
    ip = socket.gethostbyname(host)

    #Print the machine's host name and IP
    print "The host name: " + host
    print "The IP address: " + ip

#-------------------------------------------------------------------------------
#Function:      createSocket
#Input:         none
#Output:        sock - The socket created from the function
#Description:   Create a default socket object that can then be used to setup as
#               a client or a server for the internet chat relay
#-------------------------------------------------------------------------------
def createSocket():
    #Try to create a TCP socket using IPv4
    try:
        #Create a TCP socket using IPv4
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        #Display and handle the socket creation error
        print "Failed to create a socket. Error code: " + str(msg[0]) + "Error message: " + str(msg[1])
        sys.exit()

    #Successful socket creation
    print "Successful socket creation"

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #Return the created socket
    return sock

#-------------------------------------------------------------------------------
#Function:      serverSetup
#Input:         sock - The socket to be setup as a server
#Output:        sock - The setup server socket
#Description:   Sets up the server using a pre-created socket object
#-------------------------------------------------------------------------------
def serverSetup(sock):
    #Set the TCP connection to be non-blocking
    sock.setblocking(0)

    #Obtain host name of the server
    host = socket.gethostname()

    #Try to bind the host and port for communication
    try:
        #Bind the host and the port
        sock.bind((host,PORT))
    except socket.error as msg:
        #Display and handle the socket binding error
        print "Bind failed. Error code: " + str(msg[0]) + "Error message: " + str(msg[1])
        sys.exit()

    #Socket binding successful
    print "Successful socket binding"
    print_machine_info()

    #Set number of max number of connections to the server
    sock.listen(MAX_CLIENT)

    #Add the server to the connection list
    CONNECTION_LIST.append(sock)

    #Socket setup successful
    print "Internet chat relay server started on port " + str(PORT)

    #Return the setup server socket
    return sock

#-------------------------------------------------------------------------------
#Function:      clientSetup
#Input:         sock - The socket to be setup as a client
#               host -  The host the client is binding to
#Output:        sock - The client socket setup/binded to the server
#Description:   Sets up the client for connection using a pre-created socket
#               object
#-------------------------------------------------------------------------------
def clientSetup(sock, host):
     # Set the timeout for the connection to the host to 2 seconds
    sock.settimeout(2)

    # Attempt to connect to the remote host
    try:
        #Connect to the host server
        sock.connect((host, PORT))
    except:
        # Display and handle the error
        print "Unable to connect to the host"
        sys.exit()

    # Socket setup successful
    print "Connected to the remote host"
    print_machine_info()

    # Return the created and connected client socket
    return sock

#-------------------------------------------------------------------------------
#Function:      clientPrompt
#Input:         none
#Output:        none
#Description:   Displays the command prompt to the client
#-------------------------------------------------------------------------------
def clientPrompt():
    sys.stdout.write("> ")
    sys.stdout.flush()

#-------------------------------------------------------------------------------
#Function:      displayConnections
#Input:         none
#Output:        none
#Description:   Display the socket connections connected to the server for debug
#-------------------------------------------------------------------------------
def displayConnections():
    #Display the title of the message
    print "\n------------------------Connection List------------------------"
    #Loop through the connection list
    for i in range(len(CONNECTION_LIST)):
        print CONNECTION_LIST[i]

#-------------------------------------------------------------------------------
#Function:      deleteConnection
#Input:         client - The socket to be removed from the connection list
#Output:        none
#Description:   Remove the socket connection from the server connections list
#-------------------------------------------------------------------------------
def deleteConnection(client):
    #Loop through the connection list
    for i in range(len(CONNECTION_LIST)):
        currentEntry = str(CONNECTION_LIST[i])
        #Find the client in the connection list
        if str(client) in currentEntry:
            #Delete the client from the connection list
            del CONNECTION_LIST[i]
            i -= 1

#-------------------------------------------------------------------------------
#Function:      newConnection
#Input:         sockfd - The socket file descriptor created
#               addr - The socket address information
#Output:        none
#Description:   Display the address and socket file descriptor information for
#               debug
#-------------------------------------------------------------------------------
def newConnection(sockfd, addr):
    #Print connection information about the new connection to the server
    print "\n--------------------New Connection Details---------------------"
    print"|    New connection IP address: " + addr[0] + "                     |"
    print"|    Sever supplied port number: " + str(addr[1]) + "                        |"
    print"|    Socket: " + str(sockfd) + "  |"
    print "---------------------------------------------------------------\n"
