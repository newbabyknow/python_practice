def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_2(n):
    i = 0
    a, b = 1, 1
    while i < n:
        yield b
        i += 1
        a, b = b, a+b


if __name__ == '__main__':
    for n in fib_2(5):
        print(n)