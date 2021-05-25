def asert(parms):
    result = True
    try:
        assert (1 == parms)
    except AssertionError:
        result = False
    return result


if __name__ == '__main__':
    print(asert(1))