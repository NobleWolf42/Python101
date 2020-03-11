def answer(x):
    #return len(set(x)-set(x for x in x))
    x = set(x)
    x = list(x)
    y = list(x)
    for i, i1 in enumerate(x):
        for i2 in x[i+1:]:
            if i1 == i2 or i1 == i2[::-1]:
                y.remove(i2)
    return len(y)


hhh = ['cba', 'abc', 'abc', 'bac']
print(answer(hhh))