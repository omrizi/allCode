import time
import subprocess

def printIpSetState(ipList):
	for items in ipList:
		print("Ip Addr : {} Connection State : {} ".format(list(items)[1],list(items)[0]))
def createIpSet(ipFile):
	ipList = []
	ipFile = ipFile.read().splitlines()
	for lines in ipFile:
		s = set()
		s.add(lines)
		s.add(False)
		ipList.append(s)
	print(ipList)	
	return ipList
def getLocalTime():
	#
	return time.asctime(time.localtime(time.time()))
def netstatIpParse():
	
	output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
	#print(type(str(output[0]).split(" ")))
	IPS = list(set(str(output[0]).split(" ")))
	IPONLY = []
	s = set()
	for items in IPS:
		if(items[0:1:1].isdigit() == True and (len(items) > 10) and int(items[0:1:1]) > 0 ):
			IPONLY.append(items.split(":"))
	for items in IPONLY:
		s.add(items[0])
	IPONLY = list(s)
	return IPONLY


#each cell in ipSet is a tuple contain (ip address,State of the link(Up - True, Down - False))
#Set do not allow duplicate values hence it is better here then a list
ipList = []

## read file text by lines
ipFile = open('ip.txt','r')
#open file for writing up and down links
uptimeFile = open('uptimeIP.txt','w+')

#read from ip.txt the IPS into a list
ipList = createIpSet(ipFile)
printIpSetState(ipList)

#read into netstatIp all the valid IP'S
netstatIp = netstatIpParse()
print(ipList)


#itarate throw the IP list seeking for established sockets
for num in range(5):
#while(True):
	netstatIp = netstatIpParse()
	for IP in ipList:
		#print("INTO IPSET FOR, IP TO CHECK IS")
		for lines in netstatIp:
			#checking if IP exist and state = established
			if(str(list(IP)[1]) == lines):
				ipp = list(IP)[1]
	#			print("match line found {}".format(lines))	
				if (list(IP)[0] == False):
					print("IF TRUE FOR {}".format(list(IP)[1]))
					uptime = getLocalTime()
					print("Uptime is {} ".format(uptime))
					IP.clear()
					IP.add(True)
					IP.add(ipp)
					uptimeFile.write("IP ADDR : {} \nUpTime is {} \n".format(list(IP)[1],uptime))
					printIpSetState(ipList)
				elif((list(IP)[0]) == True and(str(list(IP)[1]) in lines)) :
	#				print("UP AND RUNNING")
	#				sleep x sec
					time.sleep(0)
					continue
				else:
					uptime = getLocalTime()
					print("Downtime is {} ".format(uptime))
					IP.add(False),IP.add(ipp)
					uptimeFile.write("IP ADDR : {} \nDownTime is {} \n".format(list(IP)[1],uptime))
					printIpSetState(ipList)

print(ipList)
ipFile.close()
uptimeFile.close()