import socket, sys

# Declare/define constant global variables
PORT = 5000
MAX_CLIENTS = 20
BUFFER = 4096
CONNECTION_LIST = []
QUIT = '<$quit$>'

#-------------------------------------------------------------------------------
# Function:     clientPrompt
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def clientPrompt():
    # Display the command prompt to the user
    print('<Me> ')


# Define the lobby class
#-------------------------------------------------------------------------------
class Lobby:
    # Class constructor, defines initial state of the lobby class
    def __init__(self):
        # Define lists to store chat rooms and room mapping
        self.rooms = {"Red Room", "Blue Room", "Yellow Room"}
        self.whosInTheRoom = {}

    #-----------------------------------------------------------------------
    # Function:     welcomeClient
    # Input(s):
    # Output:
    # Description:
    #-----------------------------------------------------------------------
    def welcomeClient(self, newClient):
        # Send welcome message to the client
        newClient.socket.sendall('Welcome to the lobby.\nWhat is your name:\n')


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
