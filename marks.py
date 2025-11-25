from attendance import compute_attendance_percentages
from grades import compute_average_and_grade
from storage import load_data, save_data

def menu():
    print("\n--- Student Attendance & Performance Manager ---")
    print("1. Add Student")
    print("2. Mark Attendance")
    print("3. Add Marks")
    print("4. View Report")
    print("5. Exit")

def main():
    students, attendance, grades = load_data()

    while True:
        menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Student Name: ")
            students[sid] = name
            print("Student added successfully!")

        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            if date not in attendance:
                attendance[date] = set()

            for sid in students:
                status = input(f"{students[sid]} (P/A): ").upper()
                if status == "P":
                    attendance[date].add(sid)

            print("Attendance recorded!")

        elif choice == "3":
            sid = input("Student ID: ")
            if sid not in students:
                print("Student not found!")
                continue

            mark = int(input("Enter mark: "))
            grades.setdefault(sid, []).append(mark)
            print("Marks added!")

        elif choice == "4":
            report = compute_attendance_percentages(students, attendance)

            print("\n---- STUDENT REPORT ----")
            for sid, data in report.items():
                avg, grade = compute_average_and_grade(
                    grades.get(sid, []),
                    data["attendance_pct"]
                )

                print(f"ID: {sid}")
                print(f"Name: {data['name']}")
                print(f"Attendance: {data['attendance_pct']}%")
                print(f"Average Marks: {avg}")
                print(f"Grade: {grade}")
                print("-----------------------")

        elif choice == "5":
            save_data(students, attendance, grades)
            print("Data saved. Exiting program...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()