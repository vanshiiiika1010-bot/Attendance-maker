import json

def load_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

            attendance = {
                date: set(studs)
                for date, studs in data.get("attendance", {}).items()
            }

            return data.get("students", {}), attendance, data.get("grades", {})

    except FileNotFoundError:
        return {}, {}, {}

def save_data(students, attendance, grades):

    attendance = {date: list(studs) for date, studs in attendance.items()}

    with open("data.json", "w") as file:
        json.dump({
            "students": students,
            "attendance": attendance,
            "grades": grades
        }, file, indent=4)