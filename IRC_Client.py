import IRC_Support, sys, select, socket

# Initialize/define local variables
message = ''

# Check that the user is attempting to use the program correctly
if len(sys.argv) < 2:
    # Display the usage message and exit
    print 'Usage: python2 IRC_Client.py <host name>'
    sys.exit()
# Otherwise create the client connection
else:
    # Attempt to create a socket
    try:
        # Make a TCP socket with an IPv4
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Socket error has occured
    except socket.error as msg:
        # Display and handle the error
        print 'Failed to create a socket. Error code: ' + str(msg[0]) + ' , Error message: ' + str(msg[1])
        sys.exit()

    # Set socket options
    clientSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Set the timeout to 2 seconds
    clientSocket.settimeout(2)

    # Attempt to connect to the remote host
    try:
        clientSocket.connect((sys.argv[1], IRC_Support.PORT))
    # Connection error has occured
    except:
        # Display and handle the error
        print 'Unable to connect to ' + sys.argv[1]
        sys.exit()

# Diplay successful connection to the host
print 'Connection to ' + sys.argv[1]

# Create list for the socket
socketList = [sys.stdin, clientSocket]

while True:
    # Get the list of sockets
    read_sockets, write_sockets, error_sockets = select.select(socketList, [], [])

    # Handle a socket read
    for sock in read_sockets:

        # Check for incoming data (message)
        if sock is clientSocket:
            # Recieve the incoming data (message)
            data = sock.recv(IRC_Support.BUFFER)

            # Check for valid data
            #if not data:
                # Display and handle the error
                #print '\nDisconnected from chat server'
                #sys.exit()
            # Otherwise handle the data
            #else:

            # Check for quit message
            if data == IRC_Support.QUIT.encode():
                # Display bye message and handle the quit
                sys.stdout.write('Bye, feel free to chat another time\n')
                sys.exit()
            # Otherwise write the message to standard output
            else:
                # Write the message to standard output
                sys.stdout.write(data.decode())

                # Check if the client has given his name
                if 'What is your name' in data.decode():
                    # Handle the message format
                    message = 'Name: '
                # Otherwise set message format to default
                else:
                    message = ''

        # Otherwise send data (message)
        else:
            # Read the client (user) data and send the encoded data
            data = message + sys.stdin.readline()
            clientSocket.send(data.encode())
            IRC_Support.clientPrompt()
