import socket
import struct
import sys

class multiSocket():
	def __init__(self,multicastGroup,destPort,isAlive = False):
		self.destPort = destPort # destenation port
		self.multicastGroup = multicastGroup     # Ip addr 
		self.isAlive = isAlive   # state of the connection 

		#Create the socket 
		#self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		server_address = ('', 10000)

		# Bind to the server address
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(server_address)
		self.sock.settimeout(2)


		# Tell the operating system to add the socket to the multicast group
		# on all interfaces.
		group = socket.inet_aton(self.multicastGroup)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)


	def printSocketDitails(self):
		print("Ip addr is {}".format(self.getmulticastGroup()))
		print("Dest port is {}".format(self.getDestPort()))
		print("State of the connection is {} ".format(self.getSocketState()))

	# if True = connection  Up, False = Down
	def getSocketState(self):
		return self.isAlive
		#
	def getDestPort(self):
		return self.destPort
		#

	def getmulticastGroup(self):
		return self.multicastGroup
		#

	def getSocket(self):
		return self.sock
		#
	def setmulticastGroup(self,multicastGroup):
		self.multicastGroup = multicastGroup
		#

	def setDestPort(self,destPort):
		self.destPort = destPort
		#

	def setSocketState(self,isAlive):
		self.isAlive = isAlive
		#

def readMulticastIpFromFile(ipFile):
	ipList = []
	ipFile = ipFile.read().splitlines()
	for lines in ipFile:
		ipList.append(lines)
	return ipList


ipFile = open('ip.txt','r')
ipList = readMulticastIpFromFile(ipFile)
#print(ipList)

multiDict = {} #Create a Dictionary of muplicast IP and Sockets

for IP in ipList:
	sock1 = multiSocket(IP,"10000") #Create a new object of multiSocket
	multiDict[IP] = sock1 			#Insert the new socket object into the dictionary



# Receive/respond loop
while (True):
	for k,v in multiDict.items():
		print(v.printSocketDitails())
		print("Waiting to recive data")
		data = ''
		address = ''
		try:
			print("into try")
			#recvfrom - take sample from the connection to check if Up Down
			data , address = v.getSocket().recvfrom(1024)
		except socket.timeout:
			print("caought socket timeout")
		except socket.error:
			print("caought socket error")
			continue
		print(type(data))
		print(type(address))
		if(len(data) > 0 and v.getSocketState() == False):
			print("Data is revieved")
			v.setSocketState(True)
		elif(len(data) > 0 and v.getSocketState() == True):
			print("Data is recieved but connection is already up and running")
		else: print("No data recieved")
		

		#if(v.getSocket.listen(2) == True and v.getSocketState() == False):
			#print("{}:{} is Up and running".format(k,v.getDestPort))
			#v.setSocketState(True)
	#	elif(v.getSocket.listen(2) == True and v.getSocketState() == True):
	#		continue
	#	elif(v.getSocket.listen(2) == False and v.getSocketState() == False):




