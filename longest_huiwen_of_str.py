# 输入字符串s，判断是否是回文
# 该方法仅实现了最长回文为奇数的情况，还有偶数的情况需要重复判断一下


def s_check(s):
    result = True
    for i in range(int(len(s)/2)):
        if s[i] != s[len(s)-1-i]:
            result = False
    return result


if __name__ == '__main__':
    s = 'aaabaaa'
    s_hui = ''
    s_hui_len = 1
    for i in range(len(s)):
        start = i-1
        end = i+2
        while start>=0 and end<=len(s):
            if s_check(s[start:end]):
                if len(s[start:end]) > s_hui_len:
                    s_hui_len = len(s[start:end])
                    s_hui = s[start:end]
                start -= 1
                end += 1
            else:
                break
    print(s_hui)