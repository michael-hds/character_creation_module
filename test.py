from math import sqrt


def CalculateSquareRoot(Number):
    """ Вычисляет квадратный корень"""
    return sqrt(Number)


def Calc(your_number):
    if your_number <= 0:
        return 0


message = ('Добро пожаловать в самую лучшую программу для вычисления '
           'квадратного корня из заданного числа')
print(message)
print(f'Мы вычислили квадратный корень из введённого вами числа. '
      f'Это будет: {CalculateSquareRoot(Calc(25.5))}')
