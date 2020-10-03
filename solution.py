#import socket module
from socket import *
# In order to terminate the program
import sys 

def webServer(port=13331):
   serverSocket = socket(AF_INET, SOCK_STREAM)

   #Prepare a sever socket
   hostAddress = '192.168.1.20'
   serverSocket.bind((hostAddress, port))
   serverSocket.listen(1) 

   while True:
       #Establish the connection
       print('Ready to serve...')
       connectionSocket, addr = serverSocket.accept()
       try:
           message = connectionSocket.recv(1024)
           filename = message.split()[1]
           f = open(filename[1:])
           outputdata = f.read()
           #Send one HTTP header line into socket
	   connectionSocket.send('\nHTTP/1.1 200 OK\n'.encode())
           #Send the content of the requested file to the client
           for i in range(0, len(outputdata)):
               connectionSocket.send(outputdata[i].encode())
           connectionSocket.send("\r\n".encode())
           connectionSocket.close()
       except IOError:
           #Send response message for file not found (404)
           connectionSocket.send('\nHTTP/1.1 404 Not Found\n'.encode())
	   connectionSocket.send('\n404 Not Found!\n'.encode())
           #Close client socket
           connectionSocket.close()
   serverSocket.close()

   # Terminate the program after sending the corresponding data
   sys.exit()

if __name__ == "__main__":
   webServer(13331)

