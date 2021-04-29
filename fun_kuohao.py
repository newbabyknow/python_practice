# 有效括号判断


def func_kuohao(s):
    dict_s = {'(': ')', ')': '(', '[': ']', ']': '['}
    list_s = []
    for i in range(len(s)):
        if len(list_s) > 0:
            if s[i] == dict_s[list_s[-1]]:
                list_s = list_s[0:-1]
            else:
                list_s.append(s[i])
        else:
            list_s.append(s[i])
    if len(list_s) > 0 :
        return False
    else:
        return True


if __name__ == '__main__':
    print(func_kuohao('()[()()]'))
