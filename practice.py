import random


def last_len(str1):
    # 输入一个字符串，输出字符串最后一个单词的长度
    list_word = str1.split(' ')
    print(len(list_word[-1]))


def num(str1, str2):
    # 输入一个字符串，一个字母，输出字符串中该字母出现的次数
    print(str1.count(str2))


def sort(str1):
    # 字符串切片方式实现反向输出
    print(str1[::-1])


def ra(n, nums):
    # 随机数，排序去重
    list_num = []
    for i in range(nums):
        list_num.append(random.randint(0, n))
    print(set(list_num))


def sub_str(str1, str_sub):
    # 求出自字符串的数量，输入两个字符串
    sub_num = str1.count(str_sub)
    print(sub_num)


if __name__ == '__main__':
    sub_str('1000', '0')
