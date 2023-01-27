import view as v

def start():
    while True:
        operation = v.operation_selection()
        if operation == 1:
            v.add_student()
        elif operation == 2:
            v.add_discipline()
        elif operation == 3:
            v.add_score()
        elif operation == 4:
            v.find_all_students()
        elif operation == 5:
            v.find_all_scores_of_student()
        elif operation == 6:
            v.student_avg_score_in_discipline()
        elif operation == 7:
            v.school_avg_score_in_discipline()
        elif operation == 8:
            v.number_of_gold_medalists()
        elif operation == 9:
            break
