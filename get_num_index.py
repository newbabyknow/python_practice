# 给一个列表，一个数字，找出列表里边两个数相加只和为给定数字，返回两个数的index


def get_index(nums, target):
    dict_num = {}
    for i in range(len(nums)):
        dict_num[nums[i]] = i
    print(dict_num)
    for i in range(len(nums)):
        x = target - nums[i]
        j = dict_num.get(x)
        if j:
            return i, j


if __name__ == '__main__':
    nums = [11, 15, 2, 7]
    target = 9
    print(get_index(nums, target))