import time
from grovepi import * 

pin = 3 

pinMode(pin,"OUTPUT")
time.sleep(1)
i = 0

analogWrite(pin,0)
time.sleep(3)
stop = True
while stop:
    for i in range(0,256,5) : 
		try : 
			analogWrite(pin,i)
			time.sleep(0.02)
		except KeyboardInterrupt :
			stop = False
		except : 
			print("Erreur")

		
