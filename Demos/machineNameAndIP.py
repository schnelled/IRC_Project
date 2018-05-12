# Include the socket module
import socket

#------------------------------------------------------------------------------
# Function:     print_machine_info
# Input:        none
# Output:       none (void)
# Description:  displays the host name and IP address
#------------------------------------------------------------------------------
def print_machine_info():
    # Obtain both the host name and the IP address of the machine
    hostName = socket.gethostname()
    IPAddr = socket.gethostbyname(hostName)

    # Dipslay the machine's host name and IP address
    print("The host name: ", hostName)
    print("Th IP address: ", IPAddr)

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':
    # Call the function to display the machines information
    print_machine_info()
