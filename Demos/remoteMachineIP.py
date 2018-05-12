# Include the socket module
import socket

#------------------------------------------------------------------------------
# Function:     get_remote_machine_info
# Input:        none
# Output:       none (void)
# Description:  display the IP of a remote machine
#------------------------------------------------------------------------------
def get_remote_machine_info():
    # Initialize the remote host name
    remoteHost = 'www.python.org'

    # Try to obtain the IP address of the host
    try:
        # Display the IP address of the host
        print("IP address: ", socket.gethostbyname(remoteHost))
    # Check for errors
    except socket.error as errMsg:
        # Display the error message
        print(remoteHost, ": ", errMsg)

# Check to see if the script is being run directly or add as a module
if __name__ == '__main__':
    # Call the function to display the remote machines IP address
    get_remote_machine_info()
