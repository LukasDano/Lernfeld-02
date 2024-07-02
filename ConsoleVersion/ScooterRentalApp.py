import datetime

gebuehr = 1
pricePerMinute = 0.10

ausleihZeitpunkt = [0, 0, 0]
rueckgabeZeitpunkt = [0, 0, 0]
reservierungsZeitpunkt = [0, 0]

scooterAusgeliehen = False
scooterReserviert = False

def getCurrentTimeStamp():
    now = datetime.datetime.now()
    hours = int(now.strftime("%H"))
    minutes = int(now.strftime("%M"))
    seconds = int(now.strftime("%S"))

    return [hours, minutes, seconds]

def getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt):

    differenz = [0, 0]

    differenz[0] = spaetererZeitpunkt[0] - fruehererZeitpunkt[0]
    differenz[1] = spaetererZeitpunkt[1] - fruehererZeitpunkt[1]

    #print("Differenz:", differenz)
    return differenz

def getPrice(timeInMinutes):
    price = timeInMinutes * pricePerMinute + gebuehr
    formattedPrice = "{:.2f}".format(price)
    return formattedPrice

def scooterAusleihen():
    global scooterAusgeliehen, scooterReserviert
    if scooterReserviert == True:
        scooterReserviert = False
        print("Du hast eine Reservierung")
        print("Dein reservierter Scooter steht dir jetzt zur Verfuegung")

    global scooterAusgeliehen
    scooterAusgeliehen = True

    print("\n\n")
    print("- Scooter Ausleihen -")
    print("\n")

    aktuelleZeit = getCurrentTimeStamp()

    ausleihZeitpunkt[0] = aktuelleZeit[0]
    ausleihZeitpunkt[1] = aktuelleZeit[1]
    ausleihZeitpunkt[2] = aktuelleZeit[2]

    formattedPricePerMinute = "{:.2f}".format(pricePerMinute)

    print(f"Scooter ausgeliehen um: {ausleihZeitpunkt[0]}:{ausleihZeitpunkt[1]} Uhr")
    print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {gebuehr}€")
    print(f"Der Preis pro Angefangene Minute beträgt {formattedPricePerMinute}€")

    

def datenZurAktuellenFahrt():
    if scooterAusgeliehen == False:
        print("Es ist keine Scooter ausgeliehen!")
        return
    
    print("\n\n")
    print("- Die Daten zu deiner aktuellen Fahrt -")
    print("\n")

    fruehererZeitpunkt = ausleihZeitpunkt
    spaetererZeitpunkt = getCurrentTimeStamp()

    timeDifference = getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt)
    hours = timeDifference[0]
    minutes = timeDifference[1]
    seconds = getCurrentTimeStamp()[2]

    print(f"Ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")
    #print("Seconds", seconds)

    timeInMinutes = hours * 60 + minutes
    if seconds != 0:
        timeInMinutes += 1

    price = getPrice(timeInMinutes)
    print(f"Aktueller Preis dieser Fahrt: {price}€")

def scooterZurueckgeben():
    global scooterAusgeliehen

    if scooterAusgeliehen == False:
        print("Es ist keine Scooter ausgeliehen!")
        return
    
    rueckgabeZeitpunkt = getCurrentTimeStamp()

    scooterAusgeliehen = False

    print("\n\n")
    print("- Scooter Zurueckgeben -")
    print("\n")

    print(f"Scooter zurueckgeben am: {rueckgabeZeitpunkt[0]}:{rueckgabeZeitpunkt[1]} Uhr")

    timeDifference = getTimeDifferance(ausleihZeitpunkt, rueckgabeZeitpunkt)
    hours = timeDifference[0]
    minutes = timeDifference[1]
    seconds = getCurrentTimeStamp()[2]

    print(f"Insgesamt ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")
    #print("Seconds", seconds)

    timeInMinutes = hours * 60 + minutes
    
    if seconds != 0:
        timeInMinutes += 1

    price = getPrice(timeInMinutes)
    print(f"Preis dieser Fahrt: {price}€")

def scooterReservieren():
    global scooterReserviert, reservierungsZeitpunkt
    scooterReserviert = True

    reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
    reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")
    
    reservierungsZeitpunkt = [int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)]

    if scooterReserviert == True:
        print("Du hast erfolgreich einen Scooter reserviert!")

def uebersichtScooter():
    
    if scooterReserviert == True:
        print("Du hast einen Scooter reserviert")
        print("Deine Reservierung beginnt um:", reservierungsZeitpunkt[0], ":", reservierungsZeitpunkt[1])
        return
    
    print("Du hast keinen Scooter reserviert")
