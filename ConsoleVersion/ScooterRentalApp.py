from datetime import *
import ScooterClass

scooter = ScooterClass.Scooter

GEBUEHR = 1
PRICE_PER_MINUTE = 0.10

scooter_list = []
ausgeliehene_scooter = []

for i in range(10):
    scooter_for_list = scooter(i)
    scooter_list.append(scooter_for_list)

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
    price = timeInMinutes * PRICE_PER_MINUTE + GEBUEHR
    formattedPrice = "{:.2f}".format(price)
    return formattedPrice

def scooterAusleihen():
    for scooter in scooter_list:
        if scooter.scooter_reserviert:
            selected_scooter = scooter
            selected_scooter.scooter_reserviert = False
            ausgeliehene_scooter.remove(selected_scooter)
            break
        elif not scooter.scooter_ausgeliehen:
            selected_scooter = scooter
            break
            #print(f"Der erste verfügbare Scooter hat die ID: {scooter.id}")
        else:
            print("Kein verfügbarer Scooter gefunden.")

    print("\n\n")
    print("- Scooter Ausleihen -")
    print("\n")

    aktuelleZeit = getCurrentTimeStamp()

    scooter.ausleih_zeitpunkt.append(aktuelleZeit[0])
    scooter.ausleih_zeitpunkt.append(aktuelleZeit[1])
    scooter.ausleih_zeitpunkt.append(aktuelleZeit[2])

    formattedPricePerMinute = "{:.2f}".format(PRICE_PER_MINUTE)

    print(f"Du hast den Scooter {selected_scooter.id} ausgeliehen.")
    print(f"Scooter ausgeliehen um: {scooter.ausleih_zeitpunkt[0]}:{scooter.ausleih_zeitpunkt[1]} Uhr")
    print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {PRICE_PER_MINUTE}€")
    print(f"Der Preis pro Angefangene Minute beträgt {formattedPricePerMinute}€")

    selected_scooter.scooter_ausgeliehen = True
    ausgeliehene_scooter.append(selected_scooter)
    #print(ausgeliehene_scooter)
    

def datenZurAktuellenFahrt():
    if ausgeliehene_scooter:
        # Hier wird immer auf das Letze Element der Liste zugegriffen, müsst man noch eleganter  lösen (z.B. indem der Nutzer die ID seines Scooters eingibt)
        selected_scooter = ausgeliehene_scooter[-1]
    else:
        print("Kein Scooter wurde ausgeliehen.")
        return
    
    print("\n\n")
    print("- Die Daten zu deiner aktuellen Fahrt -")
    print("\n")

    fruehererZeitpunkt = selected_scooter.ausleih_zeitpunkt
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

    print(f"Du fährst aktuell mit dem Scooter {selected_scooter.id}")

def scooterZurueckgeben():
    if ausgeliehene_scooter:
        # Hier wird immer auf das Letze Element der Liste zugegriffen, müsst man noch eleganter  lösen (z.B. indem der Nutzer die ID seines Scooters eingibt)
        selected_scooter = ausgeliehene_scooter[-1]
    else:
        print("Kein Scooter wurde ausgeliehen.")
        return
    
    selected_scooter.rueckgabe_zeitpunkt = getCurrentTimeStamp()

    selected_scooter.scooter_ausgeliehen = False

    print("\n\n")
    print("- Scooter Zurueckgeben -")
    print("\n")

    print(f"Scooter zurueckgeben am: {selected_scooter.rueckgabe_zeitpunkt[0]}:{selected_scooter.rueckgabe_zeitpunkt[1]} Uhr")

    timeDifference = getTimeDifferance(selected_scooter.ausleih_zeitpunkt, selected_scooter.rueckgabe_zeitpunkt)
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
        if not scooter.scooter_ausgeliehen and not scooter.scooter_reserviert:
            selected_scooter = scooter
            break
            #print(f"Der erste verfügbare Scooter hat die ID: {scooter.id}")
        else:
            print("Kein verfügbarer Scooter gefunden.")

    reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
    reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")

    if reservierungsZeitraumpruefen(int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)):
        selected_scooter.reservierungs_zeitpunkt = [int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)]
        selected_scooter.scooter_reserviert = True

    else:
        while reservierungsZeitraumpruefen(int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)) == False:
            print("Deine Reservierung liegt zu weit in der Zukunft")
            print("Du kannst maximal eine halbe Stunde in der Zukunft reservieren")
            print("Bitte gib einen gültigen Wert an")

            reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
            reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")

    if selected_scooter.scooter_reserviert == True:
        print(f"Du hast erfolgreich den Scooter {selected_scooter.id} reserviert!")
        ausgeliehene_scooter.append(selected_scooter)

def uebersichtScooter():
    if ausgeliehene_scooter:
        for scooter in ausgeliehene_scooter:
            if scooter.scooter_reserviert:
                # Hier wird immer auf das Letze Element der Liste zugegriffen, müsst man noch eleganter  lösen (z.B. indem der Nutzer die ID seines Scooters eingibt)
                selected_scooter = ausgeliehene_scooter[-1]
    
    try:
        if selected_scooter.scooter_reserviert == True:
            print("Es ist eine Reservierung vohanden")
            print(f"Der Scooter {selected_scooter.id} ist für dich reserviert")
            print("Deine Reservierung beginnt um:", selected_scooter.reservierungs_zeitpunkt[0], ":", selected_scooter.reservierungs_zeitpunkt[1])
            return
    except UnboundLocalError as e:
        print("Du hast keinen Scooter reserviert")
        return False

def hasReservierung():
    if ausgeliehene_scooter:
        for scooter in ausgeliehene_scooter:
            if scooter.scooter_reserviert:
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