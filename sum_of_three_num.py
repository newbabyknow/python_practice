# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/3sum



def sum_0(nums):
    nums_sorted = sorted(nums)
    res = []
    for k in range(len(nums_sorted)):
        if nums_sorted[k] == nums_sorted[k-1]:
            break
        start = k + 1
        end = len(nums_sorted) - 1
        while nums_sorted[k] < 0 and start < end:
            if nums_sorted[k] + nums_sorted[start] + nums_sorted[end] == 0:
                res.append([nums_sorted[k] , nums_sorted[start], nums_sorted[end]])
                end -= 1
                while nums_sorted[end] == nums_sorted[end - 1] : end -= 1
                start += 1
                while nums_sorted[start] == nums_sorted[start+1] : start += 1
            elif nums_sorted[k] + nums_sorted[start] + nums_sorted[end] > 0:
                end -= 1
                while nums_sorted[end] == nums_sorted[end - 1] : end -= 1
            else:
                start += 1
                while nums_sorted[start] == nums_sorted[start+1]:start += 1
    return res


if __name__ == '__main__':
    nums_in = [3, -1, 0, 1, 1, -1, 2, 3, 4]
    print(sum_0(nums_in))