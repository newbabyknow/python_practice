# 给一个有序数组和一个target，如果数组中存在target,返回true
# 二分法


def get_target_index_from_list(list_sorted, target):
    if len(list_sorted) == 0:
        return False
    low = 0
    high = len(list_sorted)
    mid = int((low+high)/2)
    if target == list_sorted[mid]:
        return True
    elif list_sorted[mid] > target:
        high = mid
        return get_target_index_from_list(list_sorted[low:high], target)
    else:
        low = mid
        return get_target_index_from_list(list_sorted[low:high], target)


if __name__ == '__main__':
    print(get_target_index_from_list([1, 2, 3, 4, 5], 4))