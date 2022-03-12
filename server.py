#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Allison Little
# Created Date: 3/11/2022
# version = 1.0
# ---------------------------------------------------------------------------
"""
Code for the server side of a client-server chat
    Server opens a listening socket on the localhost at a set port
    When a message is received from the client, the message is displayed
    A response can be written to the server and sent back to the client
    When a quit character is received from the client, the connection closes
"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import sys
from socket import *

# ---------------------------------------------------------------------------
# Globals
# ---------------------------------------------------------------------------
QUIT_CHARACTER = '/q'

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

# Verify that at least one argument was passed
if len(sys.argv) < 2:
    print('Usage error: missing port number.')
    exit(1)
# Read in server port from first argument
serverPort = int(sys.argv[1])

# Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server listening on port ', serverPort)
# Listen for a connection
while True:
    # Accept the request, create a connection socket
    connectionSocket, addr = serverSocket.accept()
    print('Client established, waiting on message')
    # Loop through receiving messages and responding to client
    while True:
        # Receive client message
        clientMessage = connectionSocket.recv(255)
        # Display the client's message
        print(clientMessage.decode())

        # Check if the client message was the quit character
        if clientMessage.decode() == QUIT_CHARACTER:
            # Quit character detected, close connection
            connectionSocket.close()
            serverSocket.close()
            exit()

        # Prompt user for response and send to client
        serverMessage = input('>')
        connectionSocket.send(serverMessage.encode())
