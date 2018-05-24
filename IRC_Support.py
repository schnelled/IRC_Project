# Helping functions and classes for the IRC

# Import needed modules
import socket, string, random, sys

# Declare constant globals
PORT = 5000
MAX_CLIENT = 10
CONNECTION_LIST = []
BUFFER = 4096
BLUE = 'blue room'
RED = 'red room'
YELLOW = 'yellow room'
GREEN = 'green room'
PURPLE = 'purple room'
ORANGE = 'orange room'
QUIT = '<quit>'

# Instruction message
INSTRUCTIONS = 'Instructions:\n[#1] to show all avaliable rooms\n'\
    + '[#2 room name] to join/switch to a room\n[#3 room name] to leave a room\n[#4] to quit\n'



#-------------------------------------------------------------------------------
# Function:     makeSocket
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
# Function:         makeServerSocket
# Input(s):
# Output:
# Description:
#-------------------------------------------------------------------------------
def makeServerSocket(s):
    # Set the TCP connection to be non-blocking
    s.setblocking(0)

    # Obtain the host name and IP
    hostName = socket.gethostname()
    IP = socket.gethostbyname(hostName)

    # Attempt to bind the host and port number for communication
    try:
        # Bind the host and port number
        s.bind((hostName, PORT))
    except socket.error, msg:
        # Display and handle the error
        print 'Bind failed. Error code: ' + str(msg[0]) + 'Error message: ' + str(msg[1])
        sys.exit()

    # Socket binding successful
    print 'Successful socket binded to ' + hostName + ' at IP address ' + IP

    # Set the number of connections that can be listened to
    s.listen(MAX_CLIENT)

    # Append the successful socket creation to the connections list
    CONNECTION_LIST.append(s)

    # Socket setup successful
    print 'Chat server started on port ' + str(PORT)

    # Return the created server socket
    return s

