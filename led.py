
from groove.grovepi import *
import time

def init(pin):
	pinMode(pin,"OUTPUT")

def turnOn(pin):
	digitalWrite(pin,1)

def turnOff(pin):
	digitalWrite(pin,0)

pin = 3
init(pin)

while 1:
    turnOnAna(pin)
	subprocess.run(["sendCloud.py",1,1])
	time.sleep(20)
	turnOffAna(pin)
	subprocess.run(["sendCloud.py",0,0])
    time.sleep(20)
	
