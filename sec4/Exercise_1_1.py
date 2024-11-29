import threading
class SingletonGenerator:

    _instance = None

    def __new__(cls, *args):
        # Implement the singleton pattern
        if not cls._instance:
            cls._instance = super().__new__(cls, *args)
        return cls._instance

    def __init__(self):
        # Initialize an empty list
        if not hasattr(self, "sequence"):  # solo inicializa la lista si no existe
            self.sequence = [0]

    def append_number(self, number):
        self.sequence.append(number)

    def getnextnumber(self):
        last_number = self.sequence[len(self.sequence) - 1]
        new_number = last_number + 1
        self.append_number(new_number)
        return new_number


sequence_1 = SingletonGenerator()
n_1 = sequence_1.getnextnumber()
print(n_1)
n_2 = sequence_1.getnextnumber()
print(n_2)


