import datetime
from datetime import *
import ScooterClass

scooter = ScooterClass.Scooter

GEBUEHR = 1
PRICE_PER_MINUTE = 0.10

scooter_list = []
ausgeliehene_scooter = []

for i in range(10):
    scooter_for_list = scooter(i + 1)
    scooter_list.append(scooter_for_list)

def getScooterById(id):
    for scooter in scooter_list:
        if scooter.getId() == id:
            return scooter
    print("Keinen Scooter mit dieser Id gefunden.")

def getCurrentTimeStamp():
    now = datetime.now()
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
    price = timeInMinutes * PRICE_PER_MINUTE + GEBUEHR
    formattedPrice = "{:.2f}".format(price)
    return formattedPrice

def scooterAusleihen():
    for scooter in scooter_list:
        if scooter.getScooterReserviert():
            selected_scooter = scooter
            selected_scooter.setScooterReserviert(False)
            ausgeliehene_scooter.remove(selected_scooter)
            print("Reservierter Scooter erfolgreich ausgeliehen.")
            break
        elif not scooter.getScooterAusgeliehen():
            selected_scooter = scooter
            break
            #print(f"Der erste verfügbare Scooter hat die ID: {scooter.id}")
        else:
            print("Kein verfügbarer Scooter gefunden.")

    print("\n\n")
    print("- Scooter Ausleihen -")
    print("\n")

    aktuelleZeit = getCurrentTimeStamp()
    ausleihZeitpunkt = [aktuelleZeit[0], aktuelleZeit[1], aktuelleZeit[2]]
    selected_scooter.setAusleihZeitpunkt(ausleihZeitpunkt)

    formattedPricePerMinute = "{:.2f}".format(PRICE_PER_MINUTE)
    ausleihZeitpunkt = 	selected_scooter.getAusleihZeitpunkt()

    print(f"Du hast den Scooter {selected_scooter.getId()} ausgeliehen.")
    print(f"Scooter ausgeliehen um: {ausleihZeitpunkt[0]}:{ausleihZeitpunkt[1]} Uhr")
    print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {PRICE_PER_MINUTE}€")
    print(f"Der Preis pro Angefangene Minute beträgt {formattedPricePerMinute}€")

    selected_scooter.setScooterAusgeliehen(True)
    ausgeliehene_scooter.append(selected_scooter)
    #print(ausgeliehene_scooter)
    

def datenZurAktuellenFahrt():
    for scooter in ausgeliehene_scooter:
        print("\n\n")
        print("- Daten zu deinen aktuell ausgeliehenen Scooteren -")
        datenZurAktuellenFahrtByScooterId(scooter.getId())
    else:
        print("Kein Scooter wurde ausgeliehen.")
        return

def datenZurAktuellenFahrtByScooterId(id):
    selected_scooter = getScooterById(id)
  
    print(f"- Daten zu Scooter '{id}' -")
    print("\n")

    fruehererZeitpunkt = selected_scooter.getAusleihZeitpunkt()
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

    print(f"Du fährst aktuell mit dem Scooter {selected_scooter.getId()}")

def scooterZurueckgeben():
    if len(ausgeliehene_scooter) == 0 or not ausgeliehene_scooter:
        print("Kein Scooter wurde ausgeliehen.")
    
    print("\nDu hast aktuell die Folgenden Scooter ausgeliehen:")
    #for scooter in ausgeliehene_scooter:
    #    print(scooter.getId())

    print(", ".join(str(scooter.getId()) for scooter in ausgeliehene_scooter))

    print("Welcher Scooter soll zurückgegeben werden?")
    returnedScooterId = input("(Als Zahl angeben oder 'all' um alle zurückzugeben): ")
    if returnedScooterId == "all":
        for scooter in ausgeliehene_scooter:
            scooterZurueckgebenById(scooter.getId())
        return
    scooterZurueckgebenById(int(returnedScooterId))


def scooterZurueckgebenById(id):
    selected_scooter = getScooterById(id)
    
    selected_scooter.setRueckgabeZeitpunkt(getCurrentTimeStamp())
    selected_scooter.setScooterAusgeliehen(False)
    ausgeliehene_scooter.remove(selected_scooter)

    print("\n\n")
    print("- Scooter Zurueckgeben -")
    print("\n")

    ausleihZeitpunkt = selected_scooter.getAusleihZeitpunkt()
    rueckgabeZeitpunkt = selected_scooter.getRueckgabeZeitpunkt()

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
    for scooter in scooter_list:
        if not scooter.getScooterAusgeliehen() and not scooter.getScooterReserviert():
            selected_scooter = scooter
            break
            #print(f"Der erste verfügbare Scooter hat die ID: {scooter.id}")
        else:
            print("Kein verfügbarer Scooter gefunden.")

    reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
    reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")

    if reservierungsZeitraumpruefen(int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)):
        selected_scooter.setReservierungsZeitpunkt([int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)])
        selected_scooter.setScooterReserviert(True)

    else:
        while reservierungsZeitraumpruefen(int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)) == False:
            print("Deine Reservierung liegt zu weit in der Zukunft")
            print("Du kannst maximal eine halbe Stunde in der Zukunft reservieren")
            print("Bitte gib einen gültigen Wert an")

            reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
            reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")

    if selected_scooter.getScooterReserviert() == True:
        print(f"Du hast erfolgreich den Scooter {selected_scooter.getId()} reserviert!")
        ausgeliehene_scooter.append(selected_scooter)

def uebersichtScooter():
    if ausgeliehene_scooter:
        for scooter in ausgeliehene_scooter:
            if scooter.getScooterReserviert():
                # Hier wird immer auf das Letze Element der Liste zugegriffen, müsst man noch eleganter  lösen (z.B. indem der Nutzer die ID seines Scooters eingibt)
                selected_scooter = ausgeliehene_scooter[-1]
    
    try:
        if selected_scooter.getScooterReserviert() == True:
            reservierungsZeitpunkt = selected_scooter.getReservierungsZeitpunkt()

            print("Es ist eine Reservierung vohanden")
            print(f"Der Scooter {selected_scooter.getId()} ist für dich reserviert")
            if reservierungsZeitpunkt[1] <= 9:
                print("Deine Reservierung beginnt um:", reservierungsZeitpunkt[0], ":0", reservierungsZeitpunkt[1])
                return
            print("Deine Reservierung beginnt um:", reservierungsZeitpunkt[0], ":", reservierungsZeitpunkt[1])
    except UnboundLocalError as e:
        print("Du hast keinen Scooter reserviert")
        return False

def hasReservierung():
    if ausgeliehene_scooter:
        for scooter in ausgeliehene_scooter:
            if scooter.getScooterReserviert():
                return True
    
    return False

def reservierungsZeitraumpruefen(reservierungsZeitpunktHour, reservierungsZeitpunktMinute):

    reservierung = datetime.now().replace(hour=reservierungsZeitpunktHour, minute=reservierungsZeitpunktMinute, second=0, microsecond=0)

    time_difference = reservierung - datetime.now() 
    max_difference = timedelta(minutes=30)

    if time_difference <= max_difference:
        return True
    else:
        return False