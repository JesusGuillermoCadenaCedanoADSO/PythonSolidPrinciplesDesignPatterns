from abc import ABC, abstractmethod
from enum import Enum

# Step 0: Create an enumeration for vehicle types
class VehicleType(Enum):
    CAR = "Car"
    MOTORCYCLE = "Motorcycle"
    BICYCLE = "Bicycle"
    PLANE = "Plane"


# Step 1: Create an abstract Vehicle class
class Vehicle(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass


# Step 2: Create concrete vehicle classes
class Car(Vehicle):
    # Implement the get_name() method
    def get_name(self):
        return VehicleType.CAR.value
    #pass


class Motorcycle(Vehicle):
    # Implement the get_name() method
    def get_name(self):
        return VehicleType.MOTORCYCLE.value
    #pass


class Bicycle(Vehicle):
    # Implement the get_name() method
    def get_name(self):
        return VehicleType.BICYCLE.value
    #pass


class VehicleFactory:
    def create_vehicle(self, vehicle_type: VehicleType) -> Vehicle:
        # Implement the logic to create a vehicle based on the vehicle_type parameter
        if vehicle_type ==VehicleType.CAR:
           return Car()
        elif vehicle_type==VehicleType.MOTORCYCLE:
            return Motorcycle()
        elif vehicle_type==VehicleType.BICYCLE:
            return Bicycle()
        else:
            raise ValueError("Invalid vehicle type")

        # pass


# Step 4: Test the VehicleFactory class
def main():
    vehicle_factory = VehicleFactory()

    # Test the VehicleFactory by creating different types of vehicles
    car = vehicle_factory.create_vehicle(VehicleType.CAR)
    print(car.get_name())

    motorcycle = vehicle_factory.create_vehicle(VehicleType.MOTORCYCLE)
    print(motorcycle.get_name())

    bicycle = vehicle_factory.create_vehicle(VehicleType.BICYCLE)
    print(bicycle.get_name())

    # plane = vehicle_factory.create_vehicle(VehicleType.PLANE)
    # print(plane.get_name())


if __name__ == "__main__":
    main()
