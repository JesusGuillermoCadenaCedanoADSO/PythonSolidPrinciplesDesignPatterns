# Interface separation principle(ISP)
# Each class (printer, scanner, copier) implementing this interface must provide
# implementations for all methods, even those that are not relevant to its functionality
# this violates the ISP, wich states that clients should not be forced to depend on
# interfaces they do not use.

class IMultiFunctionDevice:
    def print(self):
        pass
    
    def scan(self):
        pass
    
    def copy(self):
        pass
    
    def fax(self):
        pass
     
class Printer(IMultiFunctionDevice):
    def print(self):
        print("Printing...")

class Scanner(IMultiFunctionDevice):
    def scan(self):
        print("Scanning...")

class Copier(IMultiFunctionDevice):
    def copy(self):
        print("Copying...")

# correction
# The refactored solution breaks the single IMultiFunctionDevice interface into smaller,
# more specific interfaces: IPrinter, IScanner, ICopier.
# Each class now only needs to implement the methods relevant to its functionality.
# This adheres to the ISP because the interfaces are now more focused, making the code
# more maintainable and easier to understand.

class IPrinter:
    def print(self):
        pass

class IScanner:
    def scan(self):
        pass

class ICopier:
    def copy(self):
        pass

class IFax:
    def fax(self):
        pass
 
class Printer(IPrinter):
    def print(self):
        print("Printing...")

class Scanner(IScanner):
    def scan(self):
        print("Scanning...")

class Copier(ICopier):
    def copy(self):
        print("Copying...")