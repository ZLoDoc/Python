# 4. Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

#     *Пример:*

#     - k=9 => 2*x^9 - 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random

k = int(input('Введите степень многочлена : '))
polinom = '' 
b = 0
c = 0
while k >= 0:
    a = int(random.randrange(0,100))
    sign = random.randrange(-1,2)
    x = (a*sign)**k
    
    if x != 0 and sign > 0 and k !=0 and k !=1 and polinom == '':
        polinom = polinom + (f' {a}*x^{k}')
    elif x != 0 and sign > 0 and k !=0 and k !=1:
        polinom = polinom + (f' + {a}*x^{k}')
    elif x != 0 and sign < 0 and k !=0 and k !=1:
        polinom = polinom + (f' - {a}*x^{k}')

    elif x != 0 and sign > 0 and k == 1:
        b = b + a
    elif x != 0 and sign < 0 and k == 1:
        b = b - a
    elif x != 0 and sign > 0 and k == 0:
        c = c + a
    elif x != 0 and sign < 0 and k == 0:
        c = c - a  
    k = k-1
if b > 0 and b != 0 and polinom == '':
    polinom = polinom + (f' {b}*x')
elif b > 0 and b != 0:
    polinom = polinom + (f' + {b}*x')    
elif b < 0 and b != 0:
    polinom = polinom + (f' - {b*(-1)}*x')
if c > 0 and c != 0 and polinom == '':
    polinom = polinom + (f' {c}')   
elif c > 0 and c != 0 :
    polinom = polinom + (f' + {c}')    
elif c < 0 and c != 0:
    polinom = polinom + (f' - {c*(-1)}')   
print (f'{polinom} = 0')       

    