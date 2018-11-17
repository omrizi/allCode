import time
import subprocess

def printIpSetState(ipList):
	for items in ipList:
		print("Ip Addr : {}    Connection State : {} ".format(items[0],items[1]))
		#print(items[0])
		#print(items[1])

def createIpSet(ipFile):
	ipFile = ipFile.read().splitlines()
	ipList = []
	for lines in ipFile:
		s1 = set()
		s1.add(lines),s1.add(False)
		ipList.append(s1)
		#print(ipSet)	
	return ipList

def getLocalTime():
	return time.asctime(time.localtime(time.time()))



#each cell in ipSet is a tuple contain (ip address,State of the link(Up - True, Down - False))
#Set do not allow duplicate values hence it is better here then a list
ipList = []

## read file text by lines
file = open('ip.txt','r')

ipList = createIpSet(file)
printIpSetState(ipList)