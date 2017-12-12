#!/usr/bin/env python3

import http.client, urllib
import sys
import time
sleep = 20 # how many seconds to sleep between posts to the channel
key = 'Y0D6SD5C247DXZIW'  # Thingspeak channel to update

args = sys.argv
print(args)

try :
	params = urllib.parse.urlencode({'field2': float(args[1]), 'field3': float(args[2]) , 'key':key }) 
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = http.client.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	response = conn.getresponse()
	print(response.status)
	print(response.reason)
	data = response.read()
	conn.close()
except ValueError :
	print("Attention le ième argument n'est pas un entier")
except :
	print("Error in sending")
