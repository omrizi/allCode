import socket
import struct
import sys
import time

def getLocalTime():
	#
	return time.asctime(time.localtime(time.time()))

#ip = input("enter ip addr")
#port = input("enter port")
message = 'd'
#multicastGroup = (ip,int(10000))
multicastGroup = ('224.3.29.72',20000)

#Create datagram socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.settimeout(0)
ttl = struct.pack('b',1)
sock.setsockopt(socket.IPPROTO_IP,socket.IP_MULTICAST_TTL,ttl)

#send data to multicast group
#while(True):
print("Start sending data")
for i in range(20000000):
	sent = sock.sendto(bytes(512),multicastGroup)
	print("{}".format(sent))

time.sleep(60)
for i in range(2):
	sent = sock.sendto(bytes(512),multicastGroup)
	print("{}".format(sent))
print("END OF THE ROAD FOR YTOU")
print("FINISHED AT {}".format(getLocalTime()))