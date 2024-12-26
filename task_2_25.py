from abc import ABC, abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        return "The car is driving"

class Bike(Vehicle):
    def move(self):
        return "The bike is cycling"
    
class Truck(Vehicle):
    def move(self):
        return "The truck is hauling"

def test_vehicles(vehicles: list[Vehicle]):
    for vehicle in vehicles:
        print(vehicle.move())

def main():
    car = Car()
    bike = Bike()
    truck = Truck()

    vehicles = [car, bike, truck]

    test_vehicles(vehicles)


if __name__ == "__main__":
    main()