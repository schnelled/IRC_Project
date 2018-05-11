# Include the socket module
from socket import *

# Declare and initialize server variables
serverPort = 12000

# Create a TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the port
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

# Continue to loop forever
while True:
    # Accept TCP client connection
    connectionSocket, addr = serverSocket.accept()

    # Recieve the decoded TCP message from the client in 1kB size packets
    sentence = connectionSocket.recv(1024).decode()

    # Convert the message from lowercase to uppercase
    capitalizedSentence = sentence.upper()

    # Encode and sent the TCP message back to the client
    connectionSocket.send(capitalizedSentence.encode())

    # Close the TCP socket
    connectionSocket.close()
