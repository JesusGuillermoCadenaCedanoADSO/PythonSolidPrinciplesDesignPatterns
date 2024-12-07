from abc import ABC, abstractmethod


class Computer:
    def __init__(self):
        # Initialize the attributes
        self.processor = ''
        self.memory = ''
        self.storage = ''
        self.graphics_card = ''
        self.operating_system = ''
        self.extras = ''


class ComputerBuilder(ABC):

    @abstractmethod
    def add_processor(self, value, key):
        pass

    @abstractmethod
    def add_memory(self, value, key):
        pass

    @abstractmethod
    def add_storage(self, value, key):
        pass

    @abstractmethod
    def add_graphics_card(self, value, key):
        pass

    @abstractmethod
    def add_operating_system(self, value, key):
        pass

    @abstractmethod
    def add_extras(self, value, key):
        pass


class CustomComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = Computer()

    # Override abstract methods and set Computer attributes
    def add_processor(self, value, key):
        if key == 'processor':
            self.computer.processor = value

    def add_memory(self, value, key):
        if key == 'memory':
            self.computer.memory = value

    def add_storage(self, value, key):
        if key == 'storage':
            self.computer.storage = value

    def add_graphics_card(self, value, key):
        if key == 'graphics_card':
            self.computer.graphics_card = value

    def add_operating_system(self, value, key):
        if key == 'operating_system':
            self.computer.operating_system = value

    def add_extras(self, value, key):
        if key == 'extras':
            self.computer.extras = value


class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder
        # Initialize the builder instance

    def build_computer(self, specs):
        # Call the add_* methods of the builder with the specs
        for key, value in specs.items():
            self.builder.add_processor(value, key)
            self.builder.add_memory(value, key)
            self.builder.add_storage(value, key)
            self.builder.add_graphics_card(value, key)
            self.builder.add_operating_system(value, key)
            self.builder.add_extras(value, key)


# Helper function to test the computer building process
def test_computer_building(specs, expected_output):
    builder = CustomComputerBuilder()
    director = ComputerDirector(builder)
    director.build_computer(specs)
    computer = builder.computer
    assert computer.__dict__ == expected_output, f"Expected {expected_output}, but got {computer.__dict__}"


# Test cases
test_specs = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

expected_output = {
    'processor': 'Intel Core i5',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'Integrated',
    'operating_system': 'Windows 11',
    'extras': ['Wi-Fi']
}

test_computer_building(test_specs, expected_output)

print("All tests passed!")
