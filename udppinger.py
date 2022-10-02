import argparse
from socket import *
import time



address = 'simplesmtp.thought.net' # Stores the address of the server we are pinging
port = 8192                        # Stores the port 
sock = socket(AF_INET, SOCK_DGRAM) # Creates the socket
sock.settimeout(1)                 # Sets a timeout threshold for the socket 1 second in our case
count = 0                          # Counter for the amount of times we ping 
minTime = 1000                     # Initializes minimum time variable
maxTime = 0                        # Initializes maximum time variable
averageTime = 0                    # Initializes average time variable
lostPackets = 0                    # Initializes variable to keep track of lost packets
while count < 10:                  # While loop our function will be running in 
    count = count + 1              # Incrememnts count variable until it hits ten and the while loop finishes 
    message = "ping".encode()      # Stores the ping message
    sock.sendto(message, (address, port))   # Sends the ping message to the server
    timer = time.time()                     # Starts the timer
    try:                                    # Try block to handle the timeout exception
        message, server = sock.recvfrom(1024)   # Receives the message and server information from the server
        timer = time.time() - timer             # Stops the timer
        msTime = timer * 1000                   # Converts timer to milliseconds
        print(f"Message received from {server}: {message}") # Prints the message we received back from the server 
        print(f"Time for ping: {msTime} ms")                # Prints the time this ping took
        if msTime < minTime:                                # Checks if this was the shortest amount of time
            minTime = msTime
        if msTime > maxTime:                                # Checks if this was the longest amount of time
            maxTime = msTime
        averageTime = averageTime + msTime                  # Adds the time to the averageTime variable

    except:                         # Exception handler for the timeout
        print("Packet lost")        # Lets user know the packet was lost
        lostPackets = lostPackets + 1   # Adds to the lostPackets tracker
        pass                            # Allows us to stop waiting for the message we lost

    
    

averageTime = averageTime / (10 - lostPackets) # Computes the average time (excluding the lost packets)

print(f"Average time: {averageTime}")          # Lets user know the average time taken
print(f"Minimum time: {minTime}")              # Lets user know the minimum time taken
print(f"Maximum time: {maxTime}")              # Lets user know the maximum time taken
print(f"Packets lost: {lostPackets * 10}%")    # Lets user know what percentage of packets were lost
    


