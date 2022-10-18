# time 51:37
itog = set()
 
 
def f(lst, cur=None, i=0):
 
    cur = [] if cur is None else cur
    if i == len(lst):
        if len(cur) > 1:
            itog.add(tuple(cur))
        return
    f(lst, cur, i + 1)
    for index in range(i, len(lst)):
        if cur and cur[-1] < lst[index]:
            f(lst, cur + [lst[index]], index + 1)
        elif not cur:
            f(lst, [lst[index]], index + 1)
 
 
f([1, 5, 2, 3, 4, 6, 1, 7])
print(len(itog))
print(max(itog, key=lambda x: len(x)))
print(*sorted(itog), sep='\n')
