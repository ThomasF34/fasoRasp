
from groove.grovepi import *
import time

def init(pin):
        pinMode(pin,"OUTPUT")

def turnOn(pin):
       digitalWrite(pin,1)

def turnOff(pin):
       digitalWrite(pin,0)

def turnOnAna(pin):
    analogWrite(pin,1024)

def turnOffAna(pin):
    analogWrite(pin,0) 

pin = 14
init(pin)
while 1:
	turnOnAna(pin)
	time.sleep(0.5)
	turnOffAna(pin)
	time.sleep(0.5)
