import socket

host = socket.gethostname()
port = 1234

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
s.sendall("Hello world!\n")

data = s.recv(1024)

s.close()

print "Received: %r" % data
