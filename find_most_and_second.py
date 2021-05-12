# 一次循环找出最大的两个数,求nums中最大乘积最大的两个数


def find_most_and_second(s):
    most = 0
    second = 0
    for i in s:
        if i > second:
            if i >= most:
                second = most
                most = i
            else:
                second = i
    return most, second


if __name__ == '__main__':
    s = [2, 2, 4, 6, 2, 8, 3, 9, 1, 7]
    print(find_most_and_second(s))