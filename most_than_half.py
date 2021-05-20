# 给一个数组，找到数组中数量超过一半的数
# 常规解法，排序取中间的数就是超过一半的，时间复杂度nlog(n)
# 解法二，存在字典中，key记数字，value记录次数，超过半数return，时间复杂度n,多出了空间复杂度n
# 优化解法，消除两个不一样的数，双指针，循环一遍退出，只剩下相同的数，时间复杂度n


def most_than_half(nums):
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] != nums[j]:
            del nums[j]
            del nums[i]
            j -= 2
            i = j-1
        else:
            j += 1
    return nums


nums = [2, 2, 2, 2, 2, 2, 3, 4, 2, 2, 3, 4, 2]
if __name__ == '__main__':
    print(most_than_half(nums))