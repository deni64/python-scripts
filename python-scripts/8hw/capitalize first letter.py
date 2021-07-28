y = input()

def func(y):
    z = ord(y[0])-32
    print(chr(z) + y[1:])
func(y)