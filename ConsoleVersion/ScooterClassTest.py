import ScooterClass

scooter = ScooterClass.Scooter(22)
scoter2 = ScooterClass.Scooter(22)

# Beispielverwendung:
scooter = ScooterClass.Scooter()
print(scooter.get_scooterAusgeliehen())  # Ausgabe: False

scooter.set_scooterAusgeliehen(True)
print(scooter.get_scooterAusgeliehen())  # Ausgabe: True

scooter_list = []

for i in range(10):
    scooter_for_list = scooter(i)
    scooter_list.append(scooter_for_list)

for i in range(10):
    print(scooter_list[i].get_scooterAusgeliehen())