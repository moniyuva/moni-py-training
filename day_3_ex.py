MIN_TOTAL = 0
MAX_TOTAL = 100
FAIL_LIMIT = 40

global total_fail
total_fail = 0

global total_pass
total_pass = 0


def calc_avg(total_marks, num_stud):
    avg = total_marks / (num_stud * MAX_TOTAL)
    return round(avg * MAX_TOTAL, 2)


def validate_mark(stu_mark):
    global total_fail
    global total_pass

    if stu_mark < MIN_TOTAL or stu_mark > MAX_TOTAL:
        return False # Invalid student mark
    else:
        if stu_mark < FAIL_LIMIT:
            total_fail += 1
            print(f'Student mark {stu_mark} is FAIL')
        else:
            total_pass += 1
        return True


def get_marks(num_students):
    total_marks = 0.0
    temp_num_stud = num_students
    print('Now Enter the student marks:')
    for i in range(num_students):
        stu_mark = float(input(f'Student {i+1}.'))
        is_mark_valid = validate_mark(stu_mark)
        if is_mark_valid:
            total_marks += stu_mark
        else:
            print(f'\tInvalid Student Mark {i+1}.{stu_mark}')
            temp_num_stud -= 1
    return total_marks, temp_num_stud
        

num_students = int(input('Enter the total no. of students:'))
print("Total number of students:", num_students)
total_marks, mod_num_stud = get_marks(num_students)
print(f"Total valid marks entered for {mod_num_stud} students is {total_marks}")
class_avg = calc_avg(total_marks, mod_num_stud)
print(f"Average is {class_avg}")
print(f'No. of students passed:{total_pass}')
print(f'No. of studenrs failed: {total_fail}')
