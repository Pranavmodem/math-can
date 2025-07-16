class MathOperators:
    """Class containing math operation methods."""

    @staticmethod
    def add(a, b):
        """Return the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a, b):
        """Return the difference of a and b."""
        return a - b

    @staticmethod
    def multiply(a, b):
        """Return the product of a and b."""
        return a * b

    @staticmethod
    def divide(a, b):
        """Return the quotient of a and b. Raises ZeroDivisionError if b is zero."""
        return a / b

    @staticmethod
    def percentage(part, whole):
        """Return the percentage of part out of whole."""
        if whole == 0:
            raise ValueError("Whole cannot be zero.")
        return (part / whole) * 100

    @staticmethod
    def power(a, b):
        """Return a raised to the power of b."""
        return a ** b

    @staticmethod
    def modulus(a, b):
        """Return the remainder of a divided by b."""
        return a % b

    @staticmethod
    def floor_divide(a, b):
        """Return the floor division of a by b."""
        return a // b

    @staticmethod
    def absolute(a):
        """Return the absolute value of a."""
        return abs(a)
