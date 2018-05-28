#Internet Chat Relay Client

#Import needed libraries
import socket, sys, select
import Utilities

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':

    #Server startup message
    print "Staring up the client"

    #Check for proper usage of the client program
    if(len(sys.argv) < 2):
        #Display and handle the error for wrong usage
        print "Usage: pyhton2 Client.py [hostname]"
        sys.exit()

    #Set the prefix
    prefix = ""

    #Host name of the server
    host = sys.argv[1]

    #Create a TCP socket using IPv4
    clientSocket = Utilities.createSocket()
    #Setup the server socket for connection
    clientSocket = Utilities.clientSetup(clientSocket, host)

    #Create an entry for the connection list
    socketList = [sys.stdin, clientSocket]

    while True:

        #Handle the socket list functions during the connection
        readSockets, writeSockets, errorSockets =  select.select(socketList, [], [])

        #Wait for socket to read
        for sock in readSockets:

            #Check for incoming message
            if sock is clientSocket:
                #Recieve the transmitted message
                msg = sock.recv(Utilities.RECV_BUFFER)

                #Check if message is nothing (error)
                if not msg:
                    #Display and handle the error
                    print "Disconnected from chat server"
                    sys.exit()

                #Otherwise handle the valid message transmitted from the server
                else:
                    # Check for quit message
                    if msg == Utilities.QUIT:
                        # Say goodbye to the client and exit
                        sys.stdout.write('\nGoodbye, chat with you later\n')
                        sys.exit()

                    # Otherwise handle the greating or normal message states
                    else:
                        #Display the message to the client
                        sys.stdout.write(msg.decode())

                        #Check if the client is new
                        if "Please tell us your name" in msg.decode():
                            prefix = "name: "
                            #Otherwise the client is not new
                        else:
                            prefix = ""

                        #Prompt the client
                        Utilities.clientPrompt()


            #Otherwise outgoing message
            else:
                #Transmit the message to the server
                msg = prefix + sys.stdin.readline()
                clientSocket.sendall(msg.encode())
