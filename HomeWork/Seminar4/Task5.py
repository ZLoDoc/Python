# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# polinom1 = ('5x^2 + 3x - 9')
# polinom2 = ('3x^2 - 2x - 5')

# 8x^2 + 1x - 14

# НЕТ ЧЕТКОГО АЛГОРИТМА, ЗАДАЧА НЕ РЕШЕНА

f = open('file1.txt', 'r')
polinom_1 = list(f.read().split(' '))
f.close()

f = open('file2.txt', 'r')
polinom_2 = list(f.read().split(' '))
f.close()

# print(polinom_1)
# print(polinom_2)
# print(len(polinom_1))

print(f'степень 1 = {(polinom_1[0][len(polinom_1[0])-1])} \nстепень 2 = {(polinom_2[0][len(polinom_2[0])-1])}') #Проверяем степень монома 
print(f'1 моном 1-го полинома - {polinom_1[0]}')
print(f'1 моном 2-го полинома - {polinom_2[0]}')
if (polinom_1[0][len(polinom_1[0])-1]) == (polinom_2[0][len(polinom_2[0])-1]) : #Проверяем степень монома 
 #если минус ?               
                print((polinom_1[0])[0])
                print((polinom_2[0])[0])
            
                # result_polinom = (int((polinom_1[i])[0])) + (int((polinom_2[j])[0])) #Складываю коэффициенты мономов
                # print(result_polinom)



     
