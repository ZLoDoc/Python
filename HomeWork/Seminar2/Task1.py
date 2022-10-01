# 1. Напишите программу, которая принимает на вход вещественное число и
#  показывает сумму его цифр.
#     *Пример:*
#     - 6782 -> 23
#     - 0,56 -> 11
print('')
number = str(input('Введите строку :'))
sum_of_number=0
for i in range (len(number)):
    if number[i].isdigit():
        s = number[i]
        sum_of_number +=int(s)
    else:
        continue
print (f'Сумма всех цифр в строке {number} = {sum_of_number}')
print('')