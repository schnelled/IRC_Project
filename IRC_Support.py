import socket   # For socket

# Declare/define constant global variables
PORT = 5000
MAX_CLIENTS = 20

#---------------------------------------------------------------------------
# Function:       makeSocket
# Input(s):
# Output:
# Description:
#---------------------------------------------------------------------------
def makeSocket(addr):

    # Attempt to create a socket
    try:
        # Make a TCP socket with an IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as msg:
        # Display and handle the error
        print 'Failed to create a socket. Error code: ' + str(msg[0]) + ' , Error message: ' + str(msg[1])
        sys.exit()

    # Set socket options
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Attempt to bind the socket
    try:
        # Bind the socket
        s.bind(('', PORT))
    except socket.error as msg:
        # Display and handle the error
        print 'Bind failed. Error code: ' + str(msg[0]) + ' ,Error message: ' + str(msg[1])
        s.close()
        sys.exit()

    # Listen for a connection
    s.listen(MAX_CLIENTS)

    # Display the successful socket creation message
    print 'Now listening at ' + str(addr)

    # Return the created socket
    return s
