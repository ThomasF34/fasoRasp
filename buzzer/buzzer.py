import grove *
import time *

int buzzer = 3 # connect the I/O pin on the buzzer to this
pinMode (buzzer, OUTPUT)

def TurnOn ():
    for i in range(0,10):
        digitalWrite (buzzer, LOW) # Turn buzzer ON
        delay (1500) # Le buzzer reste allumé pendant 3 secondes
        digitalWrite (buzzer, HIGH) # turn buzzer OFF
        delay (200)  #Le buzzer s'etteind 2 secondes
            
