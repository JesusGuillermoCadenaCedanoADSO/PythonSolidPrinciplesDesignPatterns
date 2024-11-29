#from fractions import Fraction


def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def simplificar_fraccion(a, b):
    divisor_comun = mcd(a, b)
    numerador_simplificado = a // divisor_comun
    denominador_simplificado = b // divisor_comun
    return numerador_simplificado, denominador_simplificado


class Fraction:
    def __init__(self, numerator, denominator):
        # Initialize the numerator and denominator properties
        # Check that the denominator is non-zero
        self.numerator = int(numerator)
        if int(denominator):
            self.denominator = denominator
        else:
            raise ValueError("Denominator cannot be zero.")

    def add(self, other):
        # Add the current fraction and the other fraction
        # Return the result as a new Fraction object
        result_numerator = self.numerator * other.denominator + self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def subtract(self, other):
        # Subtract the other fraction from the current fraction
        # Return the result as a new Fraction object
        result_numerator = self.numerator * other.denominator - self.denominator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def multiply(self, other):
        # Multiply the current fraction and the other fraction
        # Return the result as a new Fraction object
        result_numerator = self.numerator * other.numerator
        result_denominator = self.denominator * other.denominator
        return Fraction(result_numerator, result_denominator)

    def divide(self, other):
        # Divide the current fraction by the other fraction
        # Check that the other fraction has a non-zero numerator
        # Return the result as a new Fraction object
        if other.numerator == 0:
            raise ValueError("Cannot divide by a fraction with a zero numerator.")
        result_numerator = self.numerator * other.denominator
        result_denominator = self.denominator * other.numerator
        return Fraction(result_numerator, result_denominator)

    def simplify(self):
        # Simplify the current fraction to its simplest form
        # Return a new Fraction object with the simplified numerator and denominator
        simplified = simplificar_fraccion(self.numerator, self.denominator)
        return Fraction(simplified[0], simplified[1])
        

    def __str__(self):
        # Return the string representation of the fraction in the format "numerator/denominator"
        return f"{self.numerator}/{self.denominator}"


# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"
