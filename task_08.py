print('Задача 8. Сумма ряда')

# Дано  N.
# Напишите программу для вычисления следующей суммы ряда (начиная с единицы)

# S = 1 - 1/2 + 1/4 - 1/8 + … (-1)**N * 1/2**N
natural_number = int(input('Введите натуральное число: ')) # ввод числа
denominator = 2 # знаменатель
denominator_degree = 0 # степень для знаменателя
switch_sign = -1 # переключатель знака дроби
fraction_sign = 1 # знак
fraction_value = 0 # значение дроби
total_summ = 0 # сумма общая

for denominator_degree in range(natural_number):
    fraction_value = ((1 / denominator ** denominator_degree) * fraction_sign)
    total_summ += fraction_value
    fraction_sign *= switch_sign

total_summ += (-1 ** natural_number) * (1 / denominator ** natural_number)
print('Сумма ряда для натурального числа', natural_number, 'равна', total_summ)