#Import needed libraries
import socket, string, random
import Utilities

#----------------------------------Lobby CLASS----------------------------------
class Lobby:
    #Class constructor
    def __init__(self):
        self.staticRooms = [redRoom, blueRoom, yellowRoom, greenRoom, purpleRoom, orangeRoom]
        self.staticRoomMap = {}   #{client name: room map}
        self.dynamicRooms = {}    #{room name: Room(class)}
        self.dynamicRoomMap = {}  #{client name: room map}

    #---------------------------------------------------------------------------
    #Function:      lobbyWelcome
    #Input:         self -
    #               newClient -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def lobbyWelcome(self, newClient):
        #Send a welcome message to the new client
        newClient.socket.sendall("Welcome to the party!\nPlease tell us your name:\n")

    #---------------------------------------------------------------------------
    #Function:      handleMsg
    #Input:         self -
    #               client -
    #               msg -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def handleMsg(self, client, msg):
        #Display what the client transmitted
        print "\n--------------------New Message from Client--------------------"
        print client.name + " sent: " + msg

        #Obtain the splash screen
        intro = self.splashScreen()

        # Check for name prefix
        if 'name:' in msg:
            # Extract the user input name from the message
            user = msg.split()[1]
            # Set the clients name to the input
            client.name = user
            # Diplay connnection with new name
            print "New connection from: " + client.name
            # Send the instructions to the user
            client.socket.sendall("\nHello " + client.name + "\n" + intro)


        #Check for the join a room command
        elif '1' in msg:
             # Show the rooms to the client
             self.showRooms(client)

        #Check for the list rooms command
        elif '2' in msg:
            # Check for valid input
            if len(msg.split()) == 3:
                # Obtain the selected room name
                roomName = msg.split()[1]

                # Check if client just entered "red room"
                if roomName == 'red':
                    # Add the client to the red room
                    self.clientStaticRoom(client, 0, redRoom)

                # Check if client just entered "blue room"
                elif roomName == 'blue':
                    # Add the client to the blue room
                    self.clientStaticRoom(client, 1, blueRoom)

                # Check if client just entered "yellow room"
                elif roomName == 'yellow':
                    # Add the client to the yellow room
                    self.clientStaticRoom(client, 2, yellowRoom)

                # Check if client just entered "green room"
                elif roomName == 'green':
                    # Add the client to the green room
                    self.clientStaticRoom(client, 3, greenRoom)

                # Check if client just entered "purple room"
                elif roomName == 'purple':
                    # Add the client to the purple room
                    self.clientStaticRoom(client, 4, purpleRoom)

                # Check if client just entered "orange room"
                elif roomName == 'orange':
                    # Add the client to the orange room
                    self.clientStaticRoom(client, 5, orangeRoom)

                # Otherwise invalid room name was chosen
                else:
                    # Send message to client to choose a valid room
                    self.invalidRoom(client)

            # Handle partial invalid usage of the command
            elif len(msg.split()) == 2:
                # Check if client just entered "red"
                if 'red' in msg:
                    # Add the client to the red room
                    self.clientStaticRoom(client, 0, redRoom)

                # Check if client just entered "blue"
                elif 'blue' in msg:
                    # Add the client to the blue room
                    self.clientStaticRoom(client, 1, blueRoom)

                # Check if client just entered "yellow"
                elif 'yellow' in msg:
                    # Add the client to the yellow room
                    self.clientStaticRoom(client, 2, yellowRoom)

                # Check if client just entered "green"
                elif 'green' in msg:
                    # Add the client to the green room
                    self.clientStaticRoom(client, 3, greenRoom)

                # Check if client just entered "purple"
                elif 'purple' in msg:
                    # Add the client to the purple room
                    self.clientStaticRoom(client, 4, purpleRoom)

                # Check if client just entered "orange"
                elif 'orange' in msg:
                    # Add the client to the orange room
                    self.clientStaticRoom(client, 5, orangeRoom)

                # Otherwise invalid room name was chosen
                else:
                    # Send message to client to choose a valid room
                    self.invalidRoom(client)

            # Otherwise invalid usage of the command
            else:
                # Send message to client to choose a valid room
                self.invalidRoom(client)

        #Check for the leave a room command
        elif '3' in msg:
            # Check if the client is currently in a room
            if client.name in self.staticRoomMap:
                # Obtain the room mapping information
                infoMapping = self.staticRoomMap[client.name]
                # Obtain the room the client is leaving
                leaving = msg.split()[1]

                # Check if the client is leaving the red room
                if leaving == 'red':
                    # Leave the red room
                    self.leaveStaticRoom(client, 0)
                    msg = '\nYou left the red room\n'

                # Check if the client is leaving the blue room
                elif leaving == 'blue':
                    # Leave the blue room
                    self.leaveStaticRoom(client, 1)
                    msg = '\nYou left the blue room\n'

                # Check if the client is leaving the yellow room
                elif leaving == 'yellow':
                    # Leave the yellow room
                    self.leaveStaticRoom(client, 2)
                    msg = '\nYou left the yellow room\n'

                # Check if the client is leaving the green room
                elif leaving == 'green':
                    # Leave the green room
                    self.leaveStaticRoom(client, 3)
                    msg = '\nYou left the green room\n'

                # Check if the client is leaving the purple room
                elif leaving == 'purple':
                    # Leave the purple room
                    self.leaveStaticRoom(client, 4)
                    msg = '\nYou left the purple room\n'

                # Check if the client is leaving the orange room
                elif leaving == 'orange':
                    # Leave the orange room
                    self.leaveStaticRoom(client, 5)
                    msg = '\nYou left the orange room\n'

                # Otherwise invalid room choosen
                else:
                    # Invalid choice message
                    msg = '\nThat room doesn\'t exist\n'

                # Create instruction message
                msg += self.splashScreen()
                # Send intructions to the client
                client.socket.sendall(msg)

            # Otherwise invalid usage of the command
            else:
                #Create invalid input message to sent back to client, with instructions
                msg = "\nInvalid user input. Please select one of the following instructions.\n"
                msg += self.splashScreen()
                # Send the invalid user input message screen back
                client.socket.sendall(msg)

        #Check for the quit command
        elif '4' in msg:
            # Send the quit message back to the client
            client.socket.sendall(Utilities.QUIT)
            # Remove the client from there room
            self.removeClient(client)

        #Otherwise the receive message was invalid
        else:
            # Check if the client is currently in a room
            if client.name in self.staticRoomMap:
                # Obtain the room mapping information
                infoMapping = self.staticRoomMap[client.name]

                # Check if the client is in the red room
                if 'red' in infoMapping.name:
                    # Boardcast the message to the red room only
                    self.staticRooms[0].broadcastRoom(client, msg)

                # Check if the client is in the blue room
                if 'blue' in infoMapping.name:
                    # Broadcast the message to the blue room only
                    self.staticRooms[1].broadcastRoom(client, msg)

                # Check if the client is in the yellow room
                if 'yellow' in infoMapping.name:
                    # Broadcast the message to the yellow room only
                    self.staticRooms[2].broadcastRoom(client, msg)

                # Check if the client is in the green room
                if 'green' in infoMapping.name:
                    # Broadcast the message to the green room only
                    self.staticRooms[3].broadcastRoom(client, msg)

                # Check if the client is in the purple room
                if 'purple' in infoMapping.name:
                    # Broadcast the message to the purple room only
                    self.staticRooms[4].broadcastRoom(client, msg)

                # Check if the client is in the orange room
                if 'orange' in infoMapping.name:
                    # Broadcast the message to the orange room only
                    self.staticRooms[5].broadcastRoom(client, msg)

            # Otherwise user input invalid command
            else:
                # Create invalid input message to sent back to client, with instructions
                msg = "\nInvalid user input. Please select one of the following instructions.\n"
                msg += self.splashScreen()
                # Send the invalid user input message screen back
                client.socket.sendall(msg)


    #---------------------------------------------------------------------------
    #Function:      splashScreen
    #Input:         self -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def splashScreen(self):
        msg = """------------------------Instructions-------------------------
|                 ______  ______  ______                    |
|                |__  __||  __  ||  ____|                   |
|                   | |  |  |_| ||  |                       |
|                   | |  |     _||  |                       |
|                 __| |_ | |\  \ |  |___                    |
|                |______||_| \__\|______|                   |
|                                                           |
|___________________________________________________________|
|    Welcome to the sever!                                  |
|                                                           |
|    1. To show all avaliable rooms                         |
|    2. [room name] to join a room                          |
|    3. [room name] to leave a room                         |
|    4. To quit & leave the server                          |
|___________________________________________________________|""" + "\n"

        #Return the instruction menu
        return msg

    #---------------------------------------------------------------------------
    #Function:      showRooms
    #Input:         self -
    #               client -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def showRooms(self, client):
        # Display show rooms introduction message
        msg = "--------------------Current Static Rooms--------------------\n"

        #Loop through the static room
        for i in range(Utilities.DEFAULT_NUMBER):
            msg += "|   " + self.staticRooms[i].name + " room\n"
        msg += "-----------------------------------------------------------\n"

        # Send the avaliable rooms to the requesting client
        client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      removeClient
    #Input:         self -
    #               client -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def removeClient(self, client):
        # Check if the client is currently in a room
        if client.name in self.staticRoomMap:
            # Obtain the room mapping information
            infoMapping = self.staticRoomMap[client.name]

            # Check if the client is in the red room
            if 'red' in infoMapping.name:
                # Remove the client from the red room
                self.leaveStaticRoom(client, 0)

            # Check if the client is in the blue room
            if 'blue' in infoMapping.name:
                # Remove the client from the blue room
                self.leaveStaticRoom(client, 1)

            # Check if the client is in the yellow room
            if 'yellow' in infoMapping.name:
                # Remove the client from the yellow room
                self.leaveStaticRoom(client, 2)

            # Check if the client is in the green room
            if 'green' in infoMapping.name:
                # Remove the client from the green room
                self.leaveStaticRoom(client, 3)

            # Check if the client is in the purple room
            if 'purple' in infoMapping.name:
                # Remove the client from the purple room
                self.leaveStaticRoom(client, 4)

            # Check if the client is in the orange room
            if 'orange' in infoMapping.name:
                # Remove the client from the orange room
                self.leaveStaticRoom(client, 5)

        # Otherwise the client is in the lobby, so display bye message
        print "Client: " + client.name + " has left the server\n"

    #---------------------------------------------------------------------------
    #Function:      clientStaticRoom
    #Input:         self -
    #               client -
    #               staticIndex -
    #               staticRoom -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def clientStaticRoom(self, client, staticIndex, staticRoom):
        # Add the client to the selected static room
        self.staticRooms[staticIndex].clients.append(client)
        # Welcome the client to the selected static room
        self.staticRooms[staticIndex].roomWelcome(client)
        # Add the client to the static room mapping
        self.staticRoomMap[client.name] = staticRoom

    #---------------------------------------------------------------------------
    #Function:      leaveStaticRoom
    #Input:         self -
    #               client -
    #               staticIndex -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def leaveStaticRoom(self, client, staticIndex):
        # Remove the client from the red room
        self.staticRooms[staticIndex].removeClient(client)
        # Delete the client from the room mapping set
        del self.staticRoomMap[client.name]

    #---------------------------------------------------------------------------
    #Function:      invalidRoom
    #Input:         self -
    #               client -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def invalidRoom(self, client):
         # Message to the client
        msg = "-------------Please choose a valid room to enter------------\n"

        #Loop through the static room
        for i in range(Utilities.DEFAULT_NUMBER):
            msg += "|   " + self.staticRooms[i].name + " room\n"
        msg += "-----------------------------------------------------------\n"

        #Concatinate the instructions to the message
        msg += '\n' + self.splashScreen()
        # Send the intructions to the user
        client.socket.sendall(msg)


