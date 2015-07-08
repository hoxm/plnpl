import socket

#host = socket.gethostname()
host = "128.224.158.229"
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    data = raw_input("$ ")
    if data != None:
        s.sendall(data + "\n")
    if data == 'exit':
        break

#data = s.recv(1024)
#print "Received: %r" % data

s.close()

