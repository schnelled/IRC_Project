# Include the socket module
from socket import *

# Declare and initialize server variables
serverName = 'servername'
serverPort = 12000

# Create a TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)

#Initiate the TCP server connection
clientSocket.connect((serverName, serverPort))

# Prompt and obtain input from the user
sentence = input('Input lowercase sentence')

# Encode the user input and transmit the TCP message
clientSocket.send(sentence.encoded())

# Recieve the modifed sentence from the server in 1kB sized packets
modifiedSentence = clientSocket.recv(1024)

# Decode and display the message from the server
print('From Server: ', modifiedSentence.decoded())

# Close the TCP socket
clientSocket.close()
