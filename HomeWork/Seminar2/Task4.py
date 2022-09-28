# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
#    Найдите произведение элементов на указанных позициях. 
#    Позиции вводятся пользователем с клавиатуры. 5 2 8

#    [-5 -4 -3 -2 -1 0 1 2 3 4 5] -> -8

# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.

from ast import Break


num = str(input('Введите значение N списка [-N,N] , позицию первого числа и позицию второго числа = '))
number = []
for i in range (len(num)):
    if num[i].isdigit() == True:
        number.append(num[i])     
n = int(number[0])
Pos1=0
row = []
for i in range(-n,n+1):
    row.append(i)
Pos1 = int(number[1])
Pos2 = int(number[2])
Pos1_value = row[Pos1-1]
Pos2_value = row[Pos2-1]
result = (row[Pos1-1])*(row[Pos2-1])
print(f'Произведение чисел {Pos1_value} и {Pos2_value} стоящих на {Pos1} и {Pos2} позициях заданного списка элементов')
print(row)
print(f'Будет {result}')