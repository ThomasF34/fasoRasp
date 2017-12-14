from groove.grovepi import *
import time

i=4
while 1:
	pinMode(i,"OUTPUT")
	digitalWrite(i,1)
	time.sleep(0.0025)
	digitalWrite(i,0)
	time.sleep(0.02)
	pinMode(i,"INPUT")
	print(analogRead(i))
