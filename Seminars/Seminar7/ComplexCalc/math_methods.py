def add(a,b):
    if type(a) is tuple and type(b) is tuple and len(a) == 2 and len(b) == 2:
        ar,ai = a
        br,bi = b
        return (ar + br, ai + bi)
    elif len(a) == 1 and len(b) == 1 and (type(a) is int or type(a) is float) and (type(b) is int or type(b) is float):
        return a+b
    else:
        return -1
    
def sub(a,b):
    if type(a) is tuple and type (b) is tuple and len(a) == 2 and len(b) == 2:
        ar,ai = a
        br,bi = b
        return (ar - br, ai - bi)
    elif len(a) == 1 and len(b) == 1:
        return a - b
    else:
        return -1

def mult(a,b):
    if type(a) is tuple and type (b) is tuple and len(a) == 2 and len(b) == 2:
        ar,ai = a
        br,bi = b
        return (ar * br, ai * bi)
    elif len(a) == 1 and len(b) == 1  :
        return a * b
    else:
        return -1

def dev(a,b):
    if type(a) is tuple and type (b) is tuple and len(a) == 2 and len(b) == 2:
        ar,ai = a
        br,bi = b
        return (ar / br, ai / bi)
    elif len(a) == 1 and len(b) == 1:
        return a / b
    else:
        return -1        