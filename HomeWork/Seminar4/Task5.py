# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# polinom1 = ('5x^2 + 3x - 9')
# polinom2 = ('3x^2 - 2x - 5')

# 8x^2 + 1x - 14

НЕТ ЧЕТКОГО АЛГОРИТМА, ЗАДАЧА НЕ РЕШЕНА

f = open('file1.txt', 'r')
polinom_1 = list(f.read().split(' '))
f.close()

f = open('file2.txt', 'r')
polinom_2 = list(f.read().split(' '))
f.close()

print(polinom_1)
print(polinom_2)
print(polinom_1[0])
print(len(polinom_1))

print(f'{(polinom_1[0][len(polinom_1[0])-1])} = {(polinom_2[0][len(polinom_2[0])-1])}') #Проверяем степень монома 
if (polinom_1[0][len(polinom_1[0])-1]) == (polinom_2[0][len(polinom_2[0])-1]) and : #Проверяем степень монома 
    for i in range(len(polinom_1)): # Этим циклом хочу сложить коэффициенты мономов
        for j in range(len(polinom_2)):
            if len(polinom_1[i]) == len (polinom_2[j]):# Проверяю не стоит ли знак в первой ячейке
                
                print((polinom_1[0])[0])
                print((polinom_2[0])[0])
            
                # result_polinom = (int((polinom_1[i])[0])) + (int((polinom_2[j])[0])) #Складываю коэффициенты мономов
                # print(result_polinom)



     
