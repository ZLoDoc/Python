# n = 10                                                    # разобраться
# fib = [0, 1]
# for i in range(n - 1):
#     fib.append(fib[-2] - fib[-1])
# print(fib)    
# ----------------------------------------------------
# from time import sleep

# with open('new_file','r', encoding='utf-8') as f:
#     lines = f.readlines()

# print(lines) 
# lines[1] = 'Hello!!!\n'

# with open('new_file','w') as f:
#     for line in lines:
#         f.write(line)
# ----------------------------------------------------
# mem = {1: 1, 2: 1}

# def fib(n):
#     if n not in mem:
#         mem[n] = fib(n - 1) + fib(n - 2)
#     return mem[n]

# print(fib(405))
# ----------------------------------------------------
# str_ = 'qwer, dfdfdf, erwrer, werewrm'
# print(str_.split(', '))

# 1. Задайте строку из набора чисел. Напишите программу, 
#   которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.

# numbers = input("Введите строку: ")
# num_list = list(map(int, numbers.split()))
# print(f"min = {min(num_list)}")
# print(f"max = {max(num_list)}")


# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0
#   с помощью математических формул нахождения корней квадратного уравнения

import math

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))

d = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(d)) / (2 * a)
x2 = (-b - math.sqrt(d)) / (2 * a)

print(x1, x2)

# 3. Задайте два числа. Напишите программу, 
# которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = num1
# num4 = num2

# while num1 != 0 and num2 != 0:
#     if num1 > num2:
#         num1 = num1 % num2
#     else:
#         num2 = num2 % num1
# gcd = num1 + num2
# print(abs(num3 * num4) / gcd)