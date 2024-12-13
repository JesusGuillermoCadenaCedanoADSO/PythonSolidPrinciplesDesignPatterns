from abc import ABC, abstractmethod
# Principio de responsabilidad unica

class PizzaShop:
    def __init__(self, name, city, zipCode):
        self.name = name
        self.city = city
        self.zipCode = zipCode

    def getName(self):
        return self.name

    def getCity(self):
        return self.city

    def getzipCode(self):
        return self.zipCode

    def changeAddress(self, new_city, new_zipcode):
        self.city = new_city
        self.zipCode = new_zipcode


new_pizza = PizzaShop("pizzeria", "mexico_city", "001")

print(new_pizza.getName())
new_pizza.changeAddress("bogota", "002")
print(new_pizza.getCity())

# Corrección acorde con principio de responsabilidad unica

class Address:
    def __init__(self, city, ZipCode):
        self.city = city
        self.ZipCode = ZipCode

    def get_city(self):
        return self.city

    def get_ZipCode(self):
        return self.ZipCode

    def changeAddress(self, new_city, new_ZipCode):
        self.city = new_city
        self.ZipCode = new_ZipCode


class PizzaShop2:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def homeDelivery(self):
        pass

    def getName(self):
        return self.name

    def getCity(self):
        return self.address.get_city()

    def getzipCode(self):
        return self.address.get_ZipCode()


new_address = Address("ciudad2", "zip2")

new_pizza_2 = PizzaShop2("pizza_pepperoni", new_address)
print(new_pizza_2.getCity())

# Principio abierto cerrado

class InvoiceService:
    def generateInvoice(self, shop):
        invoice = ""
        if isinstance(shop, A):
            invoice = "format of invoice for A"
        elif isinstance(shop, B):
            invoice = "format of invoice for B"
        elif isinstance(shop, C):
            invoice = "format of invoice for C"
        return invoice


class A(PizzaShop2):
    pass


class B(PizzaShop2):
    pass


class C(PizzaShop2):
    pass


# Ejemplo de uso
address = Address("Bogotá", "110111")
shop_a = A("La Mejor Pizza A", address)
shop_b = B("La Mejor Pizza B", address)
shop_c = C("La Mejor Pizza C", address)

invoice_service = InvoiceService()
print(invoice_service.generateInvoice(shop_a))  # format of invoice for A
print(invoice_service.generateInvoice(shop_b))  # format of invoice for B
print(invoice_service.generateInvoice(shop_c))  # format of invoice for C

# correccion para principio abierto cerrado
# se crea la clase InvoiceStragey  para evitar que InvoiceService maneje tanto la lógica de facturación
# como la referencia a shop y de esta manera no violar el principio de responsabilidad unica.
# La eliminación de la clase InvoiceStrategy puede reducir la flexibilidad del sistema.
# Si en el futuro necesitas cambiar la forma en que se seleccionan las estrategias de facturación,
# podrías encontrar más difícil hacerlo sin una clase de estrategia separada.


class InvoiceStrategy(ABC):
    @abstractmethod
    def generateInvoice(self, shop):
        pass


class InvoiceStrategyA(InvoiceStrategy):
    def generateInvoice(self, shop):
        return "format of invoice for A"


class InvoiceStrategyB(InvoiceStrategy):
    def generateInvoice(self, shop):
        return "format of invoice for B"


class InvoiceStrategyC(InvoiceStrategy):
    def generateInvoice(self, shop):
        return "format of invoice for C"


class InvoiceService:
    def __init__(self, strategy: InvoiceStrategy):
        self.strategy = strategy

    def generateInvoice(self, shop):
        return self.strategy.generateInvoice(shop)


invoice_service_a = InvoiceService(InvoiceStrategyA())
invoice_service_b = InvoiceService(InvoiceStrategyB())
invoice_service_c = InvoiceService(InvoiceStrategyC())

print(invoice_service_a.generateInvoice(shop_a))
print(invoice_service_b.generateInvoice(shop_b))
print(invoice_service_c.generateInvoice(shop_c))


# principio de sustitucion de liskov

class A2(PizzaShop2):
    def homeDelivery(self):
        return "delivery is free for all our customers"


class B2(PizzaShop2):
    def takeaway(self):
        raise Exception("we do not have home delivery service")

# correccion para principio de sustitucion de liskov
# la clase B2 introduce la funcion takeaway la cual  no pertenece a la clase PizzaShop2
# Todas las subclases pueden tener cualquiera de las funciones incluidas en la clase PizzaShop2


