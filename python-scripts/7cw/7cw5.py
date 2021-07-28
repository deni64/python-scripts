f= int(input())

def fibbonaci(f):
    fib1 = -1
    fib2 = 1
    fibsum = 0
    for x in range(f+1):
        fibsum = fib1 + fib2
        fib1 = fib2
        fib2 = fibsum
    print(fibsum)

fibbonaci(f)


