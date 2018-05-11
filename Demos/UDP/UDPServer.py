# Include the socket module
from socket import *

# Declare and initialize server variables
serverPort = 12000

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

# Continue to loop forever
while True:
    # Recieve the UDP message from the client in 2kB size packets
    message, clientAddress = serverSocket.recvfrom(2048)

    # Decode the message and convert lowercase to uppercase
    modifiedMessage = message.decode().upper()

    # Encode the UDP message and send it to the client
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
