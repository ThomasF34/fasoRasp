import time
from grovepi import *

def start(pin) : 
	pinMode(pin,"OUTPUT")
	time.sleep(1)
	analogWrite(pin,0)
	time.sleep(2)
	for i in range(0,256,5) :
		try:
			analogWrite(pin,i)
			time.sleep(0.02)
		except KeyboardInterrupt :
			stop = False
		except :
			print("Erreur")
	
def stop(pin) :
	pinMode(pin,"OUTPUT")
	time.sleep(1)
	for i in range(256,0,-5) :
		try:
			analogWrite(pin,i)
			time.sleep(0.02)
		except KeyboardInterrupt :
			stop = False
		except :
			print("Erreur")

