def dec_func(func):
    def inner(x, y):
        y = x * (y - 1)
        return func(x,y)
    return inner

@dec_func
def add_func(a, b):
    return a + b

res = add_func(4, 5)
print(res)
print(2*res)

