import socket
import threading

PORT = 5050

# my device name
NAME = socket.gethostname()
print(NAME)


# Get my device ip address

# WAY1: hard code ip address
# SERVER = '127.0.1.1'

# WAY2: This address of server only works when the client and server are under the same wifi network
# Server divece's personal ip address
# below code return's my device's ip address
# SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)

# WAY3: This address will be globally public for any user in the world to connect to our server through internet
# We need to get the server device's public ip address
# search my public ip address in google to get it
SERVER = socket.gethostbyname('localhost')
print(SERVER)

# we need to make sockets which helps us to open up this device to another connections
# 1. pick the port and pick the server
ADDRESS = (SERVER, PORT)
# 2. pick the socket and bind it to the address
# it requires a).ip address type that we are gonna listen to b).file stream type
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
# bind the server ip address to the port
server.bind(ADDRESS)
# so anything that connects to the address(ADDRESS) now will hit the socket

# the first thing that we recieve from a client is called header and it is of size 64
# it gives us info about the size of the msg that we are about to recieve from the client
HEADER = 64

# custom disconnect message
DISCONNECT_MESSAGE = '!disconnect'

# Now we need to set up this socket for listening and wait for new connections


def handle_listening(address, connection):
    """
    This function will handle all the communications between the client and the server
    """
    print("New Connection is established with: ", address, "address")
    connected = True
    while connected:
        # we will wait to recieve info from the client
        # we will wait for the message until it is fully recieved
        # we will recieve header first
        msg_length = (connection.recv(HEADER).decode(
            'utf-8'))  # decode it from byte to readable format
        if msg_length:
            # convert to integer
            msg_length = int(msg_length)
            # recieve the message
            # recv takes the length of the msg as argument
            msg = connection.recv(msg_length).decode('utf-8')

            # close connecrtion
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print('[', address, ']', 'sent :', msg)
            # send confirmation message from server to client
            connection.send('Msg Recieved xd'.encode('utf-8'))

    # Disconnecet the client and close the connection
    connection.close()


# start the socket
def start():
    """
    Listen to connections and pass them to handle_listening function
    """
    # kickstart the server
    server.listen()
    print("Server is alive and it's address is = ", SERVER)
    while True:
        # server.accept will wait until a client tries to join our server address
        connection, address = server.accept()
        # connection variable is an object which we can use to send info back to the client - socket object
        # address contains the port and server addressess of our client

        # we will create a new thread calling handle_listening function to process that particular client separately
        thread = threading.Thread(
            target=handle_listening, args=(address, connection))
        thread.start()
        # good to know the number of users
        print("Number of clients active = ", threading.activeCount()-1)


# start the server
print("Starting The server")
start()

# What if we wanna render the message that a parrticular client sent to server to all the clients
# one way is to have a global list which append all the messages from the clients and render it to everyone
# other way is to do a constant ping command, we can make client to constantly send a !read command,
# when the server recieves that we can spit back any new messages that the server recieved,
# it's like it's constantly pinging and ask for information
