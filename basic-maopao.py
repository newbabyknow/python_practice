# 冒泡排序算法

s = [2, 2, 3, 4, 1, 4, 5, 1, 9, 3]

for i in range(len(s)):
    for j in range(len(s)-i-1):
        if s[j] > s[j+1]:
            mid = s[j]
            s[j] = s[j+1]
            s[j+1] = mid
print(s)