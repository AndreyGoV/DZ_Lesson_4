'''
Задача №3795. Принадлежит ли точка области

Проверьте, принадлежит ли точка данной закрашенной области.

Если точка принадлежит области (область включает границы),
выведите слово YES, иначе выведите слово NO.

Решение должно содержать функцию IsPointInArea(x, y),
возвращающую True, если точка принадлежит области и False,
если не принадлежит. Основная программа должна считать координаты точки,
вызвать функцию IsPointInArea и в зависимости от возвращенного значения
вывести на экран необходимое сообщение.

Функция IsPointInArea не должна содержать инструкцию if.

Входные данные
Вводится два действительных числа.

Выходные данные
Выведите ответ на задачу.
'''

# Круг
xc = -1
yc = 1
r = 2
# Линия 1
x1_line1 = -3
y1_line1 = -4
x2_line1 = 1
y2_line1 = 4
# Линия 2
x1_line2 = -3
y1_line2 = -4
x2_line2 = 1
y2_line2 = 4

def line1(x, y):
    point = (x - x1_line1) * (y2_line1 - y1_line1) - (y - y1_line1) * (x2_line1 - x1_line1)
    if point < 0: return 'left'
    elif point >= 0: return 'right'
    elif point == 0: return 'on'

def line2(x, y):
    point = (x - x1_line2) * (y2_line2 - y1_line2) - (y - y2_line2) * (x2_line2 - x1_line2)
    if point < 0: return 'left'
    elif point > 0: return 'right'
    elif point == 0: return 'on'

def IsPointInSquare(x, y):
    result = (line1(x, y), line2(x, y))
    if (xc - x) ** 2 + (yc -y) ** 2 <= r ** 2:
        if result == ('left', 'right') or result == ('on', 'on'):
            return True
        else:
            return False
    else:
        if result == ('right', 'left') or result == ('on', 'on'):
            return True
        else:
            return False

print(IsPointInSquare(-1, 1))