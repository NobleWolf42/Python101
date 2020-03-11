x = 2
print("x =", x)

def func():
    global x
    print("----------")
    print("Before: x =", x)
    x = 5
    print("After: x =", x)
    print("----------")

func()   #  Calling the function
print("x =", x)

x = 99
func()
