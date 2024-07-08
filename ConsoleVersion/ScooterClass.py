class Scooter:
    def __init__(self, id):
        self.id = id

        self.ausleihZeitpunkt = []
        self.rueckgabeZeitpunkt = []
        self.reservierungsZeitpunkt = []

        self.scooterAusgeliehen = False
        self.scooterReserviert = False

    def getId(self):
        return self.id    
    
    def getScooterAusgeliehen(self):
        return self.scooterAusgeliehen
    
    def setScooterAusgeliehen(self, status):

        if isinstance(status, bool):
            self.scooterAusgeliehen = status
        else:
            raise ValueError("Status muss 'True' oder 'False' sein")

    def getScooterReserviert(self):
        return self.scooterReserviert    

    def setScooterReserviert(self, status):    
        if isinstance(status, bool):
            self.scooterReserviert = status
        else:
            raise ValueError("Status muss 'True' oder 'False' sein")

    def setAusleihZeitpunkt(self, ausleih_zeitpunkt):
        self.ausleihZeitpunkt = ausleih_zeitpunkt

    def getAusleihZeitpunkt(self):
        return self.ausleihZeitpunkt
    
    def getRueckgabeZeitpunkt(self):
        return self.rueckgabeZeitpunkt
    
    def setRueckgabeZeitpunkt(self, rueckgabeZeitpunkt):
        self.rueckgabeZeitpunkt = rueckgabeZeitpunkt

    def getReservierungsZeitpunkt(self):
        return self.reservierungsZeitpunkt
    
    def setReservierungsZeitpunkt(self, reservierungsZeitpunkt):
        self.reservierungsZeitpunkt = reservierungsZeitpunkt
