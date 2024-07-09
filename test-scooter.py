import unittest
from datetime import datetime
import ConsoleVersion.ScooterClass

scooterClass = ConsoleVersion.ScooterClass

class TestScooter(unittest.TestCase):
    def setUp(self):
        self.scooter = scooterClass.Scooter(1)

    def test_getId(self):
        self.assertEqual(self.scooter.getId(), 1)

    def test_getScooterAusgeliehen(self):
        self.assertFalse(self.scooter.getScooterAusgeliehen())

    def test_setScooterAusgeliehen(self):
        self.scooter.setScooterAusgeliehen(True)
        self.assertTrue(self.scooter.getScooterAusgeliehen())
        
        self.scooter.setScooterAusgeliehen(False)
        self.assertFalse(self.scooter.getScooterAusgeliehen())
        
        with self.assertRaises(ValueError):
            self.scooter.setScooterAusgeliehen("yes")

    def test_getScooterReserviert(self):
        self.assertFalse(self.scooter.getScooterReserviert())

    def test_setScooterReserviert(self):
        self.scooter.setScooterReserviert(True)
        self.assertTrue(self.scooter.getScooterReserviert())
        
        self.scooter.setScooterReserviert(False)
        self.assertFalse(self.scooter.getScooterReserviert())
        
        with self.assertRaises(ValueError):
            self.scooter.setScooterReserviert("yes")

    def test_setAusleihZeitpunkt(self):
        now = datetime.now()
        self.scooter.setAusleihZeitpunkt(now)
        self.assertEqual(self.scooter.getAusleihZeitpunkt(), now)

    def test_getAusleihZeitpunkt(self):
        self.assertEqual(self.scooter.getAusleihZeitpunkt(), [])

    def test_setRueckgabeZeitpunkt(self):
        now = datetime.now()
        self.scooter.setRueckgabeZeitpunkt(now)
        self.assertEqual(self.scooter.getRueckgabeZeitpunkt(), now)

    def test_getRueckgabeZeitpunkt(self):
        self.assertEqual(self.scooter.getRueckgabeZeitpunkt(), [])

    def test_setReservierungsZeitpunkt(self):
        now = datetime.now()
        self.scooter.setReservierungsZeitpunkt(now)
        self.assertEqual(self.scooter.getReservierungsZeitpunkt(), now)

    def test_getReservierungsZeitpunkt(self):
        self.assertEqual(self.scooter.getReservierungsZeitpunkt(), [])

if __name__ == '__main__':
    unittest.main()
