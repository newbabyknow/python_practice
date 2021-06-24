def join_list(m, n):
    # 合并有序数组
    if len(n) == 0:
        return m
    else:
        # 把n插入到m里
        i, j = 0, 0
        while i < len(m) and j < len(n):
            if n[j] <= m[i]:
                m.insert(i, n[j])
                i += 1
                j += 1
            else:
                i += 1
        if j < len(n):
            m += n[j:]

        return m


if __name__ == '__main__':
    m = [1, 2, 3, 4]
    n = [1, 2, 3, 4, 7, 8, 9]
    print(join_list(m, n))
