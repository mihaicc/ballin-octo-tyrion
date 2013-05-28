import socket

HOST = '127.0.0.1'
PORT = 40020

client = socket.socket()
client.connect((HOST, PORT))

data = client.recv(1024)
print data
client.close()
