# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# polinom1 = ('5x^2 + 3x - 9')
# polinom2 = ('3x^2 - 2x - 5')

# 8x^2 + 1x - 14

f = open('file1.txt', 'r')
polinom_1 = list(f.read().split(' '))
f.close()

f = open('file2.txt', 'r')
polinom_2 = list(f.read().split(' '))
f.close()

print(polinom_1)
print(polinom_1[0])
print(len(polinom_1))

