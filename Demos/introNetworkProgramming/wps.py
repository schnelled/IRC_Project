# wps.py

# Client for the server for remote versions of the w and ps commands

# User can check load on machine without logging in (or even without having
# an account on the remote machine)

# Usage:
#   python3 wsp.py remotehostname port_num {w, ps}

# e.g. python3 wps.py nimbus.org 8888 w would cause the server at nimbus.org
# on port 8888 to run the UNIX command there, and send the output of the
# command back to the client here

import socket, sys

def main():
    # Setup the connection
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Obtain the host and the port number
    host = sys.argv[1]                  #Server address
    port = int(sys.argv[2])             #Server port

    # Connect to the server
    clientSocket.connect((host, port))

    # Send w or ps command to server, by writing that command to the "file"
    clientSocket.send(sys.argv[3].encode())

    # Read result as lines from the "file-like" object
    # Wrap it to a "file-like object"
    flo = clientSocket.makefile('r',0)  #Read-only, unbuffered

    # Recall that stdout is a file-like object too
    sys.stdout.writelines(flo.readlines())

if __name__ == '__main__':
    main()
