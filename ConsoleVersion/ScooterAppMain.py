import ScooterRentalApp

app = ScooterRentalApp

optionZero = list(("0", "beenden", "exit"))
optionOne = list(("1", "ausleihen"))
optionTwo = list(("2", "abfragen"))
optionThree = list(("3", "zurueckgeben", "zurückgeben"))
optionFour = list(("4", "reservieren"))
optionFive = list(("5", "uebersicht"))



# Die eingetliche Anwendung =>
print("Digitale Scooter App")
print("\n \n \n")


while True:

    if __name__ == "__main__":

        if app.hasReservierung() and auszufuehrendeMehtode not in optionFive:
            print("- Reminder - \n")
            app.uebersichtScooter()

        print("\n")
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
        elif auszufuehrendeMehtode in optionOne:
            app.scooterAusleihen()
        elif auszufuehrendeMehtode in optionTwo:
            app.datenZurAktuellenFahrt()
        elif auszufuehrendeMehtode in optionThree:
            app.scooterZurueckgeben()
        elif auszufuehrendeMehtode in optionFour:
            app.scooterReservieren()
        elif auszufuehrendeMehtode in optionFive:
            app.uebersichtScooter()
        else:
            print("Falsche Eingabe")
            print("Bitte wähle ein der angebenen Optionen")
