def last_len(str1):
    # 输入一个字符串，输出字符串最后一个单词的长度
    list_word = str1.split(' ')
    print(len(list_word[-1]))


def num(str1, str2):
    # 输入一个字符串，一个字母，输出字符串中该字母出现的次数
    print(str1.count(str2))


def sort(str1):
    #字符串切片方式实现反向输出
    print(str1[::-1])


if __name__ == '__main__':
    sort('i, am, iron man')
