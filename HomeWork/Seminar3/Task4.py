# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# print(23/2)

def lenght(n): # вычисляем длину двоичного числа
    res = 0
    if n == 0:
        return 1
    while n > 0:
        res+=1
        n = int(n / 2)
    return res

n = int(input('Введите число для конвертации :'))
a = n 
b = n  
binary_list = []
binary_string = ' '
for i in range (int(lenght(n))):
    b = (a%2)
    a = int(a/2)
    binary_list.append(b)
    binary_string=binary_string+str(b)
print(f'{n} = {binary_list[::-1]}')
print(f'{n} = {binary_string[::-1]}')
