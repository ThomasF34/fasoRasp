import time

def moyenne(liste): 
    somme = 0
    for i in liste:
        somme = somme + i
    moyenne = somme/(len(liste))
    return moyenne

def ecartMoyen(liste):
    moy = moyenne(liste)
    sEcart = 0
    for i in liste:
        sEcart = sEcart + abs(moy-i)
    eMoyen = sEcart/(len(liste))
    return eMoyen

def analyse(liste):
    ecart = liste[len(liste)-1] - moyenne(liste)
    #print("ecart : "+str(ecart))
    if ecart > ecartMoyen(liste):
        #print("ecartMoy : "+str(ecartMoyen(liste)))
        return True
    else:
        #print("ecartMoy : "+str(ecartMoyen(liste)))
        return False
    
def simulation(liste):
    led = ""
    if analyse(liste) == True:
        led = "END"    
    
    return led
               
def decalerListe(x,sliste): #rajoute la nouvelle valeur a la liste et supprime la premiere et decale tout si liste pleine
    if len(sliste) == 20:
        sliste = sliste[1:20]
    sliste.append(x)
    return sliste
        
def main():
    li = [60.00,59.00,61.00,60.00,59.00,56.00,59.00,61.00,58.00,58.00,58.00,57.00,59.00,56.00,60.00,63.00,61.00,60.00,61.00,61.00,60.00,60.00,60.00,60.00,61.00,60.00,58.00,65.00,60.00,61.00,62.00,60.00,58.00,60.00,60.00,60.00,59.00,55.00,57.00,54.00,54.00,54.00,54.00,55.00,55.00,59.00,60.00,60.00,58.00,56.00,56.00,55.00,55.00,55.00,55.00,54.00,53.00,52.00,53.00,52.00,52.00,53.00,53.00,52.00,52.00,53.00,59.00,63.00,53.00,57.00,57.00,54.00,55.00,56.00,56.00,56.00,56.00,57.00,56.00,56.00,57.00,55.00,53.00,54.00]
    sli = []
    led = ""
    for i in range(0,len(li)-1) :
        time.sleep(0.1)
        sli = decalerListe(li[i],sli)
        #print(sli)
        if i > (len(li)-24):
            precLed = led
            #if ( (led==END) and sli[len(sli)-1] < sli[len(sli)-2])
            led = simulation(sli)
            if (precLed=="END") and ( (sli[len(sli)-1]) < (sli[len(sli)-2]) ):
                led = "LED"
            elif precLed == "LED" or precLed == "DONE" :
                led = "DONE"
            print("rythme cardiaque : " + str(sli[len(sli)-1]) +"     " + led)
        else:
            print("rythme cardiaque : " + str(sli[len(sli)-1]) +"     OFF")
            
main()
    


        