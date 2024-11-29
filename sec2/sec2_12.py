from abc import ABC, abstractmethod

# Define an abstract class 'Animal'
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    # Make the 'description' method abstract but provide a basic implementation
    @abstractmethod
    def description(self):
        print(f"{self.__class__.__name__} says: {self.sound()}")

# Define a concrete class 'Dog' that inherits from 'Animal'
class Dog(Animal):
    def sound(self):
        return "Woof!"

    # Override the 'description' method in the 'Dog' class and call the base class implementation
    def description(self):
        return super().description()

# Define a concrete class 'Cat' that inherits from 'Animal'
class Cat(Animal):
    def sound(self):
        return "Meow!"
    
    # Override the 'description' method in the 'Cat' class and call the base class implementation
    def description(self):
        return super().description()

dog = Dog()
dog.description()

cat = Cat()
cat.description()