#---------------------------------Room CLASS------------------------------------
class Room:
    #Class constructor
    def __init__(self, name):
        self.clients = []
        self.name = name

    #---------------------------------------------------------------------------
    #Function:      roomWelcome
    #Input:         self -
    #               client -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def roomWelcome(self, client):
        # Create a random number generator with bounds between 1-3
        rand = random.randint(1,3)

        # Check if the selected welcome message is the first message
        if rand == 1:
            msg = "It's a bird, it's a plane, no it's " + client.name + " flying into the " + self.name + " room.\n"
        # Check if the selected welcome message is the seconde message
        elif rand == 2:
            msg = client.name + " hopped into the " + self.name + " room. Kangaroo!\n"
        # Otherwise the selected welcome message is the third message
        else:
            msg = client.name + " has arrived into the " + self.name + " room. Party's over.\n"

        # Loop through all of the clients in the room
        for client in self.clients:
            # Send the message to clients in the room
            client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      broadcastRoom
    #Input:         self -
    #               client -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def broadcastRoom(self, client, msg):
        # Create the message to be broadcast
        msg = client.name + ': ' + msg
        # Loop through all of the clients in the room
        for client in self.clients:
            client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      removeClient
    #Input:         self -
    #               client -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def removeClient(self, client):
        # Remove the client from the rooms list of clients
        self.clients.remove(client)
        # Create the rooms client left message
        msg = client.name.encode() + " has left the " + self.name + " room.\n"
        # Broadcast the message to the room
        self.broadcastRoom(client, msg)


#---------------------------------Client CLASS----------------------------------
class Client:
    #Class constructor
    def __init__(self, socket, name= "guest"):
        socket.setblocking(0)   #Set non-blocking
        self.socket = socket    #Socket object(communication)
        self.name = name        #Name given to socket(descriptor)

    #---------------------------------------------------------------------------
    #Function:      fileno
    #Input:         self -
    #Output:        none
    #Description:
    #---------------------------------------------------------------------------
    def fileno(self):
        return self.socket.fileno()

# Create the avaliable rooms
redRoom = Room(Utilities.STATIC_ROOM[0])
blueRoom = Room(Utilities.STATIC_ROOM[1])
yellowRoom = Room(Utilities.STATIC_ROOM[2])
greenRoom = Room(Utilities.STATIC_ROOM[3])
purpleRoom = Room(Utilities.STATIC_ROOM[4])
orangeRoom = Room(Utilities.STATIC_ROOM[5])
