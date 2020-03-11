def evaluate(f, m, n):
    return f(m, n)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y


print(evaluate(add, 2, 5))
print(evaluate(multiply, 10, 4))
