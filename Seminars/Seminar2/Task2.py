# 2. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
#     - Для n = 6: [4, 7, 10, 13, 16, 19]

def task_2(n):
    result=[]
    for i in range(1,n+1):
        result.append(3 * i  + 1)
    print(result)

n = int(input())
task_2(n)
