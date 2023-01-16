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
            change_dot(dot)
            break
        print("Ячейки с такими индексами не существует или же она занята!")

def change_dot(dot):
    if dot == first_dot:
        dot = second_dot
    elif dot == second_dot:
        dot = first_dot


def check_line(dot, y, x, dy, dx, condition):
    if condition:
        for i in range(win_sequence):
            if field[y + dy * i][x + dx * i] == c:
                continue
            else:
                return False
        return True


def check_lines(dot, y, x):


def check_win(dot):


def is_map_full():


def game_checks(dot, message):


