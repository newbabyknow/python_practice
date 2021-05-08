# 输入一个字符串，输出每个字符出现的次数 112333

str_count = '1123333'
dict_str = {}
for i in str_count:
    if i in dict_str:
        dict_str[i] += 1
    else:
        dict_str[i] = 1
print(dict_str)