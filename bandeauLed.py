import time
from grovepi import *

def start(pin) :
	analogWrite(pin,0)
	for i in range(0,256,5) :
		try:
			analogWrite(pin,i)
			time.sleep(0.02)
		except IOError:
			print("Erreur")

def stop(pin) :
	for i in range(256,0,-5) :
		try:
			analogWrite(pin,i)
			time.sleep(0.02)
		except IOError:
			print("Erreur")
	analogWrite(pin,0)

