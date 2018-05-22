# Helping functions and classes for the IRC

# Import needed modules
import socket

# Declare constant globals
PORT = 5000
MAX_CLIENT = 10
CONNECTION_LIST = []
BUFFER = 4096

# Instruction message
INSTRUCTIONS = 'Instructions:\n[<rooms>] to show all avaliable rooms\n'\
    + '[<join> room name] to join/switch to a room\n[<quit>] to quit\n'

#-------------------------------------------------------------------------------
# Function:
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeSocket():
    # Attempt to create a TCP socket using IPv4
    try:
        # Create a TCP socket using IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        # Diplay and handle the error
        print 'Failed to create socket. Error code: ' + str(msg[0]) + 'Error message: ' + str(msg[1])
        sys.exit()

    # Socket creation successful
    print 'Successful socket creation'

    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Return the created socket
    return s

#-------------------------------------------------------------------------------
# Function:
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeServerSocket(s):
    # Set the TCP connection to be non-blocking
    s.setblocking(0)

    # Attempt to bind the host and port number for communication
    try:
        # Bind the host and port number
        s.bind(('', PORT))
    except socket.error, msg:
        # Display and handle the error
        print 'Bind failed. Error code: ' + str(msg[0]) + 'Error message: ' + str(msg[1])
        sys.exit()

    # Socket binding successful
    print 'Successful socket binding'

    # Set the number of connections that can be listened to
    s.listen(MAX_CLIENT)

    # Append the successful socket creation to the connections list
    CONNECTION_LIST.append(s)

    # Socket setup successful
    print 'Chat server started on port ' + str(PORT)

    # Return the created server socket
    return s

#-------------------------------------------------------------------------------
# Function:
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeClientSocket(s, host):
    # Set the timeout for the connection to the host to 2 seconds
    s.settimeout(2)

    # Attempt to connect to the remote host
    try:
        #Connect to the host server
        s.connect((host, PORT))
    except:
        # Display and handle the error
        print 'Unable to connect to the host'
        sys.exit()

    # Socket setup successful
    print 'Connected to the remote host'

    # Return the created and connected client socket
    return s


# Create the lobby object - a single lobby for all to land in
class Lobby:
    # Default constructor function
    def __init__(self):
        # Set the initial state
        self.rooms = {'Red Room', 'Blue Room', 'Yellow Room'}
        self.roomMapping = {}

    #---------------------------------------------------------------------------
    # Function:
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def welcome(self, newClient):
        newClient.socket.sendall('Welcome the lobby. \nPlease tell us your name:\n')

    #---------------------------------------------------------------------------
    # Function:
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def handleMessage(self, client, message):
        # Display user name and message sent
        print client.name + " says: " + message

        # Check for name prefix
        if 'name:' in message:
            # Extract the user input name from the message
            user = message.split()[1]
            # Set the clients name to the input
            client.name = user
            # Diplay connnection with new name
            print 'New connection from: ' + client.name
            # Send the instructions to the user
            client.socket.sendall('\nHello ' + client.name + '\n' + INSTRUCTIONS)


# Create the client object - a individual ID to each connection
class Client:
    # Default constructor function
    def __init__(self, socket, name = "guest"):
        # Set the initial state
        socket.setblocking(0)
        self.socket = socket
        self.name = name
