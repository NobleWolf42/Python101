def answer(x):
    i = 0
    a = 8
    b = 7
    c = 49
    if x == 0:
        a = 0
    elif x == 1:
        a = 8
    else:
        while i+1 != x:
            c = a
            a = (b*7)+a
            b = a - c
            i += 1
    return a

print(answer(1))