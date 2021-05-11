# 输出重复最多的10个字符，例如：aabcdbb, 输出a,b

# dict_in = {4: 3, 3: 2, 5: 5, 8: 6, 2: 9}
# list_sort = sorted(dict_in.items(), key= lambda x: x[0], reverse=True)
# print(list_sort)


def find_more_str(str_in):
    dict_in = {}
    for s in str_in:
        if s in dict_in:
            dict_in[s] += 1
        else:
            dict_in[s] = 1
    list_sorted = sorted(dict_in.items(), key=lambda x: x[1], reverse=True)
    return list_sorted


if __name__ == '__main__':
    s = 'aaabbccdddaa'
    list_result = find_more_str(s)
    print(list_result[0][0])