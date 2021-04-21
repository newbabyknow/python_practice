def join_list(m, n):
    # 合并有序字符串
    index = 0
    for i in m:
        for n_son in range(index, len(n)):
            print(index)
            if i < n[n_son]:
                n.insert(n_son, i)
                index = n_son + 1
                break


if __name__ == '__main__':
    list_1 = [1, 2, 3, 4]
    list_2 = [2, 3, 4, 5, 6]
    join_list(list_1, list_2)
    print(list_2)