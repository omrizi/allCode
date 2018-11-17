import sys



ipList = []
ipFile = open('ip.txt','r')

ipFile = ipFile.read().splitlines()
#print("{}".format(ipFile))

for line in ipFile:
	print("SPLIT LINE IS {}".format((line.split(":"))[0]))
	ip,prt = (line.split(":"))
	print("IP ADDR {} ::: DST PORT {}".format(ip,prt))
