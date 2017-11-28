import http.client, urllib
import time
sleep = 20 # how many seconds to sleep between posts to the channel
key = 'Y0D6SD5C247DXZIW'  # Thingspeak channel to update

for i in range(10):
	params = urllib.urlencode({'field1': i, 'field2': i+1 , 'key':key }) 
	headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		print(i)
		print(response.status)
		print(response.reason)
		data = response.read()
		conn.close()
	except:
		print("connection failed")
	time.sleep(sleep) 