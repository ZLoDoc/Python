# 4. Напишите программу, которая по заданному номеру четверти, 
#    показывает диапазон возможных координат точек в этой четверти (x и y).

num = int(input('Введите № четверти в которой находится точка : '))
if num <1 or num > 4:
    print(f'В декартовой плоскости всего четыре четверти')
if num == 1:
    print(f'В данной четверти возможны значения по Х от 0 до + бесконечности, по У от 0 до + бесконечности')
if num == 2:
    print(f'В данной четверти возможны значения по Х от 0 до - бесконечности, по У от 0 до + бесконечности')
if num == 3:
    print(f'В данной четверти возможны значения по Х от 0 до - бесконечности, по У от 0 до - бесконечности')
if num == 4:
    print(f'В данной четверти возможны значения по Х от 0 до + бесконечности, по У от 0 до - бесконечности')    