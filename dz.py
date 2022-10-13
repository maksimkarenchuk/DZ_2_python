# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11


# number = input('Введите вещественное число: ')
# sum_number = 0
# for i in number:
#     if i != '.':
#         sum_number += int(i)
# print(sum_number)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#
# Пример:- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


# number = int(input('Введите число: '))
# fac = 1
# for i in range(1, number+1):
#     fac *= i
#     print(fac, end=' ')


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#
# # Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
#
# n = int(input('Введите число: '))
# result = 0
# sum = 0
# for i in range(1, n + 1):
#     result =round(((1 + (1 / i)) ** i), 2)
#     sum += result
# print(f'Сумма чисел {sum}')



def intersection_list(list1, list2):
    list3 = [value for value in list1 if value in list2]
    return list3
#
#
# # Driver Code
list1 = [1, 2, 3, 2, 0]
list2 = [5, 1, 2, 7, 3, 2]
print(intersection_list(list1, list2))
