def make_node(number, frequency, parent=None, left_child=None, right_child=None, symbol=None):
    """Возвращает узел в виде списка с номером, частотой, родителем, левым и правым сыновьями, символом"""
    return [number, frequency, parent, left_child, right_child, symbol]


def nod(number, tree):
    """Возвращает узел с номером number"""
    for x in tree:
        if num(x) == number:
            return x
    print('Узел с номером ' + number + ' не найден')


def num(node):
    """Возвращает номер узла"""
    return node[0]


def freq(node):
    """Возвращает частоту узла"""
    return node[1]


def par(node):
    """Возвращает номер родителя узла"""
    return node[2]


def l_child(node):
    """Возвращает номер левого сына узла"""
    return node[3]


def r_child(node):
    """Возвращает номер правого сына узла"""
    return node[4]


def sym(node):
    """Возвращает символ узла"""
    return node[5]


def is_node_root(node):
    """Проверяет, является ли узел корнем"""
    return par(node) is None


def is_node_leaf(node):
    """Проверяет, является ли узел листом (не пригодилось, но пусть будет)"""
    return (l_child(node) is None) and (r_child(node) is None)


def make_tree(number, node_1: list, node_2: list):
    """Создает и возвращает узел с номером, суммарной частотой объединяемых узлов, с сылками на номера объединяемых
    узлов. Меняет ссылки на родительский узел входящих узлов"""
    node_1[2] = number
    node_2[2] = number
    return make_node(number, (freq(node_1) + freq(node_2)), left_child=num(node_1), right_child=num(node_2))


s = input()
symbol_list = []
frequency_dict = {}                         # словарь символ: частота
for i in s:                                 # заполнение словаря частот
    if i not in symbol_list:
        symbol_list.append(i)
        frequency_dict[i] = s.count(i) / len(s)
main_tree = []                                       # ДЕРЕВО
root_list = []                                       # список корней
number_count = 0                                     # счетчик для присовения узлам уникальных номеров
for j in symbol_list:                                # сначала вносим узлы с символами в список корней
    root_list.append(make_node(number_count, frequency_dict[j], symbol=j))
    number_count += 1
root_list.sort(key=lambda x: freq(x), reverse=True)         # сортировка корней по частотам в порядке убывания
while len(root_list) > 1:                                               # пока не останется один корень
    new_tree = make_tree(number_count, root_list[-2], root_list[-1])    # объединяем два корня с наименьшими частотами
    main_tree.append(root_list[-2])                                     # вносим их в ДЕРЕВО
    main_tree.append(root_list[-1])
    root_list = root_list[:-2]                                          # и удаляем их из списка корней
    root_list.append(new_tree)                             # добавляем в список корней созданный соданный общий корень
    root_list.sort(key=lambda x: freq(x), reverse=True)
    number_count += 1
main_tree.append(root_list[0])      # добавляем главный корень в ДЕРЕВО


code_dict = {}                      # словарь кодирования
for sym in symbol_list:             # для каждого символа
    code_dict[sym] = ''                                # начинаем с узла, содержащего...
    now_node = nod(symbol_list.index(sym), main_tree)  # ...данный символ (№ узла == index в symbol_list)
    while not is_node_root(now_node):                  # пока не дойдем до корня
        ex_number = num(now_node)                      # запоминаем текущий номер
        now_node = nod(par(now_node), main_tree)       # идем к родителю
        if l_child(now_node) == ex_number:             # определяем каким сыном является прошлый узел
            code_dict[sym] += '0'                      # и записываем либо 0, либо 1
        elif r_child(now_node) == ex_number:
            code_dict[sym] += '1'
        else:
            print('Ошибка в узле ' + str(num(now_node)) + ' при поиске пути к корню от символа "' + sym + '"')
    code_dict[sym] = code_dict[sym][::-1]       # разворот, т.к. шли по ДЕРЕВУ "наверх"
    if len(main_tree) == 1:                     # случай одного узла в ДЕРЕВЕ(ни разу не попали в предыдущий цикл)
        code_dict[sym] = 0
code_string = ''
for n in s:
    code_string += str(code_dict[n])
for m in symbol_list:
    print(m, ': ', code_dict[m], sep='')
print(code_string)
