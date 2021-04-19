def sum_str(str1, str2, is_add=0):
    num_mid = int(str1) + int(str2) + is_add
    is_add = 0
    if num_mid >= 10:
        is_add = 1
    return num_mid % 10, is_add


if __name__ == '__main__':
    str_1 = '6234'
    str_2 = '5678'
    result_list = []
    is_add = 0
    for i in range(len(str_1)+1):
        if i < len(str_1):
            result = sum_str(str_1[-i-1], str_2[-i-1], is_add)
            is_add = result[1]
            result_list.append(result[0])
        else:
            if is_add > 0:
                result_list.append(is_add)
    result_str = ''
    for i in range(len(result_list)):
        result_str += str(result_list[-i-1])
    print(result_str)