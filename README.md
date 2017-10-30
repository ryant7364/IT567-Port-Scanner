# IT567-Port-Scanner


My Basic Port Scanner

I wrote this scanner tool to fulfil an assignment for school.

Feel free to use, copy, or modify this program for education or just for fun!

You may want to start by just running the program.
When you do you will get the following prompt:

	missing arguments......

	Usage - ./Port_Scan.py [Target-IP] [Type] [First Port] [Last Port]
	Type of Scan - 'U' = UDP, 'T' = TCP, 'B' = Both
	Enter a single IP address or a list separated only by commas no spaces ie: IP,IP,IP				
	Example - ./Port_Scan.py 192.168.14.2 U 1 500
	This Example will scan UDP ports 1 through 500 on 192.168.14.2
	Example - ./Port_Scan.py 192.168.14.1,192.168.14.36,192.168.14.101 B 50 500
	This Example will scan Both UDP and TCP ports 50 through 500 on all three addresses
	
