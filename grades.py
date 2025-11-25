def compute_average_and_grade(marks_list, attendance_pct):

    if len(marks_list) == 0:
        avg = 0
    else:
        avg = sum(marks_list) / len(marks_list)

    avg = round(avg, 2)

    if avg >= 85 and attendance_pct >= 75:
        grade = "A"
    elif avg >= 70 and attendance_pct >= 65:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    else:
        grade = "D"

    return avg, grade