#!/usr/bin/python

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
import time
import sys

# This section gives help to the User if the input doesn't meet the programs input requirements.
if len(sys.argv) != 5:
	print "  "
	print "missing arguments......"
	print "  "
	print "Usage - ./Port_Scan.py [Target-IP] [Type] [First Port] [Last Port]"
	print "Type of Scan - 'U' = UDP, 'T' = TCP, 'B' = Both"
	print "Enter a single IP address or a list separated only by commas no spaces ie: IP,IP,IP"					
	print "Example - ./Port_Scan.py 192.168.14.2 U 1 500"
	print "This Example will scan UDP ports 1 through 500 on 192.168.14.2"
	print "Example - ./Port_Scan.py 192.168.14.1,192.168.14.36,192.168.14.101 B 50 500"
	print "This Example will scan Both UDP and TCP ports 50 through 500 on all three addresses"
	print "  "
	sys.exit()
else:
# This section sets all input values to variables
	addrs = sys.argv[1]
	type = sys.argv[2]
	sp = int(sys.argv[3])
	fp = int(sys.argv[4])

	if type == 'B':
	# This section is used when Both UDP and TCP results are desired.
		for addr in addrs.split(','):
			print "Host  "+ str(addr)
			for port in range(sp,fp):
				ureply = sr1(IP(dst=addr)/UDP(dport=port),timeout=5,verbose =0)
				treply = sr1(IP(dst=addr)/TCP(dport=port),timeout=1,verbose =0)
				if ureply == None:
					print "UDP  "+ str(port)
				else:
					pass

				if treply == None:
					pass
				else:
					if int(treply[TCP].flags) == 18:
						print "TCP  "+ str(port)
					else:
						pass
	else:
		pass
		
	if type == 'T':
	# This section is used when just TCP results are desired.
		for addr in addrs.split(','):
			print "Host  "+ str(addr)
			for port in range(sp,fp):
				reply = sr1(IP(dst=addr)/TCP(dport=port),timeout=1,verbose =0)
				if reply == None:
					pass
				else:
					if int(reply[TCP].flags) == 18:
						print "TCP  "+ str(port)
					else:
						pass
	else:
		pass
					
	if type == 'U':
	# This section is used when just UDP results are desired.
		for addr in addrs.split(','):
			print "Host  "+ str(addr)
			for port in range(sp,fp):
				reply = sr1(IP(dst=addr)/UDP(dport=port),timeout=5,verbose =0)
				if reply == None:
					print "UDP  "+ str(port)
				else:
					pass
	else:
		pass

	''''