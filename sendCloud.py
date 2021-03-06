#!/usr/bin/env python3

import http.client, urllib
import sys
import time

key = 'Y0D6SD5C247DXZIW'  # Clé de la chaine Thingspeak

args = sys.argv
print(args)

try :
	params = urllib.parse.urlencode({'field1':float(args[1]),'field2': float(args[2]), 'field3': float(args[3]),'key':key }) 
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = http.client.HTTPConnection("api.thingspeak.com:80")
	conn.request("POST", "/update", params, headers)
	#On effectue la requete HTTP aupres de ThingSpeak 
	response = conn.getresponse()
	print(response.status)
	print(response.reason)
	#Reason et Status permettront de savoir comment l'envoi s'est passé.
	data = response.read()
	conn.close()
except ValueError :
	print("Attention le ième argument n'est pas un entier")
except :
	print("Error in sending")
