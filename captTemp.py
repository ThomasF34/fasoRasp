import grovepi
import os
import subprocess
import time
import math
import bandeauLed
 
capt = 4  # The Sensor goes on digital port 4.
bandeau = 3

while True:
    try:
        # This example uses the blue colored sensor. 
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(capt,0)
		wd = os.getcwd()
    	print(humidity)
    	print(temp)
    	if not math.isnan(temp)  :
			subprocess.run([wd+"/sendCloud.py",str(temp),str(humidity)])
			bandeauLed.start(3)
        	time.sleep(20)
			bandeauLed.stop(3)
    	else :
        	print("not a number")
        	time.sleep(10)
    except IOError:
        print ("Error")
    except : 
        print ("Error")
    
