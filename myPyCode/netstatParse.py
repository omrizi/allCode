import time
import subprocess

def netstatIpParse():
	output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
	print(type(output))
	#print(type(str(output[0]).split(" ")))
	IPS = list(set(str(output[0]).split(" ")))
	print(type(IPS))
	IPONLY = []
	s = set()
	for items in IPS:
		if(items[0:1:1].isdigit() == True and (len(items) > 10) and int(items[0:1:1]) > 0 ):
			IPONLY.append(items.split(":"))
	for items in IPONLY:
		s.add(items[0])
	IPONLY = list(s)
	return IPONLY

netIp = netstatIpParse()
print(netIp)
#while(True):

for ip in netIp:
	print(ip)# --> IPS from netstat list
