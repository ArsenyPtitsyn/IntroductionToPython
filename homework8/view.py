def operation_selection():
    operation = int(input('Меню:\n1 - Добавить нового студента\n2 - Добавить предмет\n'
          '3 - Добавить ученику оценку по предмету\n4 - Показать список учеников\n'
          '5 - Показать лист оценок конкретного ученика по всем предметам\n'
          '6 - Узнать средний балл студента по предмету\n'
          '7 - Узнать средний балл по школе по конкретному предмету\n'
          '8 - Количество студентов, претендующих на золотую медаль\n'
          '9 - Выход: '))
    return operation

def add_student():
    id = int(input('Введите идентификационный номер студента: '))
    name = input('Введите имя студента: ')
    surname = input('Введите фамилию студента: ')
    student = f'{id} - {surname} {name}\n'
    with open('students_list.txt', 'a') as file:
        file.write(student)
    print('Студент добавлен')

def add_discipline():
    id = int(input('Введите идентификационный номер дисциплины: '))
    title = input('Введите название дисциплины: ')
    discipline = f'{id} - {title}\n'
    with open('disciplines_list.txt', 'a') as file:
        file.write(discipline)
    print("Добавлена дисциплина")

def add_score():
    id_student = int(input('Введите идентификационный номер студента: '))
    student = find_student(id_student)
    id_discipline = int(input('Введите идентификационный номер дисциплины: '))
    discipline = find_discipline(id_discipline)
    score = int(input(f'Введите оценку студента: '))
    score_line = f'{student}, {discipline}, {score}\n'
    with open('scores_list.txt', 'a') as file:
        file.write(score_line)
    print(f'Добавили оценку студенту {student} по дисциплине {discipline}')


def find_student(id):
    with open('students_list.txt', 'r') as file:
        for line in file.readlines():
            if id == int(line.split(' - ')[0]):
                return line[:-1]
            else:
                print('Нет студента с таким идентификационным номером!')

def find_discipline(id):
    with open('disciplines_list.txt', 'r') as file:
        for line in file.readlines():
            if id == int(line.split(' - ')[0]):
                return line[:-1]
            else:
                print('Нет дисциплины с таким идентификационным номером!')

def find_all_students():
    students_ids = []
    with open('students_list.txt', 'r') as file:
        for line in file.readlines():
            print(line.split(' - ')[1],end='')
            students_ids.append(int(line.split(' - ')[0]))
    return students_ids

def find_all_scores_of_student():
    all_scores_of_student = []
    id_student = input("Введите идентификационный номер студента: ")
    with open('scores_list.txt', 'r') as file:
        for line in file.readlines():
            if line.split(', ')[0].split(' - ')[0] == id_student:
                all_scores_of_student.append(line[:-1])
                print(line, end='')
    return all_scores_of_student

def student_avg_score_in_discipline():
    id_student = int(input('Введите идентификационный номер студента: '))
    student = find_student(id_student)
    id_discipline = int(input('Введите идентификационный номер дисциплины: '))
    discipline = find_discipline(id_discipline)
    avg_score = 0
    counter = 0
    with open('scores_list.txt', 'r') as file:
        for line in file.readlines():
            if int(line.split(', ')[0].split(' - ')[0]) == id_student and int(line.split(', ')[1].split(' - ')[0]) == id_discipline:
                avg_score += int(line.split(', ')[2])
                counter += 1
        if counter == 0:
            print(f'У студента {student} нет оценок по предмету {discipline}')
        else:
            print(f'Средний балл студента {student} по предмету {discipline} равен: {avg_score/counter}')

def school_avg_score_in_discipline():
    id_discipline = int(input('Введите идентификационный номер дисциплины: '))
    discipline = find_discipline(id_discipline)
    avg_score = 0
    counter = 0
    with open('scores_list.txt', 'r') as file:
        for line in file.readlines():
            if int(line.split(', ')[1].split(' - ')[0]) == id_discipline:
                avg_score += int(line.split(', ')[2])
                counter += 1
        if counter == 0:
            print(f'Никто ещё не получал оценок по предмету {discipline}')
        else:
            print(f'Средний бал по школе по предмету {discipline} равен {avg_score/counter}')

# def number_of_gold_medalists():
#     students_ids = find_all_students()
#     for student_id in students_ids:
#         with open('scores_list.txt', 'r') as file:



