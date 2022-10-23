#  1. Вычислить число пи c заданной точностью *d*
#     *Пример:*
#      - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# d = int(input('Задайте точность числа Pi: '))
import time

tic = time.perf_counter()
print('До какого знака привести число Pi' 
        '(10^{-1} ≤ d ≤10^{-10})?')
num = int(input(': '))
iteration = 1
for i in range(num+1):
    iteration = iteration * 10
pi_in_iteration = 0
for n in range(iteration):
    pi_in_iteration = (pi_in_iteration + ((1 / (2 * n + 1)) * (-1) ** n))
pi = pi_in_iteration * 4
pi_str = str(pi)
print(f'pi = [{pi_str[:num + 2]}]{pi_str[num + 2:]}\nприведено до {num} знака после запятой')
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.2f} секунд")
