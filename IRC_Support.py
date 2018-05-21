import socket, sys

# Declare/define constant global variables
PORT = 5000
MAX_CLIENTS = 20
BUFFER = 4096
CONNECTION_LIST = []
QUIT = '<$quit$>'

#-------------------------------------------------------------------------------
# Function:       makeSocket
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeSocket():
    # Attempt to create a socket
    try:
        # Make a TCP socket with an IPv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Socket error has occured
    except socket.error as msg:
        # Display and handle the error
        print 'Failed to create a socket. Error code: ' + str(msg[0]) + ' , Error message: ' + str(msg[1])
        sys.exit()

    # Set socket options
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Return the created socket
    return s

#-------------------------------------------------------------------------------
# Function:       makeServerSocket
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeServerSocket(s, hostName):
    # Attempt to bind the socket
    try:
        # Bind the socket
        s.bind((hostName, PORT))
    # Binding error has occured
    except socket.error as msg:
        # Display and handle the error
        print 'Bind failed. Error code: ' + str(msg[0]) + ' ,Error message: ' + str(msg[1])
        s.close()
        sys.exit()

    # Listen for a connection
    s.listen(MAX_CLIENTS)

    # Return the created socket
    return s

#-------------------------------------------------------------------------------
# Function:       makeClientSocket
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeClientSocket(s, hostName):
    # Set the timeout to 2 seconds
    s.settimeout(2)

    # Attempt to connect to the remote host
    try:
        s.connect((hostName, PORT))
    # Connection error has occured
    except:
        # Display and handle the error
        print 'Unable to connect to ' + hostName
        sys.exit()


# Define the lobby class
#-------------------------------------------------------------------------------
class Lobby:
    # Class constructor, defines initial state of the lobby class
    def __init__(self):
        # Define lists to store chat rooms and room mapping
        self.rooms = {"Red Room", "Blue Room", "Yellow Room"}
        self.whosInTheRoom = {}


# Define the room class
#-------------------------------------------------------------------------------
class Room:
    # Class constructor, defines initial state of the room class
    def __init__(self, roomName):
        # Define list of clients in specified room and the room name
        self.clients = {}
        self.roomName = roomName


# Define the client class
#-------------------------------------------------------------------------------
class Client:
    # Class constructor, defines initial state of the client class
    def __init__(self, socket, userName = "guest"):
        # Define the client socket/username and set to non-blocking TCP communication
        socket.setblocking(0)
        self.socket = socket
        self.userName = userName

    #---------------------------------------------------------------------------
    # Function:     clientPrompt
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def clientPrompt():
        # Display the command prompt to the user
        sys.sdtout.write('<' + self.userName + '> ')
        sys.stdout.flush()
