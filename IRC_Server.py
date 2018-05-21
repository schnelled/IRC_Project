import IRC_Support
from IRC_Support import Lobby, Room, Client

# Create the server socket
serverSocket = IRC_Support.makeSocket(IRC_Support.PORT)

# Create a lobby object
lobby = Lobby()
