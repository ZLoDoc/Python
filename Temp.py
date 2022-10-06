print(help(binary_searsh))
# import time

# tic = time.perf_counter()
# def pi():
#     k = float(input("Введите точность от 0,1 до 0,0000000001  :  "))
#     d = int(1/k) * 10
#     print(d)
#     count = -1
#     number = 1
#     while number < d:
#         number *= 10
#         count += 1
#     pi_for = 1 - 1 / 3 + 1 / 5 - 1 / 7 + 1 / 9
#     for i in range(5, d):
#         pi_for = pi_for + (1 / (2 * i + 1)) * (-1) ** i
#     pi_ = pi_for * 4
#     print(f'Точность  pi = {pi_} до {count} знака после запятой')


# pi()
# toc = time.perf_counter()
# print(f"Вычисление заняло {toc - tic:0.4f} секунд")