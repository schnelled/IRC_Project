# Include the socket module
from socket import *

# Declare and initialize server variables
serverName = 'hostname'
serverPort = 1200

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Prompt the user for input
message = input('Input lowercase sentence:')

# Send the UDP message encoded to the server
clientSocket.sendto(message.encode(), (serverName, serverPort))

# Recieve the UDP message from the server
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

# Display the decoded UDP message
print(modifiedMessage.decode())

# Close the UDP socket
clientSocket.close()
