# 2. Напишите программу для. проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = 234.324
y = 234
z = 35

expression1 = not(x or y or z) 
expression2 = not x and not y and not z
print(f'expression1 = {expression1}, expression2 = {expression2}')
if expression1 == expression2:
    print('Утверждение истино')
else:
    print('Утверждение ложно')
