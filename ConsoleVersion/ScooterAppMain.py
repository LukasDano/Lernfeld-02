import ScooterRentalApp

app = ScooterRentalApp

optionZero = list(("0", "exit", "beenden"))
optionOne = list(("1", "ausleihen"))
optionTwo = list(("2", "abfragen"))
optionThree = list(("3", "zurueckgeben", "zurückgeben"))

print("Digitale Scooter App")
print("\n \n \n")

while True:

    if __name__ == "__main__":

        print("Optionen: \n")
        print("0. Beenden")
        print("1. Scooter ausleihen")
        print("2. Daten der aktuellen Fahrt abfragen")
        print("3. Scooter zurueckgeben")


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

