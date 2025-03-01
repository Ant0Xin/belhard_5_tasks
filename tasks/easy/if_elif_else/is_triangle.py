"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
Определяем существование треугольника по трем сторонам.
Отредактировать функцию is_triangle, которая принимает 3 аргумента - три длины
сторон треугольника, таким образом, чтобы она возвращала True, если такой
треугольник может быть, и False, если нет.

У треугольника сумма любых двух сторон должна быть больше третьей.
Иначе две стороны просто "лягут" на третью и треугольника не получится.

ПРИМЕРЫ
--------------------------------------------------------------------------------
is_rectangle(3, 4, 5) -> True
is_rectangle(10, 4, 5) -> False
"""


def is_triangle(side1: int, side2: int, side3: int) -> bool:
    if side1 + side2 > side3 and side1 + side3 > side2 and side3 + side2 > side1:
        return True
    else:
        return False


if __name__ == '__main__':
    side1_val = int(input('Введите длину первой стороны: '))
    side2_val = int(input('Введите длину второй стороны: '))
    side3_val = int(input('Введите длину третьей стороны: '))
    print(f'Треугольник существует: '
          f'{is_triangle(side1_val, side2_val, side3_val)}')
