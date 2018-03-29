def quicksort(main_list, l, r):
    while l < r:
        m = partition(main_list, l, r)
        if m - l < r - m:
            quicksort(main_list, l, m - 1)
            l = m + 1
        else:
            quicksort(main_list, m + 1, r)
            r = m - 1
    return main_list


def partition(main_list, l, r):
    x = main_list[l]
    j = l
    for i in range(l + 1, r + 1):
        if main_list[i] < x:
            j += 1
            main_list[j], main_list[i] = main_list[i], main_list[j]
    main_list[l], main_list[j] = main_list[j], main_list[l]
    return j


if __name__ == '__main__':                      # for stepik
    n, m = [int(i) for i in input().split()]
    line_list = []
    point_list = []
    for _ in range(n):
        line_list.append([int(i) for i in input().split()])
    quicksort(line_list, 0, len(line_list) - 1)
    for i in [int(j) for j in input().split()]:
        counter = 0
        for x in line_list:
            if i < x[0]:
                break
            elif i <= x[1]:
                counter += 1
        print(counter, end=' ')
