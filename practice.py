import random
import re


def last_len(str1):
    # 输入一个字符串，输出字符串最后一个单词的长度
    list_word = str1.split(' ')
    print(len(list_word[-1]))


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


def cut_by_length(ori_str):
    # 按照固定长度分割字符串，最后一个补全，参数：一个字符串
    list_result = re.findall(r'.{5}', ori_str)
    last_str = len(ori_str) % 5
    last_str_re = ori_str[-last_str:]
    for i in range(5 - last_str):
        last_str_re += '0'
    list_result.append(last_str_re)
    print(list_result)


def get_similar(num):
    # 四舍五入，取近似值，参数：long型或int型数字
    result = int(num + 0.5)
    print(result)


if __name__ == '__main__':
    get_similar(4.6)
