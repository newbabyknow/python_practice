# 快速排序


def quick_sort(list_num):
    if len(list_num) < 2:
        return list_num
    mid = list_num[0]
    list_left = []
    list_right = []
    # print(list_num[1:])
    for i in list_num[1:]:
        if i <= mid:
            list_left.append(i)
        elif i > mid:
            list_right.append(i)
    return quick_sort(list_left) + [mid] + quick_sort(list_right)


if __name__ == '__main__':
    list_in = [2, 4, 1, 6, 4, 6, 3, 2, 4, 6, 3, 8, 7, 5]
    print(quick_sort(list_in))