def answer(names):
    tlist = []
    teml =[]
    for i in names:
        letters = i
        value = 0
        for j in range(0, len(letters)):
            value += ord(letters[j])-96
        tlist.append((i, value))
    tlist.sort(reverse=True)
    tlist.sort(key=lambda tup: tup[1], reverse=True)
    hello = list(map(lambda i: i[0], tlist))
    return hello

hhh = ["cabb", "cad"]
print(answer(hhh))