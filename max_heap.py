def index(i):
    """Для нумерации кучи с единицы"""
    return i - 1


def shift_up(i: int, heap: list):
    """Поднимает элемент наверх, возвращает новый индекс"""
    heap[index(i)], heap[index(i // 2)] = heap[index(i // 2)], heap[index(i)]
    return i // 2


def shift_down(i, heap):
    """Меняет элемент с максимальным сыном, возвращает новый индекс"""
    if len(heap) >= i * 2 + 1 and heap[index(i * 2 + 1)] > heap[index(i * 2)]:
        heap[index(i)], heap[index(i * 2 + 1)] = heap[index(i * 2 + 1)], heap[index(i)]
        return i * 2 + 1
    elif len(heap) >= i * 2:
        heap[index(i)], heap[index(i * 2)] = heap[index(i * 2)], heap[index(i)]
        return i * 2
    """
    else:
        print('Ошибка при Shift down')
    """


def normalize_heap_up(i, heap):
    """Просеивание вверх"""
    now_index = i
    while heap[index(now_index // 2)] < heap[index(now_index)] and now_index != 1:
        now_index = shift_up(now_index, heap)


def normalize_heap_down(i, heap):
    """Просеивание вниз. До дрожи в коленях боялся out of range, поэтому некрасиво"""
    now_index = i
    while now_index * 2 <= len(heap):
        if now_index * 2 + 1 <= len(heap):
            if heap[index(now_index)] <= heap[index(now_index * 2)] or heap[index(now_index)] <= heap[index(now_index * 2 + 1)]:
                now_index = shift_down(now_index, heap)
            else:
                break
        elif heap[index(now_index)] <= heap[index(now_index * 2)]:
            now_index = shift_down(now_index, heap)
        else:
            break


def insert(x, heap):
    """Вставка нового элемента в конец кучи, вызов просеивания наверх"""
    heap.append(x)
    normalize_heap_up(len(heap), heap)


def extract_max(heap):
    """Печатает максимальный элемент, ставит на его место последний элемент и просеивает его вниз"""
    print(heap[0])
    heap[0] = heap[-1]
    heap.pop()
    normalize_heap_down(1, heap)


heap = []
n = int(input())
for _ in range(n):
    data = input().split()
    if data[0] == 'Insert':
        insert(int(data[1]), heap)
    else:
        extract_max(heap)
