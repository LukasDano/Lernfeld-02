import ConsoleVersion.ScooterClass

scooterClass = ConsoleVersion.ScooterClass

green = "#ff0000: Works"
red = "#00ff00: Fails"

def test_scooter_class_with_list():

    scooter = scooterClass.Scooter
    scooter_list = []

    for i in range(10):
        scooter_for_list = scooter(i)
        scooter_list.append(scooter_for_list)

    for i in range(10):
        if scooter_list[i].getScooterAusgeliehen() == False:
            print(green)
        else:
            raise ValueError(red)
    
    # Status auf "True" setzen
    for i in range(10):
        scooter_list[i].setScooterAusgeliehen(True)

    for i in range(10):
        if scooter_list[i].getScooterAusgeliehen() == True:
            print(green)
        else:
            print(red)
            raise ValueError(red)
    
    return True

def test_scooter_status_und_id_methodes():
    
    scooter = scooterClass.Scooter(1)

    if scooter.getScooterAusgeliehen() == False:
        print(green)
    else:
        raise ValueError(red)

    scooter.setScooterAusgeliehen(True)
    if scooter.getScooterAusgeliehen() == True:
        print(green)
    else:
        raise ValueError(red)

    if scooter.getScooterReserviert() == False:
        print(green)
    else:
        raise ValueError(red)

    scooter.setScooterReserviert(True)
    if scooter.getScooterReserviert() == True:
        print(green)
    else:
        raise ValueError(red)

    if scooter.getId() == 1:
        print(green)
    else:
        raise ValueError(red)

    return True

#Klaus Tests
def test_all_scooter_class_methods():

    scooter = scooterClass.Scooter(2)

    ausleihZeitpunkt=[12,53]
    rueckgabeZeitpunkt=[13, 00]
    reservierungsZeitpunkt=[13, 1]

    scooter.setAusleihZeitpunkt(ausleihZeitpunkt)
    if scooter.getAusleihZeitpunkt()== ausleihZeitpunkt:
        print(green)
    else:
        raise ValueError(red)

    scooter.setRueckgabeZeitpunkt(rueckgabeZeitpunkt)
    if scooter.getRueckgabeZeitpunkt() == rueckgabeZeitpunkt:
        print(green)
    else:
        raise ValueError(red)

    scooter.setReservierungsZeitpunkt(reservierungsZeitpunkt)
    if scooter.getReservierungsZeitpunkt() == reservierungsZeitpunkt:
        print(green)
    else:
        raise ValueError(red)
    
    return True

if __name__ == "__main__":

    test_scooter_class_with_list()

    test_scooter_status_und_id_methodes()

    test_all_scooter_class_methods()

    print("\n\n <- Alle Tests waren erfolgreich ->")