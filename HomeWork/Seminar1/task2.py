# 2. Напишите программу для. проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

X = [True, False]
Y = [True, False]
Z = [True, False]

for x in X :
    for y in Y:
        for z in Z:
            expression1 = not(x or y or z) 
            expression2 = (not x) and (not y) and (not z)
            print('      ')
            #print(f'x = {x} y = {y} z = {z}')
            print(f'expression1 = {expression1}, expression2 = {expression2}')
            #print('      ')
            if expression1 == expression2:
                print(f'При Х = {x} Y = {y} Z = {z} - утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - истинно')
            else:
                print(f'При Х = {x} Y = {y} Z = {z} - утверждение  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - ложно')
            print('____________________________________________________________________')


#             print('x y z \t¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
# for n in range(64):
#     n = bin(n)[2:].rjust(6, '0')
#     print(n)
    # ------------------------------------------------------
    # x, y, z = int(n[0]), int(n[1]), int(n[2])
    # print(x, y, z, '\t', not(x or y or z) == (not(x) and not(y) and not(z)))
