# 给定一个字符串，找出每个字母，按照字母重复次数从多到少输出
# 例：输入bcdbcddcccccc
# 输出：cdb


def count_str(str1):
    dict_result = {}
    for item in str1:
        if item not in dict_result:
            dict_result[item] = 1
        else:
            dict_result[item] += 1
    return dict_result


def sort_dict(dict1):
    result_sort = sorted(dict1.items(), key=lambda item: item[1], reverse=True)
    return result_sort


if __name__ == '__main__':
    str1 = 'bcdbcddcccccc'
    str_result = ''
    dict_result = count_str(str1)
    result_list = sort_dict(dict_result)
    for item in result_list:
        str_result += item[0]
    print(str_result)
