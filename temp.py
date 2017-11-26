from groove.grovepi import *

pin="A1"
pinMode(pin,"INPUT")
print(analogRead(pin))
