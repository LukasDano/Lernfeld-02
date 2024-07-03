import ScooterRentalApp
import ScooterClass
import Scooter

app = ScooterRentalApp
scooter = Scooter.Scooter

scooter01 = ScooterClass.Scooter()

optionZero = list(("0", "beenden", "exit"))
optionOne = list(("1", "ausleihen"))
optionTwo = list(("2", "abfragen"))
optionThree = list(("3", "zurueckgeben", "zurückgeben"))
optionFour = list(("4", "reservieren"))
optionFive = list(("5", "uebersicht"))

scooter_list = []

for i in range(10):
    scooter_for_list = scooter(i)
    scooter_list.append(scooter_for_list)
print (scooter_list)

# Die eingetliche Anwendung =>
print("Digitale Scooter App")
print("\n \n \n")


while True:

    if __name__ == "__main__":

        if app.reservierungsZeitpunkt != [0,0]:
            print("- Reminder -")
            print(f"Du hast einen Scooter für {app.reservierungsZeitpunkt[0]}:{app.reservierungsZeitpunkt[1]} Uhr reserviert")

        print("<--------------------------------------->")
        print("Optionen: \n")
        print("0. Beenden")
        print("1. Scooter ausleihen")
        print("2. Daten der aktuellen Fahrt abfragen")
        print("3. Scooter zurueckgeben")
        print("4. Scooter reservieren")
        print("5. Scooter Uebersicht (Reservierungen)")


        print("\n")
        auszufuehrendeMehtode = input("Was möchtest du machen?")

        if auszufuehrendeMehtode in optionZero:
            break

        if auszufuehrendeMehtode in optionOne:
            app.scooterAusleihen()
        
        if auszufuehrendeMehtode in optionTwo:
            app.datenZurAktuellenFahrt()
        
        if auszufuehrendeMehtode in optionThree:
            app.scooterZurueckgeben()
        
        if auszufuehrendeMehtode in optionFour:
            app.scooterReservieren()
        
        if auszufuehrendeMehtode in optionFive:
            app.uebersichtScooter()

print(scooter01.get_scooterAusgeliehen())  # Ausgabe: False

scooter01.set_scooterAusgeliehen(True)
print(scooter01.get_scooterAusgeliehen())  # Ausgabe: True
