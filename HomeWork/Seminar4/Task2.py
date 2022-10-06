# 2. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
print(" ")
num = int(input('Введите целое число : '))
nums = num
nod = 2    
result = str('')
count = 0
while num != 1:
    if num % nod == 0:
        if count != nod:
            count = nod
            result = result + str(f' {nod},')
        print ("{0:>7} | {1:<4}".format(num, nod))
        num = int(num / nod)
    elif num % nod != 0:
        nod = nod + 1
print (f'Простые множители числа {nums} : {result}')
print(" ")