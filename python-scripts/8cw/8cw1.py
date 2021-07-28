class man:
    def __init__(m, name, age):
        m.name = name
        m.age = age
    def func(abc):
        print('hello my name is '+abc.name)
x = man('deni', 36)
x.func()