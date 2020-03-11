#import socket module
from socket import *

serverPort=8080
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print ('the web server is running on port: ', serverPort)
while 1:
  #Establish the connection
  print ('Ready to serve...')
  connectionSocket, addr = serverSocket.accept()
  try:
    message = connectionSocket.recv(4096)
    filename = message.split()[1]
    f = open(filename[1:])
    outputdata = f.read()
    #print outputdata
    #Send one HTTP header line into socket
    connectionSocket.send("HTTP/1.0 200 OK \r\n\r\n")
    #Send the content of the requested file to the client
    for i in range(0, len(outputdata)):
      connectionSocket.send(outputdata[i])
    connectionSocket.close()
  except IOError:
    connectionSocket.send("HTTP/1.0 404 FILE NOT FOUND \r\n\r\n")
    connectionSocket.send("Page Not Found")
  #Send response message for file not found
  connectionSocket.close()