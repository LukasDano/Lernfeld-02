import datetime

gebuehr = 1
pricePerMinute = 0.10

ausleihZeitpunkt = [0, 0, 0]
scooterAusgeliehen = False

def getCurrentTimeStamp():
    hours = datetime.datetime.now().strftime("%H")
    minutes = datetime.datetime.now().strftime("%M")
    seconds = datetime.datetime.now().strftime("%S")
    
    aktuellerZeitpunkt = [int(hours), int(minutes), int(seconds)]
    return aktuellerZeitpunkt

def getTimeDifferance():

    zeitpunkt1 = ausleihZeitpunkt
    zeitpunkt2 = getCurrentTimeStamp()
    differenz = [0, 0]
    
    differenz[0] = zeitpunkt2[0] - zeitpunkt1[0]
    differenz[1] = zeitpunkt2[1] - zeitpunkt1[1]

    print("Differenz:", differenz)
    return differenz

def getPrice(timeInMinutes):
    price = timeInMinutes * pricePerMinute + gebuehr
    formattedPrice = "{:.2f}".format(price)
    return formattedPrice

def scooterAusleihen():
    global scooterAusgeliehen
    scooterAusgeliehen = True

    print("\n\n")
    print("- Scooter Ausleihen -")
    print("\n")

    aktuelleZeit = getCurrentTimeStamp()

    ausleihZeitpunkt[0] = aktuelleZeit[0]
    ausleihZeitpunkt[1] = aktuelleZeit[1]
    ausleihZeitpunkt[2] = aktuelleZeit[2]

    formattedgebuehr = "{:.2f}".format(gebuehr)

    print(f"Scooter ausgeliehen um: {ausleihZeitpunkt[0]}:{ausleihZeitpunkt[1]} Uhr")
    print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {formattedgebuehr}€")
    print(f"Der Preis pro Angefangene Minute beträgt {pricePerMinute}€")

    

def datenZurAktuellenFahrt():
    if scooterAusgeliehen == False:
        print("Bisher wurde noch kein Scooter ausgeliehen!")
        return
    
    print("\n\n")
    print("- Die Daten zu deiner aktuellen Fahrt -")
    print("\n")

    timeDifference = getTimeDifferance()
    hours = timeDifference[0]
    minutes = timeDifference[1]
    seconds = getCurrentTimeStamp()[2]

    print(f"Ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")

    timeInMinutes = hours * 60 + minutes
    if seconds != 0:
        timeInMinutes += 1

    price = getPrice(timeInMinutes)
    print(f"Aktueller Preis dieser Fahrt: {price}€")