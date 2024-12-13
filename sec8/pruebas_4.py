from abc import ABC, abstractmethod
# Principio de sustitucion de liskov
# ejemplo tomado de : https://dev.to/victorpinzon198/solid-principio-de-sustitucion-de-liskov-4hne


class CuentaBancaria(ABC):

    @abstractmethod
    def depositar(self, monto):
        pass


class CuentaBancariaRetirable(CuentaBancaria):

    @abstractmethod
    def retirar(self, monto):
        pass


class CuentaBancariaBasica(CuentaBancariaRetirable):
    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        if self.saldo < monto:
            return False
        else:
            self.saldo -= monto
            return True

    def __str__(self):
        return f"CuentaBancariaBasica - Saldo: {self.saldo:.2f}"

class CuentaBancariaPremium(CuentaBancariaRetirable):
    def __init__(self,saldo,puntosPrefiero=1):
        self.saldo = saldo
        self.puntosPrefiero = puntosPrefiero

    def depositar(self, monto):
        self.saldo += monto
        self.incrementarPuntosPrefiero()

    def retirar(self, monto):
        if self.saldo < monto:
            return False
        else:
            self.saldo -= monto
            self.incrementarPuntosPrefiero()
            return True

    def incrementarPuntosPrefiero(self):
        self.puntosPrefiero += 1

    def __str__(self):
        return f"CuentaBancariaPremium - Saldo: {self.saldo:.2f}, Puntos Prefiero: {self.puntosPrefiero}"

class CuentaBancariaLargoPlazo(CuentaBancaria):
    def __init__(self,saldo):
        self.saldo = saldo

    def depositar(self, monto):
        self.saldo += monto

    def __str__(self):
        return f"CuentaBancariaLargoPlazo - Saldo: {self.saldo:.2f}"

class ServicioRetiro():
    def __init__(self, monto_gasto_admon=25):
        self.monto_gasto_admon = monto_gasto_admon

    def cargar_debitar_cuentas(self):
        ctaBasica = CuentaBancariaBasica(0)
        ctaBasica.depositar(100)
        print(ctaBasica)
        ctaPremium = CuentaBancariaPremium(0)
        ctaPremium.depositar(200)
        print(ctaPremium)
        cuentas = []
        cuentas.append(ctaBasica)
        cuentas.append(ctaPremium)
        self.debitarGastosAdmon(cuentas)

    def debitarGastosAdmon(self,lista_cuentas):
        for cuenta in lista_cuentas:
            cuenta.retirar(self.monto_gasto_admon)
            print(cuenta)


nuevo_servicio = ServicioRetiro()
nuevo_servicio.cargar_debitar_cuentas()





