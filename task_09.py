print('Задача 9. Выражение')


#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64)) 

number_x = int(input('Введите число X: '))
product_numerator = 1
product_denominator = 1

for degree_count in range(6):
    numerator = number_x - ((2 ** (degree_count + 1)) - 1)
    denominator = number_x - (2 ** (degree_count + 1))
    product_numerator *= numerator
    product_denominator *= denominator
fraction = product_numerator / product_denominator
print('Значение выражения равно:', fraction)
