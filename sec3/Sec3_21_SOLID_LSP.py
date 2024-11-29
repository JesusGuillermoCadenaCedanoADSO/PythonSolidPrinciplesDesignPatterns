# LISKOV SUBSTITUTION PRINCIPLE
# If we were to use the penguin class in a context where a bird is expected,
# we might get unexpected behavior due to overriden fly() method.This can lead
# to errors and inconsistencies in the code

class Bird:
    def fly(self):
        print("I can fly")

class Penguind(Bird):
    def fly(self):
        print("I can't fly")


# correction
# This adheres to the LSP because any subclasses of Bird can now be substituted
# without altering the correctness of the program. The code is more robust and less
# prone to errors.

class Bird:
    def fly(self):
        pass

class FlyingBird(Bird):
    def fly(self):
        print("I can fly")

class NonFlyingBird(Bird):
    def fly(self):
        print("I can't fly")


        