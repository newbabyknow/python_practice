list1 = [0, 1]
while list1[-1] < 100:
    sum_pre = list1[-1] + list1[-2]
    if sum_pre <100:
        list1.append(sum_pre)
    else:
        break
print(list1)
