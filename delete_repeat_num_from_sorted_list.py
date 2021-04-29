# 两个有序列表合并,从小到大
# 两个指针，后移，遇到想通过的删除


def delete_repeat_list_sorted(list1):
    i = 0
    j = 1
    while j < len(list1):
        if list1[j] == list1[i]:
            del list1[j]
        else:
            i += 1
            j += 1
    print(list1)


if __name__ == '__main__':
    list2 = [1, 1, 2, 2, 3, 4, 5, 6, 6, 7, 8]
    delete_repeat_list_sorted(list2)