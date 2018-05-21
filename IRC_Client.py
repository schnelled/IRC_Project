import IRC_Support, sys, select

# Initialize/define local variables
message = ''

# Check that the user is attempting to use the program correctly
if len(sys.argv) < 2:
    # Display the usage message and exit
    print 'Usage: python2 IRC_Client.py <host name>'
    sys.exit()
# Otherwise create the client connection
else:
    clientSocket = IRC_Support.makeSocket()
    clientSocket = IRC_Support.makeClientSocket(clientSocket, sys.argv[1])

# Diplay successful connection to the host
print 'Connection to ' + sys.argv[1]

while True:
    # Get the list of sockets
    read_sockets, write_sockets, error_sockets = select.select([sys.stdin, clientSocket], [], [])

    # Handle a socket read
    for sock in read_sockets:

        # Check for incoming data (message)
        if sock is clientSocket:
            # Recieve the incoming data (message)
            data = sock.recv(IRC_Support.BUFFER)

            # Check for valid data
            if not data:
                # Display and handle the error
                print 'Server is not responding'
                sys.exit(1)
            # Otherwise handle the data
            else:

                # Check for quit message
                if data == IRC_Support.QUIT.encode():
                    # Display bye message and handle the quit
                    sys.stdout.write('Bye, feel free to chat another time\n')
                    sys.exit(1)
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
                    # Display the command prompt
                    IRC_Support.Client.clientPrompt()

        # Otherwise send data (message)
        else:
            # Read the client (user) data and send the encoded data
            data = message + sys.sdtin.readline()
            clientSocket.sendall(data.encode())
