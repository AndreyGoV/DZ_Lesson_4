def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplicaation(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def exponentiation(num1, num2):
    return num1 ** num2

act = str(input('Введите действие:'))
num1 = float(input('Введите первое число:'))
num2 = float(input('Введите второе число:'))

if act == '+':
    print(addition(num1, num2))
elif act == '-':
    print(subtraction(num1, num2))
elif act == '*':
    print(multiplicaation(num1, num2))
elif act == '/':
    print(division(num1, num2))
elif act == '**':
    print(exponentiation(num1, num2))
