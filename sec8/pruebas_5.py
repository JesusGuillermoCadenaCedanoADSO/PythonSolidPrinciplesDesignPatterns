from abc import ABC, abstractmethod

class IOvenBakedPizzaShop(ABC):
    @abstractmethod
    def get_oven_baked_pizza(self):
        pass

class IClassicalBakedPizzaShop(ABC):
    @abstractmethod
    def get_classical_baked_pizza(self):
        pass

class IElectricOvenBakedPizzaShop(ABC):
    @abstractmethod
    def get_electric_oven_baked_pizza(self):
        pass

class IPizzaPocketSquareBakedPizzaShop(ABC):
    @abstractmethod
    def get_pizza_pocket_square_baked_pizza(self):
        pass

class IDrinkShop(ABC):
    @abstractmethod
    def get_drinks(self):
        pass

class TraditionalPizzeria(IOvenBakedPizzaShop, IClassicalBakedPizzaShop, IDrinkShop):
    def get_oven_baked_pizza(self):
        # Implementación específica para una pizzería tradicional
        return "Oven-baked pizza from Traditional Pizzeria"

    def get_classical_baked_pizza(self):
        # Implementación específica para una pizzería tradicional
        return "Classical-baked pizza from Traditional Pizzeria"

    def get_drinks(self):
        # Implementación específica para una pizzería tradicional
        return "Drinks from Traditional Pizzeria"

class NewWavePizzeria(IElectricOvenBakedPizzaShop, IPizzaPocketSquareBakedPizzaShop, IDrinkShop):
    def get_electric_oven_baked_pizza(self):
        # Implementación específica para una nueva ola de pizzerías
        return "Electric oven-baked pizza from New Wave Pizzeria"

    def get_pizza_pocket_square_baked_pizza(self):
        # Implementación específica para una nueva ola de pizzerías
        return "Pizza pocket square-baked from New Wave Pizzeria"

    def get_drinks(self):
        # Implementación específica para una nueva ola de pizzerías
        return "Drinks from New Wave Pizzeria"

# Ejemplo de uso
if __name__ == "__main__":
    traditional = TraditionalPizzeria()
    new_wave = NewWavePizzeria()

    # Probar Traditional Pizzeria
    print(traditional.get_oven_baked_pizza())
    print(traditional.get_classical_baked_pizza())
    print(traditional.get_drinks())

    # Probar New Wave Pizzeria
    print(new_wave.get_electric_oven_baked_pizza())
    print(new_wave.get_pizza_pocket_square_baked_pizza())
    print(new_wave.get_drinks())
    print(new_wave.get_oven_baked_pizza)
