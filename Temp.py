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
binary_list = ''
result_list = ''
for i in range (int(lenght(n))):
    b = (a%2)
    a = int(a/2)
    binary_list.append(b)
result_list = binary_list(::-1)
print(f'{n} = {str(result_list)}')