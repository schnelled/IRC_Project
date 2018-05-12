# svr.py

# Server for remote versions of the w and ps commands

# User can check load on machine without logging in (or even without
# having an account on the remote machine)

# Usage:
#   python3 svr.py port_num

import socket, sys, os

def main():
    # Create listening socket
    listenSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Obtain the port number and bind
    port = int(sys.argv[1])
    listenSocket.bind(('', port))

    # Enter listening loop
    while True:
        # Accept "call" from client
        listenSocket.listen(1)
        (conn, addr) = listenSocket.accept()

        # Diplay the connection information
        print('Client is at ', addr)

        # Get and run command from client, then get its output
        rc = conn.recv(2).decode()

        # Run the command in a Unix-style pipe
        ppn = os.popen(rc)

        # ppn iis a "file-like object," so can apply readlines()
        r1 = ppn.readlines()

        # Create a file-like object from the connection socket
        flo = conn.makefile('w',0)          # Write-only, unbuffered
        flo.writelines(r1[:-1])

        # Clean up
        # Must close the socket and the wrapper
        flo.close()
        conn.close()

if __name__ == '__main__':
    main()
