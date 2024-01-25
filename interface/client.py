
import socket

# Create a socket
c = socket.socket()
print("socket created")

# Bind the socket to a port
c.connect(("192.168.90.234", 9999))
print ("connection established with server")


while True:
  message = input("You :")
  c.send(bytes(message, 'utf-8'))
  print("Message sent")
  print("anjali:",c.recv(1024).decode())