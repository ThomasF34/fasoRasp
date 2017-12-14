import grovepi
import os
import subprocess
import time
import math
import bandeauLed
import captCard

capt = 4  # capteur de température sur le port 4 
bandeau = 3 #Bandeau de led sur le port 3 
sleep = 5
grovepi.pinMode(bandeau,"OUTPUT")

while True:
	try:
		[temp,humidity] = grovepi.dht(capt,0)
		wd = os.getcwd()
		print(humidity)
		print(temp)

		bandeauLed.start(bandeau)
		#card = captCard.readHeartRate(6,30)
		card = 0
		bandeauLed.stop(bandeau)


		if humidity <= 0 or temp <= 0 :
			print("Erreur de lecture")
			sleep = 10
		elif not math.isnan(temp) :
			subprocess.run([wd+"/sendCloud.py",str(card),str(temp),str(humidity)])
			sleep = 20
		else :
			print("Error")
			sleep = 20
		time.sleep(sleep)

	except IOError:
		print ("Error")
		time.sleep(sleep)
