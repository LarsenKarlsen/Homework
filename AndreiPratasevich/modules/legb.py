a = "I am global variable!"


def enclosing_funcion():
    a = "I am variable from enclosed function!"

    def inner_function():
        print(globals()['a'])
        nonlocal a; print(a)
        a = "I am local variable!"
        print(a)
    return inner_function

x = enclosing_funcion()
x()