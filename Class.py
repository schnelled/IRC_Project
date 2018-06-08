#Import needed libraries - Heirarchy Lobby, Rooms, Clients
#There is always a single lobby, that contains rooms, that can hold clients
import socket, string, random
import Utilities

#----------------------------------Lobby CLASS----------------------------------
#Class Functions:
#   lobbyWelcome(self, newClient)
#   introduction(self, msg, client)
#   handleMsg(self, client, msg)
#   splashScreen(self)
#   showRooms(self, client)
#   showRoomMapping(self, client)
#   removeLobby(self, client)
#   joinStaticRoom(self, client, staticIndex)
#   leaveStaticRoom(self, client, staticIndex)
#   invalidRoom(self, client)
#   alreadyPresent(self, client)

class Lobby:
    #Class constructor
    def __init__(self):
        #Defualt static rooms
        self.staticRooms = [redRoom, blueRoom, yellowRoom, greenRoom, purpleRoom, orangeRoom]
        self.redRoomMap = []
        self.blueRoomMap = []
        self.yellowRoomMap = []
        self.greenRoomMap = []
        self.purpleRoomMap = []
        self.orangeRoomMap = []
        #Dynamic rooms
        self.dynamicRooms = {}    #{room name: Room(class)}
        self.dynamicRoomMap = {}  #{client name: room map}

    #---------------------------------------------------------------------------
    #Function:      lobbyWelcome
    #Input:         self - The lobby object the function comes from
    #               newClient - The client being welcomed to the lobby
    #Output:        none
    #Description:   Send the welcome message to the new client. In order to
    #               obtain the client's name
    #---------------------------------------------------------------------------
    def lobbyWelcome(self, newClient):
        #Send a welcome message to the new client
        newClient.socket.sendall('Welcome to the party!\nPlease tell us your name:\n')

    #---------------------------------------------------------------------------
    #Function:      introduction
    #Input:         self - The lobby object the function comes from
    #               msg - The message containing the client's name
    #               client - The client who provided their name
    #Output:        none
    #Description:   Send the welcome message to the new client. In order to
    #               obtain the client's name and display the lobbys home page
    #---------------------------------------------------------------------------
    def introduction(self, msg, client):
        #Obtain the splash screen
        intro = self.splashScreen()

        #Extract the user input name from the message
        user = msg.split()[1]

        #Set the clients name to the input
        client.name = user

        #Diplay connnection with new name
        print '---------------------------------------------------------------'
        print 'New connection from: ' + client.name
        print '---------------------------------------------------------------\n'

        #Send the instructions to the user
        client.socket.sendall('\nHello ' + client.name + '\n' + intro)

    #---------------------------------------------------------------------------
    #Function:      handleMsg
    #Input:         self - The lobby object the function comes from
    #               client - The client who sent the message
    #               msg - The message received from the client
    #Output:        none
    #Description:   Handle the message received from the client. Checks for the
    #               name sent from the user and also...
    #                   Case 1:     Received name from the client
    #                   Case 2:     List the avaliable rooms
    #                   Case 3:     List the room mapping
    #                   Case 4:     Join a static room
    #                   Defualt:
    #---------------------------------------------------------------------------
    def handleMsg(self, client, msg):
        #Display what the client transmitted
        print '\n--------------------New Message from Client--------------------'
        print client.name + ' sent: ' + msg

        #Obtain the splash screen
        intro = self.splashScreen()

        #Check for name prefix
        if 'name:' in msg:
            #Initial introduction to obtain new clients name
            self.introduction(msg, client)

        #Check for the list rooms command
        elif '1' in msg:
             #Show the rooms to the client
             self.showRooms(client)

        #Check for the show room mapping command
        elif '2' in msg:
            #Check that at least one client is in a room
            if len(self.redRoomMap) > 0 or len(self.blueRoomMap) > 0 or len(self.yellowRoomMap) > 0 or len(self.greenRoomMap) > 0 or len(self.purpleRoomMap) > 0 or len(self.orangeRoomMap) > 0:
                #Show the mapping of all the rooms
                self.showRoomMapping(client)

            #Otherwise display no clients are mapped message
            else:
                #Create no clients mapped message, with instructions
                msg = '\nNo clients are mapped. Please select another instruction.\n'
                msg += self.splashScreen()
                #Send the invalid user input message screen back
                client.socket.sendall(msg)

        #Check for the join default room command
        elif '3' in msg:
            #Check for valid input
            if len(msg.split()) <= 3 and len(msg.split()) > 1:
                #Obtain the selected room name
                roomName = msg.split()[1]

                #Check if client wants to join the red room
                if roomName == 'red':
                    #Make sure the client is not already in the red room
                    if client.name not in self.redRoomMap:
                        #Client joins the red room
                        self.joinStaticRoom(client, 0)
                    #Otherwise the client is alreay in the red room
                    else:
                        #Create message to let client know they're already in room
                        self.alreadyPresent(client)

                #Check if client wants to join the blue room
                elif roomName == 'blue':
                    #Make sure the client is not already in the blue room
                    if client.name not in self.blueRoomMap:
                        #Client joins the blue room
                        self.joinStaticRoom(client, 1)
                    #Otherwise the client is already in the blue room
                    else:
                        #Create message to let client know they're already in room
                        self.alreadyPresent(client)

                #Check if client wants to join the yellow room
                elif roomName == 'yellow':
                    #Make sure the client is not already in the yellow room
                    if client.name not in self.yellowRoomMap:
                        #Client joins the yellow room
                        self.joinStaticRoom(client, 2)
                    #Otherwise the client is already in the yellow room
                    else:
                        #Create message to let client know they're already in room
                        self.alreadyPresent(client)

                #Check if client wants to join the green room
                elif roomName == 'green':
                    #Make sure the client is not already in the green room
                    if client.name not in self.greenRoomMap:
                        #Client joins the green room
                        self.joinStaticRoom(client, 3)
                    #Otherwise the client is already in the green room
                    else:
                        #Create message to let client know they're already in room
                        self.alreadyPresent(client)

                #Check if client wants to join the purple room
                elif roomName == 'purple':
                    #Make sure the client is not already in the purple room
                    if client.name not in self.purpleRoomMap:
                        #Client joins the purple room
                        self.joinStaticRoom(client, 4)
                    #Otherwise the client is already in the purple room
                    else:
                        #Create message to let client know they're already in room
                        self.alreadyPresent(client)

                #Check if client wants to join the orange room
                elif roomName == 'orange':
                    #Make sure the client is not already in the orange room
                    if client.name not in self.orangeRoomMap:
                        #Client joins the orange room
                        self.joinStaticRoom(client, 5)
                    #Otherwise the client is already in the orange room
                    else:
                        #Create message to let client know they're already in room
                        self.alreadyPresent(client)

                #Otherwise invalid room name was chosen
                else:
                    #Send message to client to choose a valid room
                    self.invalidRoom(client)

            #Otherwise invalid usage of the command
            else:
                #Send message to client to choose a valid room
                self.invalidRoom(client)

        #Check for the leave a room command
        elif '4' in msg:
            #Check for valid input
            if len(msg.split()) <= 3 and len(msg.split()) > 1:
                #Obtain the room the client is leaving
                leaving = msg.split()[1]

                #Check if the client is leaving the red room
                if leaving == 'red':
                    #Check if the client is in the red room
                    if client.name in self.redRoomMap:
                        #Leave the red room
                        self.leaveStaticRoom(client, 0)
                        msg = '\nYou left the red room\n'

                #Check if the client is trying to leave the blue room
                elif leaving == 'blue':
                    #Check if the client is in the blue room
                    if client.name in self.blueRoomMap:
                        #Leave the blue room
                        self.leaveStaticRoom(client, 1)
                        msg = '\nYou left the blue room\n'

                #Check if the client is trying to leave the yellow room
                elif leaving == 'yellow':
                    #Check if the client is in the yellow room
                    if client.name in self.yellowRoomMap:
                        #Leave the yellow room
                        self.leaveStaticRoom(client, 2)
                        msg = '\nYou left the yellow room\n'

                #Check if the client is trying to leave the green room
                elif leaving == 'green':
                    #Check if the client is in the green room
                    if client.name in self.greenRoomMap:
                        #Leave the green room
                        self.leaveStaticRoom(client, 3)
                        msg = '\nYou left the green room\n'

                #Check if the client is trying to leave the purple room
                elif leaving == 'purple':
                    #Check if the client is in the purple room
                    if client.name in self.purpleRoomMap:
                        #Leave the purple room
                        self.leaveStaticRoom(client, 4)
                        msg = '\nYou left the purple room\n'

                #Check if the client is trying to leave the orange room
                elif leaving == 'orange':
                    #Check if the client is in the orange room
                    if client.name in self.orangeRoomMap:
                        #Leave the orange room
                        self.leaveStaticRoom(client, 5)
                        msg = '\nYou left the orange room\n'

                #Otherwise invalid room choosen
                else:
                    # Invalid choice message
                    msg = '\nThat room doesn\'t exist\n'

                # Create instruction message
                msg += self.splashScreen()
                # Send intructions to the client
                client.socket.sendall(msg)

            #Otherwise invalid usage of the command
            else:
                #Create invalid input message to sent back to client, with instructions
                msg = '\nInvalid user input. Please select one of the following instructions.\n'
                msg += self.splashScreen()
                #Send the invalid user input message screen back
                client.socket.sendall(msg)

        #Check for the quit command
        elif '5' in msg:
            #Send the quit message back to the client
            client.socket.sendall(Utilities.QUIT)
            #Remove the client from there room
            self.removeClient(client)

        #Otherwise the receive message was invalid
        else:
            #Check if the client is in a room
            if client.name in self.redRoomMap or self.blueRoomMap or self.yellowRoomMap or self.greenRoomMap or self.purpleRoomMap or self.orangeRoomMap:
                #Check if the client is in the red room
                if client.name in self.redRoomMap:
                    # Boardcast the message to the red room only
                    self.staticRooms[0].broadcastRoom(client, msg)

                # Check if the client is in the blue room
                if client.name in self.blueRoomMap:
                    # Broadcast the message to the blue room only
                    self.staticRooms[1].broadcastRoom(client, msg)

                # Check if the client is in the yellow room
                if client.name in self.yellowRoomMap:
                    # Broadcast the message to the yellow room only
                    self.staticRooms[2].broadcastRoom(client, msg)

                # Check if the client is in the green room
                if client.name in self.greenRoomMap:
                    # Broadcast the message to the green room only
                    self.staticRooms[3].broadcastRoom(client, msg)

                # Check if the client is in the purple room
                if client.name in self.purpleRoomMap:
                    # Broadcast the message to the purple room only
                    self.staticRooms[4].broadcastRoom(client, msg)

                # Check if the client is in the orange room
                if client.name in self.orangeRoomMap:
                    # Broadcast the message to the orange room only
                    self.staticRooms[5].broadcastRoom(client, msg)

            # Otherwise user input invalid command
            else:
                # Create invalid input message to sent back to client, with instructions
                msg = '\nInvalid user input. Please select one of the following instructions.\n'
                msg += self.splashScreen()
                # Send the invalid user input message screen back
                client.socket.sendall(msg)


    #---------------------------------------------------------------------------
    #Function:      splashScreen
    #Input:         self - The lobby object the function comes from
    #Output:        msg - Message containing splash menu
    #Description:   Return a string message containing the slash menu with
    #               information on avaliable commands(options)
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
|    2. To show the room mapping                            |
|    3. [room name] to join a defualt room                  |
|    4. [room name] to leave a room                         |
|    5. To quit & leave the server                          |
|___________________________________________________________|""" + '\n'

        #Return the instruction menu
        return msg

    #---------------------------------------------------------------------------
    #Function:      showRooms
    #Input:         self - The lobby object the function comes from
    #               client -The client requesting the avaliable rooms
    #Output:        none
    #Description:   Send a list of all the avaliable rooms to the client
    #---------------------------------------------------------------------------
    def showRooms(self, client):
        #Display show rooms introduction message
        msg = '--------------------Current Static Rooms--------------------\n'

        #Loop through the static room
        for i in range(Utilities.DEFAULT_NUMBER):
            msg += '|   ' + self.staticRooms[i].name + ' room\n'
        msg += '------------------------------------------------------------\n'

        #Send the avaliable rooms to the requesting client
        client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      showRoomMapping
    #Input:         self - The lobby object the function comes from
    #               client -The client requesting the room mappings
    #Output:        none
    #Description:   Send the room mappings to the client
    #---------------------------------------------------------------------------
    def showRoomMapping(self, client):
        #Declare the message
        msg = ''

        #Check if the red room has at least one client
        if len(self.redRoomMap) > 0:
            msg += '--------------------------Red Room---------------------------\n'
            #Loop through the red room mapping
            for x in range(len(self.redRoomMap)):
                msg += '|    ' + self.redRoomMap[x] + '\n'

        #Check if the blue room has at least one client
        if len(self.blueRoomMap) > 0:
            msg += '-------------------------Blue Room---------------------------\n'
            #Loop through the blue room mapping
            for x in range(len(self.blueRoomMap)):
                msg += '|    ' + self.blueRoomMap[x] + '\n'

        #Check if the yellow room has at least one client
        if len(self.yellowRoomMap) > 0:
            msg += '------------------------Yellow Room--------------------------\n'
            #Loop through the yellow room mapping
            for x in range(len(self.yellowRoomMap)):
                msg += '|    ' + self.yellowRoomMap[x] + '\n'

        #Check if the green room has at least one client
        if len(self.greenRoomMap) > 0:
            msg += '-------------------------Green Room--------------------------\n'
            #Loop through the green room mapping
            for x in range(len(self.greenRoomMap)):
                msg += '|    ' + self.greenRoomMap[x] + '\n'

        #Check if the purple room has at least one client
        if len(self.purpleRoomMap) > 0:
            msg += '-------------------------Purple Room-------------------------\n'
            #Loop through the purple room
            for x in range(len(self.purpleRoomMap)):
                msg += '|    ' + self.purpleRoomMap[x] + '\n'

        #Check if the orange room has at least one client
        if len(self.orangeRoomMap) > 0:
            msg += '-------------------------Orange Room-------------------------\n'
            #Loop through the orange room mapping
            for x in range(len(self.orangeRoomMap)):
                msg += '|    ' + self.orangeRoomMap[x] + '\n'

        #Send the all room mappings to the client
        client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      removeClient
    #Input:         self - The lobby object the function comes from
    #               client - The client being removed from room mappings
    #Output:        none
    #Description:   Remove the client from all occupied rooms
    #---------------------------------------------------------------------------
    def removeClient(self, client):
        #Check if the client is in the red room
        if client.name in self.redRoomMap:
            #Remove the client from the red room
            self.leaveStaticRoom(client, 0)

        #Check if the client is in the blue room
        if client.name in self.blueRoomMap:
            #Remove the client from the blue room
            self.leaveStaticRoom(client, 1)

        #Check if the client is in the yellow room
        if client.name in self.yellowRoomMap:
            #Remove the client from the yellow room
            self.leaveStaticRoom(client, 2)

        #Check if the client is in the green room
        if client.name in self.greenRoomMap:
            #Remove the client from the green room
            self.leaveStaticRoom(client, 3)

        #Check if the client is in the purple room
        if client.name in self.purpleRoomMap:
            #Remove the client from the purple room
            self.leaveStaticRoom(client, 4)

        #Check if the client is in the orange room
        if client.name in self.orangeRoomMap:
            #Remove the client from the orange room
            self.leaveStaticRoom(client, 5)

        #Otherwise the client is in the lobby, so display bye message
        print "Client: " + client.name + " has left the server\n"

    #---------------------------------------------------------------------------
    #Function:      joinStaticRoom
    #Input:         self - The lobby object the function comes from
    #               client - The client joining the selected room
    #               staticRoom - The index of the selected room
    #Output:        none
    #Description:   Client joins the selected room and is appended to the mapping
    #---------------------------------------------------------------------------
    def joinStaticRoom(self, client, staticIndex):
        #Check if the client is joining the red room
        if staticIndex == 0:
            #Add the client to the red room
            self.staticRooms[staticIndex].clients.append(client)
            #Welcome the client to the red room
            self.staticRooms[staticIndex].roomWelcome(client)
            #Add the client to the red room mapping
            self.redRoomMap.append(client.name)

        #Check if the client is joining the blue room
        elif staticIndex == 1:
            #Add the client to the blue room
            self.staticRooms[staticIndex].clients.append(client)
            #Welcome the client to the blue room
            self.staticRooms[staticIndex].roomWelcome(client)
            #Add the client to the blue room mapping
            self.blueRoomMap.append(client.name)

        #Check if the client is joining the yellow room
        elif staticIndex == 2:
            #Add the client to the yellow room
            self.staticRooms[staticIndex].clients.append(client)
            #Welcome the client to the yellow room
            self.staticRooms[staticIndex].roomWelcome(client)
            #Add the client to the yellow room mapping
            self.yellowRoomMap.append(client.name)

        #Check if the client is joining the green room
        elif staticIndex == 3:
            #Add the client to the green room
            self.staticRooms[staticIndex].clients.append(client)
            #Welcome the client to the green room
            self.staticRooms[staticIndex].roomWelcome(client)
            #Add the client to the green room mapping
            self.greenRoomMap.append(client.name)

        #Check if the client is joining the purple room
        elif staticIndex == 4:
            #Add the client to the purple room
            self.staticRooms[staticIndex].clients.append(client)
            #Welcome the client to the purple room
            self.staticRooms[staticIndex].roomWelcome(client)
            #Add the client to the purple room mapping
            self.purpleRoomMap.append(client.name)

        #Otherwise the client is joining the orange room
        else:
            #Add the client to the orange room
            self.staticRooms[staticIndex].clients.append(client)
            #Welcome the client to the orange room
            self.staticRooms[staticIndex].roomWelcome(client)
            #Add the client to the orange room mapping
            self.orangeRoomMap.append(client.name)

    #---------------------------------------------------------------------------
    #Function:      leaveStaticRoom
    #Input:         self - The lobby object the function comes from
    #               client - The client leaving the room
    #               staticIndex - The index of the room the client is leaving
    #Output:        none
    #Description:   Client leaves the selected room they occupied and is removed
    #               from the mapping
    #---------------------------------------------------------------------------
    def leaveStaticRoom(self, client, staticIndex):
        #Remove the client from the selected room
        self.staticRooms[staticIndex].removeClient(client)

        #Check if the client is leaving the red room
        if staticIndex == 0:
            #Remove the client from the red room's mapping
            self.redRoomMap.remove(client.name)

        #Check if the client is leaving the blue room
        if staticIndex == 1:
            #Remove the client from the blue room's mapping
            self.blueRoomMap.remove(client.name)

        #Check if the client is leaving the yellow room
        if staticIndex == 2:
            #Remove the client from the yellow room's mapping
            self.yellowRoomMap.remove(client.name)

        #Check if the client is leaving the green room
        if staticIndex == 3:
            #Remove the client from the green room's mapping
            self.greenRoomMap.remove(client.name)

        #Check if the client is leaving the purple room
        if staticIndex == 4:
            #Remove the client from the purple room's mapping
            self.purpleRoomMap.remove(client.name)

        #Check if the client is leaving the orange room
        if staticIndex == 5:
            #Remove the client from the orange's mapping
            self.orangeRoomMap.remove(client.name)

    #---------------------------------------------------------------------------
    #Function:      invalidRoom
    #Input:         self - The lobby object the function comes from
    #               client - The client that selected an invalid room
    #Output:        none
    #Description:   Tells the client they entered an invalid room name, then
    #               lists the avaliable room, and displays the slash menu
    #---------------------------------------------------------------------------
    def invalidRoom(self, client):
         #Message to the client
        msg = "-------------Please choose a valid room to enter------------\n"

        #Loop through the static room
        for i in range(Utilities.DEFAULT_NUMBER):
            msg += "|   " + self.staticRooms[i].name + " room\n"
        msg += "-----------------------------------------------------------\n"

        #Concatinate the instructions to the message
        msg += '\n' + self.splashScreen()
        #Send the intructions to the user
        client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      alreadyPresent
    #Input:         self - The lobby object the function comes from
    #               client - Client that is already present to the room
    #Output:        none
    #Description:   Transmits to the client to let them know they're already in
    #               the selected room
    #---------------------------------------------------------------------------
    def alreadyPresent(self, client):
        #Message to inform client they're already in the room selected
        msg = '\nError: Already in Selected Room'
        #Concatinate the instructions to the message
        msg += '\n' + self.splashScreen()
        #Send the intructions to the user
        client.socket.sendall(msg)


#---------------------------------Room CLASS------------------------------------
#Class Functions:
#   roomWelcome(self, client)
#   broadcastRoom(self, client)
#   removeClient(self, client)

class Room:
    #Class constructor
    def __init__(self, name):
        self.clients = []
        self.name = name

    #---------------------------------------------------------------------------
    #Function:      roomWelcome
    #Input:         self - The room object the function comes from
    #               client - The client joining and being welcomed to the room
    #Output:        none
    #Description:   Selects random introduction message for the room and sends
    #               the introduction message to everyone in the room
    #---------------------------------------------------------------------------
    def roomWelcome(self, client):
        #Create a random number generator with bounds between 1-3
        rand = random.randint(1,3)

        #Check if the selected welcome message is the first message
        if rand == 1:
            msg = "It's a bird, it's a plane, no it's " + client.name + " flying into the " + self.name + " room.\n"

        #Check if the selected welcome message is the seconde message
        elif rand == 2:
            msg = client.name + " hopped into the " + self.name + " room. Kangaroo!\n"

        #Otherwise the selected welcome message is the third message
        else:
            msg = client.name + " has arrived into the " + self.name + " room. Party's over.\n"

        #Loop through all of the clients in the room
        for client in self.clients:
            #Send the message to clients in the room
            client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      broadcastRoom
    #Input:         self - The room object the function comes from
    #               client - The client transmitting to the room
    #Output:        none
    #Description:   Boardcast the message to everyone in the room
    #---------------------------------------------------------------------------
    def broadcastRoom(self, client, msg):
        #Create the message to be broadcast
        msg = client.name + ': ' + msg
        #Loop through all of the clients in the room
        for client in self.clients:
            client.socket.sendall(msg)

    #---------------------------------------------------------------------------
    #Function:      removeClient
    #Input:         self - The room object the function comes from
    #               client - The client to be removed from the room
    #Output:        none
    #Description:   Removes the client from the room and send a message to
    #               everyone in the room that the client left
    #---------------------------------------------------------------------------
    def removeClient(self, client):
        #Remove the client from the rooms list of clients
        self.clients.remove(client)
        #Create the rooms client left message
        msg = client.name.encode() + " has left the " + self.name + " room.\n"
        #Broadcast the message to the room
        self.broadcastRoom(client, msg)


#---------------------------------Client CLASS----------------------------------
#Class Functions:
#   fileno(self)

class Client:
    #Class constructor
    def __init__(self, socket, name= "guest"):
        socket.setblocking(0)   #Set non-blocking
        self.socket = socket    #Socket object(communication)
        self.name = name        #Name given to socket(descriptor)

    #---------------------------------------------------------------------------
    #Function:      fileno
    #Input:         self - The client object the function comes from
    #Output:        fileno - The fileno of the socket
    #Description:   Returns the fileno for the client's socket
    #---------------------------------------------------------------------------
    def fileno(self):
        return self.socket.fileno()

#Create the avaliable rooms
redRoom = Room(Utilities.STATIC_ROOM[0])
blueRoom = Room(Utilities.STATIC_ROOM[1])
yellowRoom = Room(Utilities.STATIC_ROOM[2])
greenRoom = Room(Utilities.STATIC_ROOM[3])
purpleRoom = Room(Utilities.STATIC_ROOM[4])
orangeRoom = Room(Utilities.STATIC_ROOM[5])