#-------------------------------------------------------------------------------
# Function:     makeClientSocket
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
        self.rooms = [redRoom, blueRoom, yellowRoom, greenRoom, purpleRoom, orangeRoom]
        self.roomMapping = {}

    #---------------------------------------------------------------------------
    # Function:     welcome
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def welcome(self, newClient):
        # Send the welcome message to the user
        newClient.socket.sendall('Welcome the lobby. \nPlease tell us your name:\n')

    #---------------------------------------------------------------------------
    # Function:     showRooms
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def showRooms(self, client):
        # Display show rooms introduction message
        message = '\nShowing current rooms...\n'

        # Loop through the listed rooms
        i = 0
        while i < 6:
            # Concatinate the message with each avaliable room
            message += self.rooms[i].name + ' room\n'
            #Increment the value of i by 1
            i += 1

        # Send the avaliable rooms to the requesting client
        client.socket.sendall(message.encode())

    #---------------------------------------------------------------------------
    # Function:     handleMessage
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def handleMessage(self, client, message):
        # Display client's name and message sent
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

        # Check for the join a room command
        elif '#1' in message:
            # Show the rooms to the client
            self.showRooms(client)

        # Check for the list rooms command
        elif '#2' in message:
            # Check for valid input
            if len(message.split()) == 3:
                # Obtain the selected room name
                roomName = message.split()[1]

                # Check if client just entered "red room"
                if roomName == 'red':
                    # Add the client to the red room
                    self.clientToRoom(client, 0, redRoom)

                # Check if client just entered "blue room"
                if roomName == 'blue':
                    # Add the client to the blue room
                    self.clientToRoom(client, 1, blueRoom)

                # Check if client just entered "yellow room"
                if roomName == 'yellow':
                    # Add the client to the yellow room
                    self.clientToRoom(client, 2, yellowRoom)

                # Check if client just entered "green room"
                if roomName == 'green':
                    # Add the client to the green room
                    self.clientToRoom(client, 3, greenRoom)

                # Check if client just entered "purple room"
                if roomName == 'purple':
                    # Add the client to the purple room
                    self.clientToRoom(client, 4, purpleRoom)

                # Check if client just entered "orange room"
                if roomName == 'orange':
                    # Add the client to the orange room
                    self.clientToRoom(client, 5, orangeRoom)

            # Handle partial invalid usage of the command
            elif len(message.split()) == 2:
                # Check if client just entered "red"
                if 'red' in message:
                    # Add the client to the red room
                    self.clientToRoom(client, 0, redRoom)

                # Check if client just entered "blue"
                if 'blue' in message:
                    # Add the client to the blue room
                    self.clientToRoom(client, 1, blueRoom)

                # Check if client just entered "yellow"
                if 'yellow' in message:
                    # Add the client to the yellow room
                    self.clientToRoom(client, 2, yellowRoom)

                # Check if client just entered "green"
                if 'green' in message:
                    # Add the client to the green room
                    self.clientToRoom(client, 3, greenRoom)

                # Check if client just entered "purple"
                if 'purple' in message:
                    # Add the client to the purple room
                    self.clientToRoom(client, 4, purpleRoom)

                # Check if client just entered "orange"
                if 'orange' in message:
                    # Add the client to the orange room
                    self.clientToRoom(client, 5, orangeRoom)

            # Otherwise invalid usage of the command
            else:
                # Message to the client
                message = '\n\nPlease choose a valid room to enter\n'
                # Loop through the listed rooms
                i = 0
                while i < 6:
                    # Concatinate the message with each avaliable room
                    message += self.rooms[i].name + ' room\n'
                    #Increment the value of i by 1
                    i += 1

                #Concatinate the instructions to the message
                message += '\n' + INSTRUCTIONS
                # Send the intructions to the user
                client.socket.sendall(message.encode())

        # Check for the leave room command
        elif '#3' in message:
            # Check if the client is currently in a room
            if client.name in self.roomMapping:
                # Obtain the room mapping information
                infoMapping = self.roomMapping[client.name]
                # Obtain the room the client is leaving
                leaving = message.split()[1]

                # Check if the client is leaving the red room
                if leaving == 'red':
                    # Leave the red room
                    self.clientOutRoom(client, 0)
                    message = '\n\nYou left the red room\n'

                # Check if the client is leaving the blue room
                if leaving == 'blue':
                    # Leave the blue room
                    self.clientOutRoom(client, 1)
                    message = '\n\nYou left the blue room\n'

                # Check if the client is leaving the yellow room
                if leaving == 'yellow':
                    # Leave the yellow room
                    self.clientOutRoom(client, 2)
                    message = '\n\nYou left the yellow room\n'

                # Check if the client is leaving the green room
                if leaving == 'green':
                    # Leave the green room
                    self.clientOutRoom(client, 3)
                    message = '\n\nYou left the green room\n'

                # Check if the client is leaving the purple room
                if leaving == 'purple':
                    # Leave the purple room
                    self.clientOutRoom(client, 4)
                    message = '\n\nYou left the purple room\n'

                # Check if the client is leaving the orange room
                if leaving == 'orange':
                    # Leave the orange room
                    self.clientOutRoom(client, 5)
                    message = '\n\nYou left the orange room\n'

                # Create instruction message
                message += INSTRUCTIONS
                # Send intructions to the client
                client.socket.sendall(message.encode())

            # Otherwise invalid usage of the command
            else:
                # Create invalid input message (client not in room) to sent back to client, with instructions
                message = '\n\nYour not currently in a room. Please select one of the following instructions.\n'
                message += INSTRUCTIONS
                # Send the invalid user input message screen back
                client.socket.sendall(message.encode())

        # Check for the quit command
        elif '#4' in message:
            # Send the quit message back to the client
            client.socket.sendall(QUIT.encode())
            # Remove the client from there room
            self.removeClient(client)

        # Otherwise check if the client is currently in a room
        else:
            # Check if the client is currently in a room
            if client.name in self.roomMapping:
                # Obtain the room mapping information
                infoMapping = self.roomMapping[client.name]

                # Check if the client is in the red room
                if 'red' in infoMapping.name:
                    # Boardcast the message to the red room only
                    self.rooms[0].broadcastRoom(client, message.encode())

                # Check if the client is in the blue room
                if 'blue' in infoMapping.name:
                    # Broadcast the message to the blue room only
                    self.rooms[1].broadcastRoom(client, message.encode())

                # Check if the client is in the yellow room
                if 'yellow' in infoMapping.name:
                    # Broadcast the message to the yellow room only
                    self.rooms[2].broadcastRoom(client, message.encode())

                # Check if the client is in the green room
                if 'green' in infoMapping.name:
                    # Broadcast the message to the green room only
                    self.rooms[3].broadcastRoom(client, message.encode())

                # Check if the client is in the purple room
                if 'purple' in infoMapping.name:
                    # Broadcast the message to the purple room only
                    self.rooms[4].broadcastRoom(client, message.encode())

                # Check if the client is in the orange room
                if 'orange' in infoMapping.name:
                    # Broadcast the message to the orange room only
                    self.rooms[5].broadcastRoom(client, message.encode())

            # Otherwise user input invalid command
            else:
                # Create invalid input message to sent back to client, with instructions
                message = '\n\nInvalid user input. Please select one of the following instructions.\n\n'
                message += INSTRUCTIONS
                # Send the invalid user input message screen back
                client.socket.sendall(message.encode())

    #---------------------------------------------------------------------------
    # Function:     removeClient
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def removeClient(self, client):
        # Check if the client is currently in a room
        if client.name in self.roomMapping:
            # Obtain the room mapping information
            infoMapping = self.roomMapping[client.name]

            # Check if the client is in the red room
            if 'red' in infoMapping.name:
                # Remove the client from the red room
                self.clientOutRoom(client, 0)

            # Check if the client is in the blue room
            if 'blue' in infoMapping.name:
                # Remove the client from the blue room
                self.clientOutRoom(client, 1)

            # Check if the client is in the yellow room
            if 'yellow' in infoMapping.name:
                # Remove the client from the yellow room
                self.clientOutRoom(client, 2)

            # Check if the client is in the green room
            if 'green' in infoMapping.name:
                # Remove the client from the green room
                self.clientOutRoom(client, 3)

            # Check if the client is in the purple room
            if 'purple' in infoMapping.name:
                # Remove the client from the purple room
                self.clientOutRoom(client, 4)

            # Check if the client is in the orange room
            if 'orange' in infoMapping.name:
                # Remove the client from the orange room
                self.clientOutRoom(client, 5)

        # Otherwise the client is in the lobby, so display bye message
        print 'Client: ' + client.name + ' has left the server\n'

    #---------------------------------------------------------------------------
    # Function:     clientToRoom
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def clientToRoom(self, client, roomIndex, roomClass):
        # Add the client to the selected room
        self.rooms[roomIndex].clients.append(client)
        # Welcome the client to the selected room
        self.rooms[roomIndex].welcome(client)
        # Add the client to the room mapping
        self.roomMapping[client.name] = roomClass

    #---------------------------------------------------------------------------
    # Function:     clientOutRoom
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def clientOutRoom(self, client, roomIndex):
        # Remove the client from the red room
        self.rooms[roomIndex].removeClient(client)
        # Delete the client from the room mapping set
        del self.roomMapping[client.name]


