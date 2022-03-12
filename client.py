#!/usr/bin/env python
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Allison Little
# Created Date: 3/11/2022
# version = 1.0
# ---------------------------------------------------------------------------
"""
Code for the client side of a client-server chat
    Client connects to the server at a specified port on the localhost
    User inputs a message that the client sends to the server
    When a response is received from the server, the message is displayed
    Chat continues until user inputs quit character to send to server
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import sys
from socket import *

# ---------------------------------------------------------------------------
# GLOBALS
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

# Create a client socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# Connect the client to the server
clientSocket.connect(('localhost', serverPort))
print('Connected to localhost port ', serverPort)

# Prompt user for input
print('Type ', QUIT_CHARACTER, ' to quit')
print('Enter messages to send to server: ')

# Enter chat with server by sending and receiving messages
while True:
    # Get input from user
    clientMessage = input('>')
    # Send message to server
    clientSocket.send(clientMessage.encode())

    # Check if the message was the quit character
    if clientMessage == QUIT_CHARACTER:
        # Client sent quit character, no more responses from server
        break

    # Receive response from server
    serverMessage = clientSocket.recv(20)
    # Print the server's response
    print(serverMessage.decode())

# Quit character has been sent, exit program
exit()