# 输入ABC，判断三角形是否是等边等腰三角形


def sanjiao_panduan(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return
    if a + b < c or a + c < b or b + c < a:
        return
    if a == b and b == c:
        print('等边三角形')
    elif a == b or b == c or a == c:
        print('等腰三角形')
    else:
        print('普通三角形')


if __name__ == '__main__':
    sanjiao_panduan(4, 3, 3)