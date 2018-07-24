"""
Наибольшая невозрастающая последовательность
ВВОД: первая строка - n, количество элементов последовательности (int, 1 <= n <= 10**5)
      вторая строка - n элементов a последовательности через пробел (a: int, 0 <= a <= 10**9)

ВЫВОД: первая строка - m, количество элементов максимальной невозрастающей подпоследовательности
       вторая строка - m элементов максимальной невозрастающей подпоследовательности

Используется библиотека pycontracts
"""
import sys
import random
import time
import doctest
import unittest


from contracts import contract


def read_data():
    sys.stdin.readline() # пропускаем n, т.е. первая строка тут не нужна
    return [int(i) for i in sys.stdin.readline().split()]


@contract(seq_list='list[>=1, <=10^5](int, >=0, <=10^9)')
def naive_longest_noninreasing(seq_list):
    """
    Наивная реализация алгоритма поиска максимальной невозрастающей последовательности.
    :param: list[>=1, <=10^5](int, >=0, <=10^9)
    :return: list of indexes of elements from noninreasing subsequence
    >>> naive_longest_noninreasing([1, 2, 3, 4, 5])
    [5]
    >>> naive_longest_noninreasing([5, 3, 4, 4, 2])
    [1, 3, 4, 5]
    >>> naive_longest_noninreasing([5, 6, 7, 7, 6, 2, 3])
    [3, 4, 5, 7]
    >>> naive_longest_noninreasing([5, 3, 4, 4, 2, 5, 9])
    [1, 3, 4, 5]
    >>> naive_longest_noninreasing([2, 2, 2, 2])
    [1, 2, 3, 4]
    """

    max_len = 1
    last_index = 0
    sub_seq_len = [1 for _ in range(len(seq_list))]  # Список максимальных длин для каждого индекса.

    for i in range(len(sub_seq_len)):
        for j in range(i):
            if seq_list[i] <= seq_list[j] and sub_seq_len[i] < sub_seq_len[j] + 1:
                sub_seq_len[i] = sub_seq_len[j] + 1
        if sub_seq_len[i] >= max_len:
            max_len = sub_seq_len[i]
            last_index = i

    # Восстановление последовательности
    sub_seq_list = [0 for _ in range(max_len)]  # Список индексов эл-тов, входящих в макс. подпоследовательность.
    previous_item = seq_list[last_index]
    expect_num = max_len

    for i in range(last_index, -1, -1):
        if sub_seq_len[i] < expect_num or seq_list[i] < previous_item:
            continue
        sub_seq_list[expect_num - 1] = i + 1
        previous_item = seq_list[i]
        expect_num -= 1

    return sub_seq_list


@contract(seq_list='list[>=1, <=10^5](int, >=0, <=10^9)')
def fast_noninreasing(seq_list):
    """
    nlog(n) реализация алгоритма поиска максимальной невозрастающей последовательности.
    :param: list[>=1, <=10^5](int, >=0, <=10^9)
    :return: list of indexes of elements from noninreasing subsequence
    >>> fast_noninreasing([1, 2, 3, 4, 5])
    [5]
    >>> fast_noninreasing([5, 3, 4, 4, 2])
    [1, 3, 4, 5]
    >>> fast_noninreasing([5, 6, 7, 7, 6, 2, 3])
    [3, 4, 5, 7]
    >>> fast_noninreasing([5, 3, 4, 4, 2, 5, 9])
    [1, 3, 4, 5]
    >>> fast_noninreasing([2, 2, 2, 2])
    [1, 2, 3, 4]
    """
    sub_list = [-1 for _ in range(len(seq_list) + 1)]
    sub_list[0] = 10**9 + 1
    parent = [0 for _ in range(len(seq_list))]  # Для каждого элемента seq записываем его предшественника из подпосл.
    max_len = 1  # Максимальная длина подпоследовательности.
    last_index = 0  # Храним индекс из seq_list для последнего элемента, входящего в подпоследовательность.

    for i in range(len(seq_list)):
        j = search_index(sub_list, seq_list[i])
        if sub_list[j - 1] >= seq_list[i] > sub_list[j]:
            sub_list[j] = seq_list[i]
            parent[i] = sub_list[j - 1]
            if j >= max_len:
                max_len = j
                last_index = i

    # Восстановление ответа
    res_list = [0 for _ in range(max_len)]
    now_index = max_len - 1
    expect_num = seq_list[last_index]
    for i in range(last_index, -1, -1):
        if seq_list[i] != expect_num:
            continue
        res_list[now_index] = i + 1
        expect_num = parent[i]
        now_index -= 1

    return res_list


@contract(sub_list='list[>=1, <=10^5](int, >=-1, <=10^9+1)', item='int, >=0, <=10^9')
def search_index(sub_list, item):
    """
    Бинарный поиск индекса элемента в массиве sub_list, который строго меньше чем item.
    sub_list отсортирован по невозрастанию.
    Из-за специфики функции fast_nonincreasing, предполагается, что в sub_list всегда есть хотябы один элемент
    меньше чем item.
    :param sub_list: 'list[>=1, <=10^5](int, >=0, <=10^9+1)'
    :param item: 'int, >=1, <=10**9, >sub_list[-1]'
    :return: index: int
    >>> search_index([5, 4, 3, 2, 1], 5)
    1
    >>> search_index([10, 7, 7, 5, 5, 4, 4, 3, 3], 5)
    5
    >>> search_index([1000000001, 6, 6, 6, 5, 5, 4, 4, 4, 4, -1], 3)
    10
    """
    res_index = -1  # Из условий входящих данных, последний элемент sub_list всегда меньше чем item.
    left = 0
    right = len(sub_list) - 1
    while left <= right:
        mid_index = (left + right) // 2
        if sub_list[mid_index] >= item:
            left = mid_index + 1
        else:
            res_index = mid_index
            right = mid_index - 1
    return res_index


def out_data(res_list):
    result = str(len(res_list))
    result += '\n'
    result += " ".join(str(i) for i in res_list)
    print(result)


def comparsion_time_execution():

    seq = [random.randint(0, 10**9) for _ in range(10000)]

    start_time = time.time()
    naive_longest_noninreasing(seq)
    stop_time = time.time()
    print("naive " + str(int((stop_time-start_time) * 1000)) + " ms")

    start_time = time.time()
    fast_noninreasing(seq)
    stop_time = time.time()
    print("fast " + str(int((stop_time - start_time) * 1000)) + " ms")


def run():
    seq = read_data()
    res = fast_noninreasing(seq)
    out_data(res)


class MyTest(unittest.TestCase):

    def setUp(self):
        self.sequences = [[random.randint(0, 10**9) for _ in range(100)] for _ in range(5)]

    def test_simple(self):
        for seq in self.sequences:
            with self.subTest(case=seq):
                self.assertCountEqual(naive_longest_noninreasing(seq), fast_noninreasing(seq))

    def tearDown(self):
        self.sequences = None


if __name__ == '__main__':
    run()
