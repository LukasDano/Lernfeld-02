class Scooter:
    def __init__(self, id):
        self.id = id
        self.scooterAusgeliehen = False
        self.scooterReserviert = False
        self.ausleih_zeitpunkt = []
        self.rueckgabeZeitpunkt = []
        self.reservierungsZeitpunkt = []

    def getId(self):
        return self.id    
    
    def get_scooterAusgeliehen(self):
        return self.scooterAusgeliehen
    
    def set_scooterAusgeliehen(self, status):

        if isinstance(status, bool):
            self.scooterAusgeliehen = status
        else:
            raise ValueError("Status muss ein Boolean-Wert sein")

    def get_scooterReserviert(self):
        return self.scooterReserviert    

    def setScooterReserviert(self, status):    
        if isinstance(status, bool):
            self.scooterReserviert = status
        else:
            raise ValueError("Status muss ein Boolean-Wert sein")

    def set_ausleih_zeitpunkt(self, ausleih_zeitpunkt):
        self.ausleih_zeitpunkt = ausleih_zeitpunkt

    def ausleih_zeitpunkt(self):
        return self._ausleih_zeitpunkt
    
    def getRueckgabeZeitpunkt(self):
        return self.rueckgabeZeitpunkt
    
    def setRueckgabeZeitpunkt(self, rueckgabeZeitpunkt):
        self.rueckgabeZeitpunkt = rueckgabeZeitpunkt

    def getReservierungsZeitpunkt(self):
        return self.reservierungsZeitpunkt
    
    def setReservierungsZeitpunkt(self, reservierungsZeitpunkt):
        self.reservierungsZeitpunkt = reservierungsZeitpunkt

scooter1 = Scooter(1)
ausleihZeitpunkt=[12,53]
rueckgabeZeitpunkt=[13, 00]
reservierungsZeitpunkt=[13, 1]
print(scooter1.get_scooterAusgeliehen()) 
print(scooter1.getId())
scooter1.set_scooterAusgeliehen(True)
print(scooter1.get_scooterAusgeliehen())  

scooter1.set_ausleih_zeitpunkt(ausleihZeitpunkt)
print(scooter1.ausleih_zeitpunkt)
scooter1.setRueckgabeZeitpunkt(rueckgabeZeitpunkt)
print(scooter1.getRueckgabeZeitpunkt())
scooter1.setReservierungsZeitpunkt(reservierungsZeitpunkt)
print(scooter1.getReservierungsZeitpunkt())
print("Scooter sollte nicht reserviert sein!")
print(scooter1.get_scooterReserviert())
scooter1.setScooterReserviert(True)
print("Scooter sollte reserviert sein!")
print(scooter1.get_scooterReserviert())
