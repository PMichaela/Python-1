class Car:
    def __init__(self, registration_mark, type_vehicle, mileage):
        self.registration_mark = registration_mark
        self.type_vehicle = type_vehicle
        self.mileage = mileage
        self.available = True

    def rent_car(self):
        if self.available:
            self.available = False
            return "I confirm the rental of the vehicle."
        else:
            return "The vehicle is not available."
    
    def get_info(self):
        return f"Type of vehicle {self.type_vehicle} and its registration plate {self.registration_mark}."

peugeot = Car("4A2 3020", "Peugeot 403 Cabrio", 47534)
skoda = Car("1P3 4747", "Škoda Octavia", 41253)

order = input("Which car do you want to rent (Peugeot/Škoda): ")

if order.casefold() == "peugeot":
    vehicle = peugeot
elif order.casefold() == "škoda" or "skoda":
    vehicle = skoda
else:
    print("We don't have that vehicle.")
    exit()

print(vehicle.get_info())
print(vehicle.rent_car())

print(vehicle.rent_car())