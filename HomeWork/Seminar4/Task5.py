# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# polinom1 = ('5x^2 + 3x - 9')
# polinom2 = ('3x^2 - 2x - 5')

# 8x^2 + 1x - 14

# with open('file2.txt', 'w') as data:
#     data.write('3x^2 - 2x - 5')
path = 'file1.txt'
data = open(path, 'r')
for line in data:
    polinom1 = line
    print(polinom1)
data.close()
path = 'file2.txt'
data = open(path, 'r')
for line in data:
    polinom2 = line
    print(polinom2)
data.close()

poli_list = []
a = []
b = []

poli_list = (polinom1.split(' '))
# for i in range(len(poli_list)):
#     print(poli_list[i])
a = (poli_list[0])
b = (poli_list[2])

print(f' a = {a}')
print(f' b = {b}')
    # for j in range(len(poli_list[0]))