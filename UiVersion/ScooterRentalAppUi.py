import random
import datetime
from datetime import *

import ScooterClassUi

class ScooterRentalApp:
    GEBUEHR = 1
    PRICE_PER_MINUTE_RESERVE = 0.05
    PRICE_PER_MINUTE_DRIVE = 0.10

    MINDEST_ENTFERNUNG = 10
    MAXIMALE_ENTFERNUNG = 2500

    def __init__(self):
        self.scooter = ScooterClassUi.Scooter
        self.scooter_list = []
        self.ausgeliehene_scooter = []

        for i in range(10):
            scooter_for_list = self.scooter(i + 1, self.getRandomStandort())
            self.scooter_list.append(scooter_for_list)

        self.bearbeiteterScooterId = 1

    def getRandomStandort(self):
        return random.randint(self.MINDEST_ENTFERNUNG, self.MAXIMALE_ENTFERNUNG)
        
    def getScooterById(self, id):
        for scooter in self.scooter_list:
            if scooter.getId() == id:
                return scooter
        print("Keinen Scooter mit dieser Id gefunden.")

    @staticmethod
    def getCurrentTimeStamp():
        now = datetime.now()
        hours = int(now.strftime("%H"))
        minutes = int(now.strftime("%M"))
        seconds = int(now.strftime("%S"))

        return [hours, minutes, seconds]

    @staticmethod
    def getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt):
        frueher = datetime(2020, 1, 1, fruehererZeitpunkt[0], fruehererZeitpunkt[1], fruehererZeitpunkt[2])
        spaeter = datetime(2020, 1, 1, spaetererZeitpunkt[0], spaetererZeitpunkt[1], spaetererZeitpunkt[2])
        
        differenz = spaeter - frueher
        differenz_in_secs = differenz.total_seconds()
        hours = int(differenz_in_secs // 3600)
        minutes = int((differenz_in_secs % 3600) // 60)
        seconds = int(differenz_in_secs % 60)
        
        return [hours, minutes, seconds]

    @staticmethod
    def getPrice(timeInMinutes):
        price = timeInMinutes * ScooterRentalApp.PRICE_PER_MINUTE_DRIVE + ScooterRentalApp.GEBUEHR
        formattedPrice = "{:.2f}".format(price)
        return formattedPrice

    def scooterAusleihen(self, id):
        selected_scooter = None
        for scooter in self.scooter_list:
            if scooter.getScooterReserviert():
                selected_scooter = scooter
                selected_scooter.setScooterReserviert(False)
                self.ausgeliehene_scooter.remove(selected_scooter)
                print("Reservierter Scooter erfolgreich ausgeliehen.")
                break
            elif not scooter.getScooterAusgeliehen():
                selected_scooter = scooter
                break
            else:
                print("Kein verfügbarer Scooter gefunden.")

        # TODO: Reservierung Handling
        selected_scooter = self.getScooterById(id)
        
        if selected_scooter:
            print("\n\n- Scooter Ausleihen -\n")
            aktuelleZeit = self.getCurrentTimeStamp()
            ausleihZeitpunkt = [aktuelleZeit[0], aktuelleZeit[1], aktuelleZeit[2]]
            selected_scooter.setAusleihZeitpunkt(ausleihZeitpunkt)
            formattedPricePerMinute = "{:.2f}".format(self.PRICE_PER_MINUTE_DRIVE)
            ausleihZeitpunkt = selected_scooter.getAusleihZeitpunkt()
            
            print(f"Du hast den Scooter {selected_scooter.getId()} ausgeliehen.")
            print(f"Scooter ausgeliehen um: {ausleihZeitpunkt[0]}:{ausleihZeitpunkt[1]} Uhr")
            print(f"Die Gebühr zum Ausleihen eines Scooters beträgt {self.PRICE_PER_MINUTE_DRIVE}€")
            print(f"Der Preis pro angefangene Minute beträgt {formattedPricePerMinute}€")

            selected_scooter.setScooterAusgeliehen(True)
            self.bearbeiteterScooterId = selected_scooter.getId()
            self.ausgeliehene_scooter.append(selected_scooter)

    def datenZurAktuellenFahrt(self):
        if self.ausgeliehene_scooter:
            print("\n\n- Daten zu deinen aktuell ausgeliehenen Scootern -")
            for scooter in self.ausgeliehene_scooter:
                self.datenZurAktuellenFahrtByScooterId(scooter.getId())
        else:
            print("Kein Scooter wurde ausgeliehen.")

    def datenZurAktuellenFahrtByScooterId(self, id):
        selected_scooter = self.getScooterById(id)
        if selected_scooter:
            print(f"- Daten zu Scooter '{id}' -\n")
            fruehererZeitpunkt = selected_scooter.getAusleihZeitpunkt()
            spaetererZeitpunkt = self.getCurrentTimeStamp()
            timeDifference = self.getTimeDifferance(fruehererZeitpunkt, spaetererZeitpunkt)
            hours = timeDifference[0]
            minutes = timeDifference[1]
            seconds = self.getCurrentTimeStamp()[2]
            print(f"Ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")
            timeInMinutes = int(hours) * 60 + int(minutes)
            if seconds != 0:
                timeInMinutes += 1
            price = self.getPrice(timeInMinutes)
            self.selected_scooter.setAktuellerPreis(price)
            print(f"Aktueller Preis dieser Fahrt: {price}€")
            print(f"Du fährst aktuell mit dem Scooter {selected_scooter.getId()}")

    def scooterZurueckgeben(self):
        if not self.ausgeliehene_scooter:
            print("Kein Scooter wurde ausgeliehen.")
            return
        
        print("\nDu hast aktuell die folgenden Scooter ausgeliehen:")
        print(", ".join(str(scooter.getId()) for scooter in self.ausgeliehene_scooter))
        returnedScooterId = input("(Als Zahl angeben oder 'all' um alle zurückzugeben): ")
        if returnedScooterId == "all":
            for scooter in self.ausgeliehene_scooter[:]:
                self.scooterZurueckgebenById(scooter.getId())
        else:
            self.scooterZurueckgebenById(int(returnedScooterId))

    def scooterZurueckgebenById(self, id):
        selected_scooter = self.getScooterById(id)
        if selected_scooter:
            selected_scooter.setRueckgabeZeitpunkt(self.getCurrentTimeStamp())
            selected_scooter.setScooterAusgeliehen(False)
            self.ausgeliehene_scooter.remove(selected_scooter)
            print("\n\n- Scooter Zurueckgeben -\n")
            ausleihZeitpunkt = selected_scooter.getAusleihZeitpunkt()
            rueckgabeZeitpunkt = selected_scooter.getRueckgabeZeitpunkt()
            print(f"Scooter zurueckgeben am: {rueckgabeZeitpunkt[0]}:{rueckgabeZeitpunkt[1]} Uhr")
            timeDifference = self.getTimeDifferance(ausleihZeitpunkt, rueckgabeZeitpunkt)
            hours = timeDifference[0]
            minutes = timeDifference[1]
            seconds = self.getCurrentTimeStamp()[2]
            print(f"Insgesamt ausgeliehene Zeit: {hours} Stunden {minutes} Minuten")
            timeInMinutes = int(hours) * 60 + int(minutes)
            if seconds != 0:
                timeInMinutes += 1
            price = self.getPrice(timeInMinutes)
            print(f"Preis dieser Fahrt: {price}€")

    def scooterReservieren(self):
        selected_scooter = None
        for scooter in self.scooter_list:
            if not scooter.getScooterAusgeliehen() and not scooter.getScooterReserviert():
                selected_scooter = scooter
                break
            else:
                print("Kein verfügbarer Scooter gefunden.")

        if selected_scooter:
            reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
            reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")

            if self.reservierungsZeitraumpruefen(int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)):
                selected_scooter.setReservierungsZeitpunkt([int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)])
                selected_scooter.setScooterReserviert(True)
            else:
                while not self.reservierungsZeitraumpruefen(int(reservierungsZeitpunktHour), int(reservierungsZeitpunktMinute)):
                    print("Deine Reservierung liegt zu weit in der Zukunft")
                    print("Du kannst maximal eine halbe Stunde in der Zukunft reservieren")
                    print("Bitte gib einen gültigen Wert an")
                    reservierungsZeitpunktHour = input("Reservierungszeitpunkt (HH): ")
                    reservierungsZeitpunktMinute = input("Reservierungszeitpunkt (MM): ")

            if selected_scooter.getScooterReserviert():
                print(f"Du hast erfolgreich den Scooter {selected_scooter.getId()} reserviert!")
                self.ausgeliehene_scooter.append(selected_scooter)

    def uebersichtScooter(self):
        if self.ausgeliehene_scooter:
            selected_scooter = None
            for scooter in self.ausgeliehene_scooter:
                if scooter.getScooterReserviert():
                    selected_scooter = scooter
            
            if selected_scooter and selected_scooter.getScooterReserviert():
                reservierungsZeitpunkt = selected_scooter.getReservierungsZeitpunkt()
                print("Es ist eine Reservierung vorhanden")
                print(f"Der Scooter {selected_scooter.getId()} ist für dich reserviert")
                if reservierungsZeitpunkt[1] <= 9:
                    print(f"Deine Reservierung beginnt um: {reservierungsZeitpunkt[0]}:0{reservierungsZeitpunkt[1]}")
                else:
                    print(f"Deine Reservierung beginnt um: {reservierungsZeitpunkt[0]}:{reservierungsZeitpunkt[1]}")
            else:
                print("Du hast keinen Scooter reserviert")

    def hasReservierung(self):
        for scooter in self.ausgeliehene_scooter:
            if scooter.getScooterReserviert():
                return True
        return False

    def reservierungsZeitraumpruefen(self, reservierungsZeitpunktHour, reservierungsZeitpunktMinute):
        reservierung = datetime.now().replace(hour=reservierungsZeitpunktHour, minute=reservierungsZeitpunktMinute, second=0, microsecond=0)
        time_difference = reservierung - datetime.now() 
        max_difference = timedelta(minutes=30)
        return time_difference <= max_difference
