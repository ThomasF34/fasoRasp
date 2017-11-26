
from groove.grovepi import *
import time

def init(pin):
        pinMode(pin,"OUTPUT")

def turnOn(pin):
       digitalWrite(pin,1)

def turnOff(pin):
       digitalWrite(pin,0)

pin = 2
init(pin)
while 1:
	turnOn(pin)
	time.sleep(0.5)
	turnOff(pin)
	time.sleep(0.5)
