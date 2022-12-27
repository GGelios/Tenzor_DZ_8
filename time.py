import time

def timer(func):
    def wrapper(n):
        start = time.time()
        func(n)
        end = time.time()
        print(f'Function execution time:', end - start)
        return func
    return wrapper

@timer
def print_fib(n):
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(f'The value of the Fibonacci sequence element with the sequence number {n} is equal to {fibonacci(n)}')

try:
    n = int(input("Enter the sequence number of the Fibonacci sequence element: "))
except:
    print('The ordinal number of the element of the Fibonacci sequence must be a positive integer')
    exit()
if n < 0:
    print('The ordinal number of the element of the Fibonacci sequence must be a positive integer')
    exit()

print_fib(n)
