import socket

s1 = socket.socket()
host = socket.gethostname()
port = 12345
s1.bind((host,port))
print("type is {}".format(type(s1)))
print("{}".format(s1))
print("hostName is {}".format(host))

