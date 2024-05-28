from math import e, pi, factorial, sin, cos, tan, asin, acos, atan, log

x = float(input('Введите значение: '))
operator = str(input('Оператор: '))
arithmetic_operators = {'+', '-', '*', '/', '**'}
valid_operators = arithmetic_operators | {'factorial', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'log'}
while operator != '=':
    if operator in valid_operators:
        if operator in arithmetic_operators:
            y = float(input('Введите следующее значение: '))
            if operator == '+':
                x += y
                operator = str(input('Оператор: '))
            elif operator == '-':
                x -= y
                operator = str(input('Оператор: '))
            elif operator == '*':
                x *= y
                operator = str(input('Оператор: '))
            elif operator == '/':
                x /= y
                operator = str(input('Оператор: '))
            elif operator == '**':
                x **= y
                operator = str(input('Оператор: '))
        elif operator == 'factorial':
            if x == int(x):
                x = factorial(int(x))
                operator = str(input('Оператор: '))
            else:
                print('Нельзя применять факториал по отношению к числам с плавающей точкой')
                operator = str(input('Оператор: '))
        elif operator == 'sin':
            x = sin(x)
            operator = str(input('Оператор: '))
        elif operator == 'cos':
            x = cos(x)
            operator = str(input('Оператор: '))
        elif operator == 'tan':
            x = tan(x)
            operator = str(input('Оператор: '))
        elif operator == 'asin':
            x = asin(x)
            operator = str(input('Оператор: '))
        elif operator == 'acos':
            x = acos(x)
            operator = str(input('Оператор: '))
        elif operator == 'atan':
            x = atan(x)
            operator = str(input('Оператор: '))
        elif operator == 'log':
            y = float(input('Введите значение основания: '))
            if y > 0 and y != 1:
                x = log(x, y)
                operator = str(input('Оператор: '))
            else:
                print('Основание логарифма должно быть положительным числом, отличным от 1')
                operator = str(input('Оператор: '))
    else:
        print('Error')
        operator = str(input('Оператор: '))
print(x)