def fib(n):
    fib1 = 0
    fib2 = 1
    i = 0
    while i < n:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        i = i + 1
    return fib2

    
N = int(input("Введите число: "))
print (N, fib(N))