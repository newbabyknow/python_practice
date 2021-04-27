# 滑动窗口方法，计算字符串的最长不重复子字符串


def window(s):
    begin_index = 0
    max_long = 0
    for i in range(1, len(s)):
        if s[i] in s[begin_index:i]:
            max_long = max(max_long, len(s[begin_index:i]))
            begin_index = s.index(s[i]) + 1
    if max_long == 0:
        max_long = len(s)
    return max_long


if __name__ == '__main__':
    a = window('abccdc')
    print(a)
