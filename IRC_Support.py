import socket   # For socket

# Declare/define constant global variables
PORT = 5000
MAX_CLIENTS = 20
CLIENT_BUFFER = 4096
CONNECTION_LIST = []

#-------------------------------------------------------------------------------
# Function:       makeSocket
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeSocket(hostName):
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
        s.bind((hostName, PORT))
    except socket.error as msg:
        # Display and handle the error
        print 'Bind failed. Error code: ' + str(msg[0]) + ' ,Error message: ' + str(msg[1])
        s.close()
        sys.exit()

    # Listen for a connection
    s.listen(MAX_CLIENTS)

    # Return the created socket
    return s


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
