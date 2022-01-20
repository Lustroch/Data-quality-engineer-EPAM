# Программа будет получать на вход аргументы из командной строки
#
# Аргументы командной строки – коэффициенты и переменная полинома:
#
# P(x)=an⋅xn+an−1⋅xn−1+...+a1⋅x+a0

import argparse

parser = argparse.ArgumentParser(description='Polynomial Functions with Python')

#  Positional arguments
parser.add_argument('-a', type=float, nargs='*', required=True, default=0, dest='ai',
                    help='coefficients ai (float, largest to smallest)')
parser.add_argument('-x', type=float, nargs=1, required=True, default=0, dest='x', help='value x (float)')

#  Optional argument
parser.add_argument('-v', '--verbose', action='store_true', dest='v', default=False,
                    help='outputs a calculated expression "an*xn+...+a1*x+a0*1.0=p"')

args = parser.parse_args()


class Polynomial:
    def __init__(self, coefficient):
        """ input: coefficients are in the form a_n, ...a_1, a_0
        """
        self.coefficients = coefficient  # tuple is turned into a list

    def __str__(self, x2):
        def x_expr(degree):
            if degree == 0:
                res = '*' + str(x2**0)
            elif degree == 1:
                res = '*' + str(x2)
            else:
                res = '*' + str(x2 ** degree)
            return res
        degree = len(self.coefficients) - 1
        res = ""
        for i in range(0, degree+1):
            res += f"{self.coefficients[i]:+.2}{x_expr(degree-i)}"
        return res.lstrip('+')    # removing leading '+'

    def __call__(self, x1):
        res = 0
        for index, coeff in enumerate(self.coefficients[::-1]):
            res += coeff * x1 ** index
        return res


fun = Polynomial(args.ai)


if args.v:
    print(f'{fun.__str__(args.x[0])}={fun.__call__(args.x[0])}')
else:
    print(fun.__call__(args.x[0]))
