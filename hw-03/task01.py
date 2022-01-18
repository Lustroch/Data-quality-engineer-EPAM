# Определите классы исключений PreconditionError и ComplexRootError и напишите функцию solve(a, b, c), которая:

# принимает целые или вещественные коэффициенты (в противном случае возбуждает ошибку TypeError)
# проверяет предусловие a!=0 (в противном случае возбужает PreconditionError)
# решает уравнение с вещественными корнями (в противном случае возбуждает ComplexRootError)
# возвращает кортеж из 1 или 2 корней, упорядоченных по возрастанию
# исключения должны содержать информацию о том, какие аргументы привели к ошибке.


import math


class PreconditionError(Exception):
    def __str__(self):
        return 'Исплючение: нарушение предусловия a!=0'


class ComplexRootError(Exception):
    pass


num_of_errors = 0
mark_of_type_error = False


def solve(a, b, c):
    num_of_arguments_typeerror = []
    type_error(a)
    if mark_of_type_error:
        num_of_arguments_typeerror.append(1)
    type_error(b)
    if mark_of_type_error:
        num_of_arguments_typeerror.append(2)
    type_error(c)
    if mark_of_type_error:
        num_of_arguments_typeerror.append(3)
    if num_of_errors == 1:
        raise TypeError(f"Исключение: неправильные типы: {''.join(map(str, num_of_arguments_typeerror))} аргумент")
    elif num_of_errors > 1:
        raise TypeError(f"Исключение: неправильные типы: {', '.join(map(str, num_of_arguments_typeerror))} аргументы")

    if a == 0:
        raise PreconditionError

    discr = b ** 2 - 4 * a * c
    if discr > 0:
        x1 = (-b - math.sqrt(discr)) / (2 * a)
        x2 = (-b + math.sqrt(discr)) / (2 * a)
        print(x1, x2)
    elif discr == 0:
        x = -b / (2 * a)
        print(x)
    else:
        raise ComplexRootError(f'Исключение: комплексные корни с аргументами: {a}, {b}, {c}')


def type_error(input_value):
    if isinstance(input_value, int) or isinstance(input_value, float):
        global mark_of_type_error
        mark_of_type_error = False
    else:
        global num_of_errors
        num_of_errors += 1
        mark_of_type_error = True
        return


solve('1', '2', '3')
