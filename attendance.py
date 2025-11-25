def compute_attendance_percentages(students, attendance_records):
    dates = list(attendance_records.keys())
    total_sessions = len(dates)

    result = {}

    for sid, name in students.items():
        present = sum(1 for d in dates if sid in attendance_records[d])

        if total_sessions > 0:
            pct = (present / total_sessions) * 100
        else:
            pct = 0

        result[sid] = {
            "name": name,
            "attendance_pct": round(pct, 2)
        }

    return result