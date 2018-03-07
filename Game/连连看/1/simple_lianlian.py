# coding:utf-8
'''
http://migdal-bavel.in/2015/09/26/%E8%AE%A9%E6%88%91%E4%BB%AC%E6%9D%A5%E7%A0%94%E7%A9%B6%E4%B8%80%E4%B8%8B%E7%A5%9E%E5%A5%87%E7%9A%84%E8%BF%9E%E8%BF%9E%E7%9C%8B/
'''

import random

length = 4
width = 4


def set_up_random_matrix(length, width):  # 生成一个随机矩阵
    matrix = []
    random_list = set_random_list(int(length * width / 2))
    for i in range(width):
        line = []
        for j in range(length):
            line.append([i + 1, j + 1, random_list[i * length + j]])
        matrix.append(line)
    return matrix


def expand_matrix(matrix):  # 扩展矩阵使其有边界
    width = len(matrix)
    length = len(matrix[0])

    new_matrix = []
    # add the first expand line
    new_line = []
    for i in range(length + 2):
        new_line.append([0, i, -1])
    new_matrix.append(new_line)

    for i in range(width):
        new_line = []
        new_line.append([i + 1, 0, -1])
        for j in range(length):
            new_line.append(matrix[i][j])
        new_line.append([i + 1, length + 1, -1])
        new_matrix.append(new_line)

    new_line = []
    for i in range(length + 2):
        new_line.append([width + 1, i, -1])
    new_matrix.append(new_line)
    return new_matrix


def show(matrix):  # 显示矩阵，不显示边界和消去的元素
    width = len(matrix)
    length = len(matrix[0])
    for i in range(width):
        for j in range(length):
            if matrix[i][j][2] == 0:
                print(' ' + '\t', )
            elif matrix[i][j][2] == -1:
                print(' ' + '\t', )
            else:
                print(str(matrix[i][j][2]) + '\t', )
        print('\n')


def is_linked(matrix, flag):  # 检验是否这一对是相连的
    position = []
    for i in matrix:
        for j in i:
            if j[2] == flag:
                position.append([j[0], j[1]])
    node_in_depth_0 = []
    node_in_depth_0.extend(search_with_direction(0, matrix, position[0], flag))
    if ('ok' in node_in_depth_0):
        return True, position

    node_in_depth_1 = []
    for i in node_in_depth_0:
        temp = search_with_direction(i[1], matrix, i[0], flag)
        node_in_depth_1.extend(temp)
    if ('ok' in node_in_depth_1):
        return True, position
    node_in_depth_2 = []

    for j in node_in_depth_1:
        node_in_depth_2.extend(search_with_direction(j[1], matrix, j[0], flag))
    if ('ok' in node_in_depth_2):
        return True, position
    return False, position


def search_with_direction(direction, matrix, position, flag):  # 搜寻这个结点指定方向上的所有可以到达的结点
    x = position[0]
    y = position[1]

    if direction == 0:  # 东西南北都搜索，只有开始的那个结点使用
        line_0 = []
        if search_with_direction(1, matrix, position, flag) == ['ok']:
            return ['ok']
        else:
            line_0.extend(search_with_direction(1, matrix, position, flag))

        if search_with_direction(2, matrix, position, flag) == ['ok']:
            return ['ok']
        else:
            line_0.extend(search_with_direction(2, matrix, position, flag))
        return line_0

    if direction == 1:  # 东西方向
        line_1 = []
        i = 1
        while (y + i < len(matrix[0])):
            if matrix[x][y + i][2] == flag:
                return ['ok']
            elif (matrix[x][y + i][2] > 0):
                break
            else:
                line_1.append([[x, y + i], 2])
            i = i + 1

        i = 1
        while (y - i >= 0):
            if matrix[x][y - i][2] == flag:
                return ['ok']
            elif (matrix[x][y - i][2] > 0):
                break
            else:
                line_1.append([[x, y - i], 2])
            i = i + 1
        return line_1

    if direction == 2:  # 南北方向
        line_2 = []
        i = 1
        while (x + i < len(matrix)):
            if matrix[x + i][y][2] == flag:
                return ['ok']
            elif (matrix[x + i][y][2] > 0):
                break
            else:
                line_2.append([[x + i, y], 1])
            i = i + 1

        i = 1
        while (x - i >= 0):
            if matrix[x - i][y][2] == flag:
                return ['ok']
            elif (matrix[x - i][y][2] > 0):
                break
            else:
                line_2.append([[x - i, y], 1])
            i = i + 1
        return line_2


