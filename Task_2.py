 # Дз 1. Задача 4. 
# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

# print('Введите номер четверти от 1 до 4: ')
# n = int(input())

# if n == 1:
#      print('x и y > 0')
# if n == 2:
#      print('x < 0 и y > 0')
# if n == 3:
#      print('x и y < 0')
# if n == 4:
#      print('x > 0 и y < 0')

# Новое решение

slovar = {'1':'x и y > 0', '2':'x < 0 и y > 0', '3':'x и y < 0', '4':'x > 0 и y < 0'}
print((lambda n: slovar[n])(input('Введите номер четверти от 1 до 4: ')))