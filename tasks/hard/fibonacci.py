"""
Вычисление n-го числа ряда Фибоначчи с помощью цикла while

Присвоить переменным fib1 и fib2 значения двух первых элементов ряда,
то есть присвоить переменным единицы.

Запросить у пользователя номер элемента, значение которого он хочет получить.
Присвоить номер переменной n.

Выполнять следующие действия n - 2 раз, так как первые два элемента уже учтены:
Сложить fib1 и fib2,
присвоив результат переменной для временного хранения данных, например, fib_sum.

Переменной fib1 присвоить значение fib2.
Переменной fib2 присвоить значение fib_sum.
Вывести на экран значение fib2.

Примечание. Если пользователь вводит 1 или 2, тело цикла ни разу не выполняется,
на экран выводится исходное значение fib2.

Числа Фибоначчи – это ряд чисел, в котором
каждое следующее число равно сумме двух предыдущих: 1, 1, 2, 3, 5, 8, 13, ... .
Иногда ряд начинают с нуля: 0, 1, 1, 2, 3, 5, ... .
В данном случае мы будем придерживаться первого варианта.
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("n must highe than 0")
    elif n == 1 or n == 2:
        return 1
    fib1 = 1
    fib2 = 1
    for _ in range(n - 2):
        fib1, fib2 = fib2, fib1 + fib2
    return fib2


if __name__ == '__main__':
    assert fibonacci(8) == 21
    print('Решено!')
