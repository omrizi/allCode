import socket
import struct
import sys
import time
import csv

class multiSocket():
	def __init__(self,multicastGroupAddr,destPort = 10000,isAlive = False):
		self.destPort = destPort 							# destenation port
		self.multicastGroupAddr = multicastGroupAddr     	# Ip addr 
		self.isAlive = isAlive   							# state of the connection 
		#Create the socket 
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) 
		server_address = ('', destPort)						# '' is eth0 witch have ip ...
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(server_address) # binding ip:port
		#self.sock.settimeout(0.0001)
		self.sock.setblocking(False)
		# Tell the operating system to add the socket to the multicast group
		# on all interfaces.
		group = socket.inet_aton(self.multicastGroupAddr)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		try:
			self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		except socket.error:
			print("Err CREATING the socket, Explore it")
			sys.exit()

	def openAndConfSocket(self):
		server_address = ('', destPort)						# '' is eth0 witch have ip ...
		self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		self.sock.bind(server_address) # binding ip:port
		self.sock.settimeout(0.0001)
		# Tell the operating system to add the socket to the multicast group
		# on all interfaces.
		group = socket.inet_aton(self.multicastGroupAddr)
		mreq = struct.pack('4sL', group, socket.INADDR_ANY)
		try:
			self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
		except socket.error:
			print("Err CREATING the socket, Explore it")
			sys.exit()
	def closeSocket(self):
		self.sock.close()
		#
		self.sock.close()
		#
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
		return self.multicastGroupAddr
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
def getLocalTime():
	#
	return time.asctime(time.localtime(time.time()))

ipFile = open('ip.txt','r')
ipList = readMulticastIpFromFile(ipFile)

#open file for writing up and down links
uptimeFile = open('uptimeIP.txt','w+')
multiDict = {} #Create a Dictionary of muplicast IP and Sockets

for sct in ipList:
	IP,DSTPORT = sct.split(":")
	sock1 = multiSocket(IP,int(DSTPORT)) #Create a new object of multiSocket
	multiDict[IP] = sock1 		  		 #Insert the new socket object into the dictionary

# field names - the first raw in thr csv file
fields = ["Multicast ADDR","Connection Status(Up/Down","Change Time"]
# name of csv file
filename = "multicastConnectionStatusReport.csv"
 
# writing to csv file
#first create the file if do not exist with 'w' privledge
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
    # writing the fields
    csvwriter.writerow(fields)
try:
	# Receive/respond loop
	while (True):
		time.sleep(0.1)
		for k,v in multiDict.items():
			#print(v.printSocketDitails())
			#print("Waiting to recive data")
			data = ''
			address = ''
			try:
				data , address = v.getSocket().recvfrom(512) #recvfrom - sample session to check if Up or Down
			except socket.timeout:
				#print("caought socket timeout")
				pass
			except socket.error:
				#print("caought socket error")
				pass
			#print(type(data))
			#print(type(address))
			if(len(data) > 0 and v.getSocketState() == False):
				print("Data is revieved")
				print("data size is {}".format(len(data)))
				v.setSocketState(True)
				print(v.printSocketDitails())
				uptime = getLocalTime()
				uptimeFile.write("IP ADDR : {} \nUpTime is {} \n".format(k,uptime))
				with open(filename, 'a') as csvfile:
				    # creating a csv writer object
				    csvwriter = csv.writer(csvfile)
				    # writing the fields
				    csvwriter.writerow([k,v.getSocketState(),getLocalTime()])
			elif(len(data) > 0 and v.getSocketState() == True):
				print("Data is recieved but connection is already up and running --> {}".format(k))
			elif(len(data) == 0 and v.getSocketState() == True ):
				print("Link is just went down")
				v.setSocketState(False)
				print(v.printSocketDitails())
				uptime = getLocalTime()
				uptimeFile.write("IP ADDR : {} \nDownTime is {} \n".format(k,uptime))
				with open(filename, 'a') as csvfile:
				    # creating a csv writer object
				    csvwriter = csv.writer(csvfile)
				    # writing the fields
				    csvwriter.writerow([k,v.getSocketState(),getLocalTime()])
			elif(len(data) == 0 and v.getSocketState() == False): 
				#print("No data recieved and no link went up")
				pass
except KeyboardInterrupt:
	print("Exiting the server! Good bey")
	#pass
finally:
	for k,v in multiDict.items():
		v.getSocket().close()
	ipFile.close()
	uptimeFile.close()
	sys.exit()