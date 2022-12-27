import time


def sleep(func):
    '''Decorator for the function counting the value of a given element
    of the Fibonacci sequence, prohibiting the function from being called more often
    than once every 5 seconds
    '''

    count = [0]
    last = [time.time()]

    def wrapper(n):
        # The first function call
        if count[0] == 0:
            count[0] += 1
            return func(n)
        # Subsequent calls
        else:
            if time.time() - last[0] < 5:
                print(f'The function call is too frequent. The result will be output after {5 - (time.time() - last[0])} seconds')
                # Timer
                time.sleep(5 - (time.time() - last[0]))
        count[0] += 1
        last[0] = time.time()
        return func(n)
    return wrapper


@sleep
def print_fib(n):
    def fibonacci(n):
        if n in (1, 2):
            return 1
        return fibonacci(n - 1) + fibonacci(n - 2)
    print(
        f'The element of the Fibonacci sequence with the ordinal number {n} is equal to {fibonacci(n)}\n')


n = '0'
while n.isdigit():
    try:
        n = input('Enter the sequence number of the Fibonacci sequence element:\n')
        print_fib(int(n))
    except RecursionError:
        print('The ordinal number of the element of the Fibonacci sequence must be a positive integer')
        exit()
    except ValueError:
        print('The ordinal number of the element of the Fibonacci sequence must be a positive integer')
        exit()
    except KeyboardInterrupt:
        print('The program has been completed')
        exit()
