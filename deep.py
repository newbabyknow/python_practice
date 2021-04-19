def deep_count(n):
    if n == 1:
        return 1
    else:
        return n * deep_count(n - 1)


def n_power(x, n):
    if n == 1:
        return x
    else:
        return x * n_power(x, n - 1)


if __name__ == '__main__':
    print(n_power(3, 4))
