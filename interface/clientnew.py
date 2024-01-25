import socket
s=socket.socket()
print("Socket created")
s.bind(("192.168.97.234",9999))
s.listen(3)
print("Waiting for connections")

c,addr=s.accept()
while True:
    name=c.recv(1024).decode()
    # print("Connected with ",addr,name)
    print("Aashish: ",name)
    msg=input("Your msg:")
    c.send(bytes(msg,'utf-8')) 
print("successfully")