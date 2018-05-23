# TCP Chat Client

# Import needed modules
import sys, socket, select
import IRC_Support
from IRC_Support import Client

#-------------------------------------------------------------------------------
# Function:
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def prompt():
        sys.stdout.write('> ')
        sys.stdout.flush()

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':

    # Dislay server startup message
    print 'Starting up the server'

    # Check that the user is using the program correctly
    if(len(sys.argv) < 2):
        # Display and handle the error
        print 'Usage: python2 IRC_Client [hostname]'
        sys.exit()

    # Declare local variables
    prefix = ''

    # Create a TCP socket using IPv4
    clientSocket = IRC_Support.makeSocket()
    # Create and connect client socket
    clientSocket = IRC_Support.makeClientSocket(clientSocket, sys.argv[1])

    # Create entry for the connection list
    connectionList = [sys.stdin, clientSocket]

    while True:

        # Handle the socket list functions during connection
        read_sockets, write_sockets, error_sockets = select.select(connectionList, [], [])

        # Wait for sockets wanting to read
        for sock in read_sockets:

            # Check for incoming message
            if sock is clientSocket:
                # Recieve the message
                message = sock.recv(IRC_Support.BUFFER)

                # Check for valid message
                if not message:
                    # Display and handle the error
                    print '\nDisconnected from chat server'
                    sys.exit()

                # Otherwise the message is valid
                else:

                    # Check for quit message
                    if message == IRC_Support.QUIT.encode():
                        # Say goodbye to the client and exit
                        sys.stdout.write('\nGoodbye, chat with you later\n')
                        sys.exit()

                    # Otherwise handle the greating or normal message states
                    else:
                        # Display the message
                        sys.stdout.write(message)

                        # Check if client just entered the lobby
                        if 'Please tell us your name' in message.decode():
                            # Change the value of the defualt prefix
                            prefix = 'name: '
                        # Otherwise the client isn't just entering the lobby
                        else:
                            # Defualt value of prefix
                            prefix = ''

                # Display the command prompt
                prompt()

            #Otherwise user is sending a message
            else:
                # Comminticate the message
                message = prefix + sys.stdin.readline()
                # Send the message to the server
                clientSocket.sendall(message)
