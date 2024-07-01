import ScooterRentalApp

app = ScooterRentalApp
again = True

while again:

    if __name__ == "__main__":
        print("Digitale Scooter App")
        print("\n \n \n")

        ausleihen = input("Scooter ausleihen (y/n)? ")

        if ausleihen == "y":
            app.scooterAusleihen()
        else:
            print("Scooter nicht ausgeliehen")
        
        
        abfragen = input("Aktuelle Datenabfragen (y/n)? ")
        
        if abfragen == "y":
            app.datenZurAktuellenFahrt()
        else:
            print("Nicht abgefragt")

        again = input("Noch einmal (True/False)? ")