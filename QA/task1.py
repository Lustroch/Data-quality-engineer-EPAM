import pytest
from unittest import TestCase
import math

class Calculator:
    def sum_int(self, a, b):
        return a + b

    def sum_float(self, a, b):
        return a + b

    def sub_int(self, a, b):
        return a - b

    def sub_float(self, a, b):
        return a - b

    def mult_int(self, a, b):
        return a * b

    def mult_float(self, a, b):
        return math.floor(a * b)

    def div_int(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Attempt to divide by zero")
        else:
            return a / b

    def div_float(self, a, b):
        return a / b

    def pow(self, a, b):
        return math.pow(a, math.floor(b))

    def sqrt(self, a):
        return math.sqrt(abs(a))

    def ctg(self, a):
        return math.tan(a)

    def cos(self, a):
        return math.sin(a)

    def sin(self, a):
        return math.sin(a)


class CalculatorTest(TestCase):
    def test_sum_int(self):
        assert Calculator.sum_int(self, 3, 4) == 3 + 4

    def test_sum_float(self):
        assert Calculator.sum_float(self, 3.2, 4.3) == 3.2 + 4.3

    def test_sub_int(self):
        assert Calculator.sub_int(self, 7, 3) == 7 - 3
        assert Calculator.sub_int(self, 3, 7) == 3 - 7

    def test_sub_float(self):
        assert Calculator.sub_float(self, 13.2, 9.1) == 13.2 - 9.1

    def test_mult_int(self):
        assert Calculator.mult_int(self, 5, 3) == 5 * 3

    def test_mult_float(self):
        assert Calculator.mult_float(self, 1.1, 1.1) == math.floor(1.1 * 1.1)

    def test_div_int(self):
        assert Calculator.div_int(self, 5, 2) == 5 / 2
        with pytest.raises(ZeroDivisionError) as excinfo:
            Calculator.div_int(self, 5, 0)

        assert str(excinfo.value) == "Attempt to divide by zero"

    def test_div_float(self):
        assert Calculator.div_float(self, 5.5, 1.1) == 5.5 / 1.1

    def test_pow(self):
        assert Calculator.pow(self, 5, 3.4) == 5 ** 3.4

    def test_sqrt(self):
        assert Calculator.sqrt(self, 36) == math.sqrt(36)
        assert Calculator.sqrt(self, -36) == math.sqrt(-36)

    def test_ctg(self):
        assert Calculator.ctg(self, 20) == 1 / math.tan(20)

    def test_cos(self):
        assert Calculator.cos(self, 0.5) == math.cos(0.5)

    def test_sin(self):
        assert Calculator.sin(self, 0.5) == math.sin(0.5)
