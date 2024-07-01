import datetime

gebühr = 1
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
    differenz = [0, 0, 0]
    
    differenz[0] = zeitpunkt2[0] - zeitpunkt1[0]
    differenz[1] = zeitpunkt2[1] - zeitpunkt1[1]
    differenz[2] = zeitpunkt2[2] - zeitpunkt1[2]

    print("Differenz:", differenz)
    return differenz

def getPrice(timeInMinutes):
    price = timeInMinutes * pricePerMinute + gebühr
    formattedPrice = "{:.2f}".format(price)
    return formattedPrice

def scooterAusleihen():
    print("\n\n")
    print("- Scooter Ausleihen -")
    print("\n")

    aktuelleZeit = getCurrentTimeStamp()

    ausleihZeitpunkt[0] = aktuelleZeit[0]
    ausleihZeitpunkt[1] = aktuelleZeit[1]
    ausleihZeitpunkt[2] = aktuelleZeit[2]

    print(f"Scooter ausgeliehen um: {ausleihZeitpunkt[0]} Stunden {ausleihZeitpunkt[1]} Minuten")
    print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {gebühr}€")
    print(f"Der Preis pro Angefangene Minute beträgt {pricePerMinute}€")

    scooterAusgeliehen = True

def datenZurAktuellenFahrt():
    print("\n\n")
    print("- Die Daten zu deiner aktuellen Fahrt -")
    print("\n")

    timeDifference = getTimeDifferance()
    hours = timeDifference[0]
    minutes = timeDifference[1]
    seconds = timeDifference[2]

    if timeDifference[0] < 0:
        print("Bisher wurde noch kein Scooter ausgeliehen!")
        return

    print(f"Ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")

    timeInMinutes = hours * 60 + minutes

    price = getPrice(timeInMinutes)
    print(f"Aktueller Preis dieser Fahrt: {price}€")