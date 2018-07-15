"""
СОРТИРОВКИ
ВВОД: числа через пробел
"""
import random


def selection_sort(main_list):
    for i in range(len(main_list) - 1):
        min_index = i
        for j in range(i + 1, len(main_list)):
            if main_list[j] < main_list[min_index]:
                min_index = j
        main_list[i], main_list[min_index] = main_list[min_index], main_list[i]


def insertion_sort(main_list):
    for i in range(1, len(main_list)):
        for j in range(i - 1, - 1, -1):
            if main_list[i] > main_list[j]:
                break
            main_list[i], main_list[j] = main_list[j], main_list[i]
            i -= 1


def bubble_sort(main_list):
    for i in range(len(main_list) - 1, 0, -1):
        for j in range(i):
            if main_list[j] > main_list[j + 1]:
                main_list[j], main_list[j + 1] = main_list[j + 1], main_list[j]


def merge_sort(main_list):

    def merge(list_1, list_2):
        i = 0
        j = 0
        k = 0
        res_list = list()
        while i < len(list_1) and j < len(list_2):
            if list_1[i] <= list_2[j]:
                res_list.append(list_1[i])
                i += 1
            else:
                res_list.append(list_2[j])
                j += 1
            k += 1
        if i < len(list_1):
            res_list.append(list_1[i:])
            return res_list
        res_list.append(list_2[j:])
        return res_list

    if len(main_list) <= 1:
        return main_list
    m = len(main_list) // 2
    return merge(merge_sort(main_list[0:m + 1]), merge_sort(main_list[m + 1:]))


def quick_sort(main_list, l=None, r=None):

    def partition(main_list, l, r):

        # тут берем случайный индекс, чтоб не тормозить на почти упорядовенных массивах
        random_index = random.randint(l, r)
        main_list[l], main_list[random_index] = main_list[random_index], main_list[l]

        nowItem = main_list[l]
        j = l
        for i in range(l + 1, r + 1):
            if main_list[i] <= nowItem:
                j += 1
                main_list[j], main_list[i] = main_list[i], main_list[j]
        main_list[l], main_list[j] = main_list[j], main_list[l]
        return j

    l = l or 0
    r = r or len(main_list) - 1

    """
    Вариант с хвостовой рекурсией
    if l >= r:
        return
    m = partition(main_list, l, r)
    quick_sort(main_list, l, m - 1)
    quick_sort(main_list, m + 1, r)
    """

    # Элиминация хвостовой рекурсии и балансировка дерева(рекурсивно вызываем более короткий отрезок)
    while l < r:
        m = partition(main_list, l, r)
        if (r - m) >= m + 1:
            quick_sort(main_list, l, m - 1)
            l = m + 1
            continue
        quick_sort(main_list, m + 1, r)
        r = m - 1


def heap_sort(main_list):

    def sift_down(main_list, index, size):

        now_index = index

        while now_index < size and now_index * 2 <= size:
            target_index = now_index * 2
            if (now_index * 2) + 1 <= size and \
                    main_list[(now_index * 2) - 1] < main_list[((now_index * 2) + 1) - 1]:
                target_index = (now_index * 2) + 1
            if main_list[now_index - 1] >= main_list[target_index - 1]:
                break
            main_list[now_index - 1], main_list[target_index - 1] = \
                main_list[target_index - 1], main_list[now_index - 1]
            now_index = target_index

    def build_max_heap(main_list):
        for i in range(len(main_list) // 2, 0, -1):
            sift_down(main_list, i, len(main_list))

    build_max_heap(main_list)
    size = len(main_list)
    for i in range(len(main_list), 1, - 1):
        main_list[size - 1], main_list[0] = main_list[0], main_list[size - 1]
        size -= 1
        sift_down(main_list, 1, size)



if __name__ == '__main__':
    sort_list = [int(i) for i in input().split()]
    heap_sort(sort_list)
    print(*sort_list)
