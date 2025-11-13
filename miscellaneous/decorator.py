
def outer(fun):
    def inner(*arg, **kwargs):
        a = arg[0]
        b = arg[1]
        print('inner called')
        return a - b
    return inner

class multi:
    def __init__(self, text):
        print(text)

    def __call__(self, func):
        def wrapper(a, b):
            result = func(a, b)
            return result * 10
        return wrapper

@multi('msg')
@outer
def add_num(a, b):
    return a + b

print(add_num(20, 10))