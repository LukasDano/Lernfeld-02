class Scooter:
    GEBUEHR = 1
    PRICE_PER_MINUTE = 0.10

    def __init__(self, id):
        self.id = id
        self.ausleih_zeitpunkt = []
        self.rueckgabe_zeitpunkt = []
        self.reservierungs_zeitpunkt = []
        self.scooter_ausgeliehen = False
        self.scooter_reserviert = False

    @property
    def gebuehr(self):
        return self.GEBUEHR

    @property
    def price_per_minute(self):
        return self.PRICE_PER_MINUTE

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def ausleih_zeitpunkt(self):
        return self._ausleih_zeitpunkt

    @ausleih_zeitpunkt.setter
    def ausleih_zeitpunkt(self, ausleih_zeitpunkt):
        self._ausleih_zeitpunkt = ausleih_zeitpunkt

    @property
    def rueckgabe_zeitpunkt(self):
        return self._rueckgabe_zeitpunkt

    @rueckgabe_zeitpunkt.setter
    def rueckgabe_zeitpunkt(self, rueckgabe_zeitpunkt):
        self._rueckgabe_zeitpunkt = rueckgabe_zeitpunkt

    @property
    def reservierungs_zeitpunkt(self):
        return self._reservierungs_zeitpunkt

    @reservierungs_zeitpunkt.setter
    def reservierungs_zeitpunkt(self, reservierungs_zeitpunkt):
        self._reservierungs_zeitpunkt = reservierungs_zeitpunkt

    @property
    def scooter_ausgeliehen(self):
        return self._scooter_ausgeliehen

    @scooter_ausgeliehen.setter
    def scooter_ausgeliehen(self, scooter_ausgeliehen):
        self._scooter_ausgeliehen = scooter_ausgeliehen

    @property
    def scooter_reserviert(self):
        return self._scooter_reserviert

    @scooter_reserviert.setter
    def scooter_reserviert(self, scooter_reserviert):
        self._scooter_reserviert = scooter_reserviert
