# 给一个数组，一个数值x，删除数组中的x


def del_num_from_list(list_nums, num):
    ans = 0
    i = 0
    while i < len(list_nums):
        if list_nums[i] == num:
            del list_nums[i]
        else:
            ans += 1
            i += 1
    print(ans, list_nums)


if __name__ == '__main__':
    del_num_from_list([1, 2, 3, 4, 5, 6, 7, 1, 1, 1, 3, 42, 1, 2], 1)