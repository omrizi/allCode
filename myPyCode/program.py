## read file text by lines
A = open('ip.txt','r')
IP = A.readlines()
IP = [x.strip() for x in IP]

##open cmd
subprocess.call('start',shell=True) 

##check the localtime
import time;
localtime = time.asctime( time.localtime(time.time()) )
print "Local current time :", localtime

---
import subprocess
output = subprocess.Popen(['netstat', '-ano'], stdout=subprocess.PIPE).communicate()
valid_lines = [ line for line in output[0].split('\r\n') if  in line ]
## valid_lines = [ line for line in output[0].split('\r\n') if '151.101.112.166:443' in line ]
valid_lines

 
valid_lines = [ line for line in output[0].split('\r\n') if ':80' in line ]