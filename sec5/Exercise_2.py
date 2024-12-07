from abc import ABC, abstractmethod
from enum import Enum


# Step 0: Create an enumeration for animal types
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"


# Step 1: Create an abstract Animal class
class Animal(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self) -> str:
        pass


# Step 2: Create concrete animal classes
class Dog(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        description = AnimalType.DOG.value + " " + str(self.name) + ":" + str(self.age) + "\n"
        return description



class Cat(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        description = AnimalType.CAT.value + " " + str(self.name) + ":" + str(self.age) + "\n"
        return description


class Fish(Animal):
    # Implement the __init__ and get_info() methods
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_info(self):
        description = AnimalType.FISH.value + " " + str(self.name) + ":" + str(self.age) + "\n"
        return description


# Step 3: Create an AnimalFactory class
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            new_dog = Dog(context["name"], context["age"])
            return new_dog
        elif animal_type == AnimalType.FISH:
            new_fish = Fish(context["name"], context["age"])
            return new_fish
        elif animal_type == AnimalType.CAT:
            new_cat = Cat(context["name"], context["age"])
            return new_cat
        else:
            raise ValueError("Invalid Animal")


# Step 4: Test the AnimalFactory class
def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    dog_context = {"name": "lucas", "age": 15}
    dog = animal_factory.create_animal(AnimalType.DOG, dog_context)
    print(dog.get_info())

    cat_context = {"age": 5, "name": "FUZZ"}
    cat = animal_factory.create_animal(AnimalType.CAT, cat_context)
    print(cat.get_info())

    fish_context = {"age": 2, "name": "clown"}
    fish = animal_factory.create_animal(AnimalType.FISH, fish_context)
    print(fish.get_info())


if __name__ == "__main__":
    main()
