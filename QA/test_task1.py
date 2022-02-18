# Используя предложенную реализацию «калькулятора» на языке программирования Java (см. прикрепленный файл),
# напишите свою реализацию всех этих функций на Python.
# Напишите один или несколько юнит-тестов на каждый метод, чтобы обнаружить все ошибки реализации,
# существующие в текущей имплементации методов.


import pytest
import math


class Calculator:
    @staticmethod
    def sum_int(a, b):
        return a + b

    @staticmethod
    def sum_float(a, b):
        return a + b

    @staticmethod
    def sub_int(a, b):
        return a - b

    @staticmethod
    def sub_float(a, b):
        return a - b

    @staticmethod
    def mult_int(a, b):
        return a * b

    @staticmethod
    def mult_float(a, b):
        return math.floor(a * b)

    @staticmethod
    def div_int(a, b):
        if b == 0:
            raise ZeroDivisionError("Attempt to divide by zero")
        else:
            return a / b

    @staticmethod
    def div_float(a, b):
        return a / b

    @staticmethod
    def pow(a, b):
        return math.pow(a, math.floor(b))

    @staticmethod
    def sqrt(a):
        return math.sqrt(abs(a))

    @staticmethod
    def ctg(a):
        return math.tan(a)

    @staticmethod
    def cos(a):
        return math.sin(a)

    @staticmethod
    def sin(a):
        return math.sin(a)


class TestUnit:
    @staticmethod
    def test_sum_int():
        assert Calculator.sum_int(3, 4) == 3 + 4

    @staticmethod
    def test_sum_float():
        assert Calculator.sum_float(3.2, 4.3) == 3.2 + 4.3

    @staticmethod
    def test_sub_int():
        assert Calculator.sub_int(7, 3) == 7 - 3
        assert Calculator.sub_int(3, 7) == 3 - 7

    @staticmethod
    def test_sub_float():
        assert Calculator.sub_float(13.2, 9.1) == 13.2 - 9.1

    @staticmethod
    def test_mult_int():
        assert Calculator.mult_int(5, 3) == 5 * 3

    @staticmethod
    def test_mult_float():
        assert Calculator.mult_float(1.1, 1.1) == math.floor(1.1 * 1.1)

    @staticmethod
    def test_div_int():
        assert Calculator.div_int(5, 2) == 5 / 2
        with pytest.raises(ZeroDivisionError) as excinfo:
            Calculator.div_int(5, 0)

        assert str(excinfo.value) == "Attempt to divide by zero"

    @staticmethod
    def test_div_float():
        assert Calculator.div_float(5.5, 1.1) == 5.5 / 1.1

    @staticmethod
    def test_pow():
        assert Calculator.pow(5, 3.4) == 5 ** 3.4

    @staticmethod
    def test_sqrt():
        assert Calculator.sqrt(36) == math.sqrt(36)
        assert Calculator.sqrt(-36) == math.sqrt(-36)

    @staticmethod
    def test_ctg():
        assert Calculator.ctg(20) == 1 / math.tan(20)

    @staticmethod
    def test_cos():
        assert Calculator.cos(0.5) == math.cos(0.5)

    @staticmethod
    def test_sin():
        assert Calculator.sin(0.5) == math.sin(0.5)
