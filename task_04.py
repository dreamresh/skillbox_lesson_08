print('Задача 4. Отрезок')

# Напишите программу,
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

first_number = int(input('Введите значение a - начало отрезка: '))
second_number = int(input('Введите значение b - конец отрезка: '))
step = int(input('Введите значение кратности: '))
summ, count_number = 0, 0
for count in range(first_number, second_number + 1):
    if count % step == 0:
        count_number += 1
        summ += count
arithmetic_mean = summ / count_number
print('Среднее арифметическое чисел кратных', step,
      'на отрезке [' + str(first_number) + ':' + str(second_number) + '] равно:', arithmetic_mean)
