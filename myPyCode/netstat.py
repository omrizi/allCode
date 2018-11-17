import time
import subprocess

def printIpSetState(ipSet):
	for items in ipSet:
		print("Ip Addr : {}    Connection State : {} ".format(items[0],items[1]))
		#print(items[0])
		#print(items[1])

def createIpSet(ipFile):
	ipSet = set()
	ipFile = ipFile.read().splitlines()
	for lines in ipFile:
		s = set()
		s.add(lines),s.add(False)
		ipSet.add(s)
		#print(ipSet)	
	return ipSet

def getLocalTime():
	return time.asctime(time.localtime(time.time()))



#each cell in ipSet is a tuple contain (ip address,State of the link(Up - True, Down - False))
#Set do not allow duplicate values hence it is better here then a list
ipSet = set()

## read file text by lines
file = open('ip.txt','r')

ipSet = createIpSet(file)
printIpSetState(ipSet)

#running netstat in a sub process and save the output into output arg
output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()

#itarate throw the IP list seeking for established sockets
for IP in ipSet:
	print("INTO IPSET FOR, IP TO CHECK IS")
	print(IP[0]),print(type(IP)),print(type(IP[1]))
	for lines in output[0].split():
#		print("INTO OUTPUT FOR")
		#checking if IP exist and state = established
#		if(str(IP[0]) in str(lines[0]) and "ESTABLISHED" in str(lines[0])):
		if(str(IP[0]) in str(lines)):
			print("match line found {}".format(lines))	
			if (IP[1] == False):
				print("IF TRUE FOR {}".format(IP[1]))
				uptime = getLocalTime()
				print("Uptime is {} ".format(uptime))
				IP.update(IP[0],True)
			else:
				uptime = getLocalTime()
				print("Downtime is {} ".format(uptime))
				IP.update(IP[0],False)

printIpSetState(ipSet)