class B3(PizzaShop2):
    def homeDelivery(self):
        return "Home delivery is not available"


# Principio de segregacion de interfaces

class IPizzaShop(ABC):
    #traditional pizzerias
    @abstractmethod
    def getOvenBakedPizza(self):
        pass

    @abstractmethod
    def getClassicalBakedPizza(self):
        pass
    # new wave pizzerias
    @abstractmethod
    def getElectricOvenBakedPizza(self):
        pass

    @abstractmethod
    def getPizzaPocketSquareBakedPizza(self):
        pass

    # all pizzerias
    def getDrinks(self):
        pass

class TraditionalPizzeria(IPizzaShop):
    def getOvenBakedPizza(self):
        return True
    def getClassicalBakedPizza(self):
        return True
    def getDrinks(self):
        return True
    def getElectricOvenBakedPizza(self):
        return "We don't do that"
    def getPizzaPocketSquareBakedPizza(self):
        return "We don't do that"

class NewWavePizzeria(IPizzaShop):
    def getElectricOvenBakedPizza(self):
        return True
    def getPizzaPocketSquareBakedPizza(self):
        return True
    def getDrinks(self):
        return True
    def getOvenBakedPizza(self):
        return "We don't do that"
    def getClassicalBakedPizza(self):
        return "We don't do that"

# correccion principio de segregacion de interfaces


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

class TraditionalPizzeria_2(IOvenBakedPizzaShop, IClassicalBakedPizzaShop, IDrinkShop):
    def get_oven_baked_pizza(self):
        # Implementación específica para una pizzería tradicional
        return "Oven-baked pizza from Traditional Pizzeria"

    def get_classical_baked_pizza(self):
        # Implementación específica para una pizzería tradicional
        return "Classical-baked pizza from Traditional Pizzeria"

    def get_drinks(self):
        # Implementación específica para una pizzería tradicional
        return "Drinks from Traditional Pizzeria"

class NewWavePizzeria_2(IElectricOvenBakedPizzaShop, IPizzaPocketSquareBakedPizzaShop, IDrinkShop):
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
    traditional = TraditionalPizzeria_2()
    new_wave = NewWavePizzeria_2()

    # Probar Traditional Pizzeria
    print(traditional.get_oven_baked_pizza())
    print(traditional.get_classical_baked_pizza())
    print(traditional.get_drinks())

    # Probar New Wave Pizzeria
    print(new_wave.get_electric_oven_baked_pizza())
    print(new_wave.get_pizza_pocket_square_baked_pizza())
    print(new_wave.get_drinks())

# principio de inversion de dependencias

class PizzaShop3:
    def getPayment(self):
        pass
    def deliverPizza(self):
        pass

class Customer:
    def makePayment(self):
        pass

    def receivePizza(self):
        pass

class Delivery(PizzaShop3,Customer):
    def __init__(self, customer, pizzashop):
        self.customer = customer
        self.pizzashop = pizzashop
    def deliver(self):
        self.customer.makePayment()
        self.pizzashop.getPayment()
        self.pizzashop.deliverPizza()
        self.customer.receivePizza()

# correccion principio de inversion de dependencias

# se definen interfaces
class IPayment(ABC):
    @abstractmethod
    def makePayment(self):
        pass

class IDelivery(ABC):
    @abstractmethod
    def deliverPizza(self):
        pass

class ICustomer(ABC):
    @abstractmethod
    def receivePizza(self):
        pass

# se implementan las interfaces en las clases concretas

class PizzaShop4(IPayment,IDelivery):
    def makePayment(self):
        print("Payment received by PizzaShop4")

    def deliverPizza(self):
        print("Pizza delivered by PizzaShop4")


class Customer(ICustomer):
    def makePayment(self):
        print("Payment made by Customer")

    def receivePizza(self):
        print("Pizza received by Customer")

class Delivery_2:
    def __init__(self, customer:Customer, pizzashop:PizzaShop4):
        self.pizzashop = pizzashop
        self.customer = customer

    def deliver(self):
        self.customer.makePayment()
        self.pizzashop.makePayment()
        self.pizzashop.deliverPizza()
        self.customer.receivePizza()

# Ejemplo de uso
customer = Customer()
pizzashop = PizzaShop4()
delivery = Delivery_2(customer, pizzashop)
delivery.deliver()

