# Telnet program example
import socket, select, string, sys

def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':

    # Check that the program was used as designed
    if(len(sys.argv) < 3):
        # Display usage error
        print 'Usage: python2 telnet.py hostname port'
        sys.exit()

    # Obtain the host and port
    host = sys.argv[1]
    port = int(sys.argv[2])

    # Try to create a socket
    try:
        # Create an AF_INET, STREAM socket (TCP)
        clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        # Display the error code
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1]
        sys.exit()

    # Set the timeout to 2 seconds
    clientSocket.settimeout(2)

    # Connect to remote host
    try:
        # Connect to remote server
        clientSocket.connect((host, port))
    except:
        # Display the error message
        print 'Unable to connect'
        sys.exit()

    # Connection was successful
    print 'Connected to remote host. Start sending messages'
    prompt()

    while True:
        socket_list = [sys.stdin, clientSocket]

        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # Incoming message from remote server
            if sock = clientSocket:
                data = sock.recv(4096)
                if not data:
                    print '\nDisconnected from chat server'
                    sys.exit()
                else:
                    # Print data
                    sys.stdout.write(data)
                    prompt()

            # User entered a message
        else:
            msg = sys.stdin.readline()
            clientSocket.send(msg)
            prompt()