# Create the room object - a room to enter from the lobby that contains clients
class Room:
    # Defualt constructor function
    def __init__(self, name):
        # Set the initial state
        self.clients = []
        self.name = name

    #---------------------------------------------------------------------------
    # Function:     welcome
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def welcome(self, client):
        # Create a random number generator with bounds between 1-3
        select = random.randint(1,3)

        # Check if the selected welcome message is the first message
        if select == 1:
            message = 'It\'s a bird, it\'s a plane, no it\'s ' + client.name + ' flying into the ' + self.name + ' room.\n'
        # Check if the selected welcome message is the seconde message
        elif select == 2:
            message = client.name + ' hopped into the ' + self.name + ' room. Kangaroo!\n'
        # Otherwise the selected welcome message is the third message
        else:
            message = client.name + ' has arrived into the ' + self.name + ' room. Party\'s over.\n'

        # Loop through all of the clients in the room
        for client in self.clients:
            # Send the message to clients in the room
            client.socket.sendall(message.encode())

    #---------------------------------------------------------------------------
    # Function:     boardcastRoom
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def broadcastRoom(self, client, message):
        # Create the message to be broadcast
        message = client.name.encode() + ': ' + message
        # Loop through all of the clients in the room
        for client in self.clients:
            client.socket.sendall(message)


    #---------------------------------------------------------------------------
    # Function:     removeClient
    # Input(s):
    # Output:
    # Description:
    #---------------------------------------------------------------------------
    def removeClient(self, client):
        # Remove the client from the rooms list of clients
        self.clients.remove(client)
        # Create the rooms client left message
        message = client.name.encode() + ' has left the ' + self.name + ' room.\n'
        # Broadcast the message to the room
        self.broadcastRoom(client, message)


# Create the avaliable rooms
redRoom = Room(RED.split()[0])
blueRoom = Room(BLUE.split()[0])
yellowRoom = Room(YELLOW.split()[0])
greenRoom = Room(GREEN.split()[0])
purpleRoom = Room(PURPLE.split()[0])
orangeRoom = Room(ORANGE.split()[0])


# Create the client object - a individual ID to each connection
class Client:
    # Default constructor function
    def __init__(self, socket, name = "guest"):
        # Set the initial state
        socket.setblocking(0)
        self.socket = socket
        self.name = name
