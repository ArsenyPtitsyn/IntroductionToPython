import random

first_dot = 'X'
second_dot = '0'
empty_dot = '.'

vertical_field_size = 10
horizontal_field_size = 15
win_sequence = 5
field = [empty_dot] * vertical_field_size
for i in range(vertical_field_size):
    field[i] = [empty_dot] * horizontal_field_size

def print_map():
    for i in range(vertical_field_size):
        print('|', end='')
        for j in range(horizontal_field_size):
            print(field[i][j] + '|', end='')
        print()


def is_empty_cell(y, x):
    return field[y][x] == empty_dot

def is_valid_cell(y, x):
    return x >= 0 and x < horizontal_field_size and y >= 0 and y < vertical_field_size

def turn(dot):
    while True:
        x = int(input(f"Введите координату хода X (от 1 до {horizontal_field_size})")) - 1
        y = int(input(f"Введите координату хода Y (от 1 до {vertical_field_size})")) - 1
        if is_valid_cell(y, x) and is_empty_cell(y, x):
            field[y][x] = dot
            break
        print("Ячейки с такими индексами не существует или же она занята!")

def check_line(dot, y, x, dy, dx, condition):
    if condition:
        for i in range(win_sequence):
            if field[y + dy * i][x + dx * i] != dot:
                return False
            else:
                continue
        return True


def check_lines(dot, y, x):
    return check_line(dot, y, x, 0, 1, x <= horizontal_field_size - win_sequence) \
        or check_line(dot, y, x, 1, 0, y <= vertical_field_size - win_sequence) \
        or check_line(dot, y, x, 1, 1, x <= horizontal_field_size - win_sequence
                      and y <= vertical_field_size - win_sequence) \
        or check_line(dot, y, x, -1, 1, x <= horizontal_field_size - win_sequence
                      and y >= win_sequence - 1)


def check_win(dot):
    for i in range(vertical_field_size):
        for j in range(horizontal_field_size):
            if check_lines(dot, i, j):
                return True
    return False

def is_map_full():
    for i in range(vertical_field_size):
        for j in range(horizontal_field_size):
            if is_empty_cell(i, j):
                return False
    return True

def game_checks(dot, message):
    if check_win(dot):
        print(message)
        return True
    if is_map_full():
        print('draw!')
        return True
    return False

print_map()
while True:
    turn(first_dot)
    print_map()
    if game_checks(first_dot, "First player win!"):
        break
    turn(second_dot)
    print_map()
    if game_checks(second_dot, "Second player win!"):
        break
