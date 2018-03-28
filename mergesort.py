def merge(list_1, list_2):
    global counter      # for stepik
    new_list = []
    pointer_1 = 0
    pointer_2 = 0
    while pointer_1 < len(list_1) and pointer_2 < len(list_2):
        if list_1[pointer_1] <= list_2[pointer_2]:
            new_list.append(list_1[pointer_1])
            pointer_1 += 1
        else:
            counter += len(list_1) - pointer_1        # for stepik
            new_list.append(list_2[pointer_2])
            pointer_2 += 1
    if pointer_1 < len(list_1):
        new_list.extend(list_1[pointer_1:])
    else:
        new_list.extend(list_2[pointer_2:])
    return new_list


def mergesort(main_list):
    if len(main_list) == 1:
        return main_list
    l = 0
    r = len(main_list) - 1
    m = (r - l) // 2
    return merge(mergesort(main_list[l:m + 1]), mergesort(main_list[m + 1: r + 1]))


def iter_mergesort(main_list):
    queue = [[i] for i in main_list]
    while len(queue) > 1:
        queue.append(merge(queue.pop(0), queue.pop(0)))
    return queue[0]


if __name__ == '__main__':  #for stepik
    n = input()
    counter = 0
    mergesort(list(map(int, input().split())))
    print(counter)

