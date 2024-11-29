from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):
    # Implement the move method for the Car class
    def move(self):
        return "The car is driving."

class Bicycle(Vehicle):
    # Implement the move method for the Bicycle class
    def move(self):
        return "The bicycle is pedaling."

class Boat(Vehicle):
    # Implement the move method for the Boat class
    def move(self):
        return "The boat is sailing."
    

def start_vehicle(vehicle):
    # Call the move method of the given vehicle object and print the returned string
    print(vehicle.move())
    

# Test your implementation
car = Car()
bicycle = Bicycle()
boat = Boat()

start_vehicle(car)
start_vehicle(bicycle)
start_vehicle(boat)
