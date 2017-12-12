#!/usr/bin/env python3

from grovepi import *
import time
import subprocess
import os

def init(pin):
	pinMode(pin,"OUTPUT")

def turnOn(pin):
	digitalWrite(pin,1)

def turnOff(pin):
	digitalWrite(pin,0)
pin = 3
init(pin)
while 1:
	turnOn(pin)
	time.sleep(2)
	turnOff(pin)
	time.sleep(2)
time.sleep(20)
