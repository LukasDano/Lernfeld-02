class Scooter:
    def __init__(self):
        # Initialisierung des Scooter-Status, zu Beginn auf False
        self.scooterAusgeliehen = False
    
    def get_scooterAusgeliehen(self):
        # Gibt den aktuellen Status des Scooters zurück
        return self.scooterAusgeliehen
    
    def set_scooterAusgeliehen(self, status):
        # Setzt den Scooter-Status auf den angegebenen Wert
        if isinstance(status, bool):
            self.scooterAusgeliehen = status
        else:
            raise ValueError("Status muss ein Boolean-Wert sein")

# Beispielverwendung:
scooter = Scooter()
class Scooter:
    def __init__(self):
        # Initialisierung des Scooter-Status, zu Beginn auf False
        self.scooterAusgeliehen = False
    
    def get_scooterAusgeliehen(self):
        # Gibt den aktuellen Status des Scooters zurück
        return self.scooterAusgeliehen
    
    def set_scooterAusgeliehen(self, status):
        # Setzt den Scooter-Status auf den angegebenen Wert
        if isinstance(status, bool):
            self.scooterAusgeliehen = status
        else:
            raise ValueError("Status muss ein Boolean-Wert sein")

# Beispielverwendung:
scooter = Scooter()
print(scooter.get_scooterAusgeliehen())  # Ausgabe: False

scooter.set_scooterAusgeliehen(True)
print(scooter.get_scooterAusgeliehen())  # Ausgabe: True