def vanish(flag, matrix):  # 消去一对结点
    for i in matrix:
        for j in i:
            if (j[2] == flag):
                j[2] = 0
    return matrix


def set_random_list(n):  # 生成一个特定随机的数列，用来生成随机矩阵
    random_list = [0] * n * 2
    for i in range(n):

        position = random.randint(0, n * 2 - 1)
        while (random_list[position] != 0): position = (position + 1) % (n * 2)
        random_list[position] = i + 1

        position = random.randint(0, n * 2 - 1)
        while (random_list[position] != 0): position = (position + 1) % (n * 2)
        random_list[position] = i + 1
    return random_list


def check_deadlock(matrix):  # 检查死锁
    for i in matrix:
        for j in i:
            if j[2] != -1 and j[2] != 0:
                x, y = is_linked(matrix, j[2])
                if x == True:
                    return False
    return True


def random_switch(matrix):  # 随机调整矩阵
    x = len(matrix) - 2
    y = len(matrix[0]) - 2
    for i in range(x):
        x_ran_1 = random.randint(0, x - 1)
        y_ran_1 = random.randint(0, y - 1)

        x_ran_2 = (x_ran_1 + random.randint(1, 100)) % x
        y_ran_2 = (y_ran_1 + random.randint(1, 100)) % y
        matrix[x_ran_1 + 1][y_ran_1 + 1][2], matrix[x_ran_2 + 1][y_ran_2 + 1][2] = matrix[x_ran_2 + 1][y_ran_2 + 1][2], \
                                                                                   matrix[x_ran_1 + 1][y_ran_1 + 1][2]
    return matrix


def check_empty(matrix):  # 检查是否 game over
    for i in matrix:
        for j in i:
            if j[2] != 0 and j[2] != -1:
                return False
    return True


if __name__ == '__main__':  # 开始游戏
    print('***********')
    print("This is a demo lianliankan game. You could vanish the number pairs in '-1' boundary if they were linked in rule.")
    print('***********')

    print('please input the length of lianliankan, please input even number bigger than 2:')
    while True:
        length = int(input('>'))
        if type(length) == int and length % 2 == 0 and width > 2:
            break
        else:
            print('error type of input, please input again:')

    print('please input the width of lianliankan, please input even number bigger than 2:')
    while True:
        width = int(input('>'))
        if type(length) == int and width % 2 == 0 and length > 2:
            break
        else:
            print('error type of input, please input again:')

    matrix = set_up_random_matrix(length, width)
    matrix = expand_matrix(matrix)
    while True:
        if check_deadlock(matrix) == True:
            matrix = random_switch(matrix)
        else:
            break

    print('The fllowing random matrix was generated:')
    show(matrix)
    box = range(1, int(length * width / 2 + 1))
    used_box = []
    print('Now starting game')
    while True:
        print("please input the number pairs you wanna vanish:")
        flag = input('>')
        if flag not in box or flag in used_box:
            print("error input type, please input the number pairs exists again:")

        else:
            index, position = is_linked(matrix, flag)
            if index == False:
                print('This pairs can not link, please try other pairs:')
            else:
                print('This pairs were linked, vanishhhhhhh!')
                used_box.append(flag)
                matrix = vanish(flag, matrix)
                show(matrix)
                if check_empty(matrix):
                    print('You win the game, congratulations')
                    break
                elif check_deadlock(matrix) == True:
                    print('Now the matrix is no pairs linked, let us watch a magic:')
                    while True:
                        matrix = random_switch(matrix)
                        if check_deadlock(matrix) == False:
                            break
                    show(matrix)
                print('Next round')
