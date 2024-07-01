import ScooterRentalApp

app = ScooterRentalApp

print("Digitale Scooter App")
print("\n \n \n")

while True:

    if __name__ == "__main__":

        print("Optionen: \n")
        print("1. Scooter ausleihen")
        print("2. Daten der aktuellen Fahrt abfragen")

        print("\n")
        auszuführendeMehtode = input("Was möchtest du machen?")

        if auszuführendeMehtode == "1" or auszuführendeMehtode == "ausleihen":
            app.scooterAusleihen()
        
        if auszuführendeMehtode == "2" or auszuführendeMehtode == "abfragen":
            app.datenZurAktuellenFahrt()
