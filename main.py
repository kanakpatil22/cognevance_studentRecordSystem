import os
import json

FILE_NAME = "students.json"


def load_students():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump(students, f, indent=4)


def add_student():
    students = load_students()
    try:
        roll_no = input("Enter Roll No: ").strip()

        for s in students:
            if s["roll_no"] == roll_no:
                print("Student with this Roll No already exists!\n")
                return

        name = input("Enter Name: ").strip()
        marks = float(input("Enter Marks (out of 100): ").strip())

        if not roll_no or not name:
            print("Roll No and Name cannot be empty!\n")
            return

        if marks < 0 or marks > 100:
            print("Marks should be between 0 and 100!\n")
            return

        student = {"roll_no": roll_no, "name": name, "marks": marks}
        students.append(student)
        save_students(students)
        print("Student added successfully!\n")

    except ValueError:
        print("Invalid input! Marks must be a number.\n")


def view_students():
    students = load_students()
    if not students:
        print("No records found.\n")
        return

    print("\n" + "-" * 45)
    print(f"{'Roll No':<10}{'Name':<20}{'Marks':<10}")
    print("-" * 45)
    for s in students:
        print(f"{s['roll_no']:<10}{s['name']:<20}{s['marks']:<10}")
    print("-" * 45 + "\n")


def update_student():
    students = load_students()
    roll_no = input("Enter Roll No to update: ").strip()

    for s in students:
        if s["roll_no"] == roll_no:
            try:
                new_name = input(f"Enter new name (current: {s['name']}): ").strip()
                new_marks = input(f"Enter new marks (current: {s['marks']}): ").strip()

                if new_name:
                    s["name"] = new_name
                if new_marks:
                    marks_val = float(new_marks)
                    if 0 <= marks_val <= 100:
                        s["marks"] = marks_val
                    else:
                        print("Marks should be between 0 and 100! Skipped.\n")

                save_students(students)
                print("Student record updated!\n")
                return
            except ValueError:
                print("Invalid marks input!\n")
                return

    print("Student not found!\n")


def delete_student():
    students = load_students()
    roll_no = input("Enter Roll No to delete: ").strip()

    for s in students:
        if s["roll_no"] == roll_no:
            confirm = input(f"Are you sure you want to delete {s['name']}? (y/n): ").strip().lower()
            if confirm == "y":
                students.remove(s)
                save_students(students)
                print("Student deleted successfully!\n")
            else:
                print("Deletion cancelled.\n")
            return

    print("Student not found!\n")


def search_student():
    students = load_students()
    roll_no = input("Enter Roll No to search: ").strip()

    for s in students:
        if s["roll_no"] == roll_no:
            print("\nStudent Found:")
            print(f"Roll No: {s['roll_no']}")
            print(f"Name   : {s['name']}")
            print(f"Marks  : {s['marks']}\n")
            return

    print("Student not found!\n")


def generate_report():
    students = load_students()
    if not students:
        print("No records to generate report.\n")
        return

    total_students = len(students)
    total_marks = sum(s["marks"] for s in students)
    average = total_marks / total_students
    topper = max(students, key=lambda s: s["marks"])
    passed = [s for s in students if s["marks"] >= 40]
    failed = [s for s in students if s["marks"] < 40]

    print("\n" + "=" * 40)
    print("        STUDENT PERFORMANCE REPORT")
    print("=" * 40)
    print(f"Total Students   : {total_students}")
    print(f"Average Marks    : {average:.2f}")
    print(f"Topper           : {topper['name']} ({topper['marks']} marks)")
    print(f"Passed Students  : {len(passed)}")
    print(f"Failed Students  : {len(failed)}")
    print("=" * 40 + "\n")


def show_menu():
    print("\n===== STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Search Student")
    print("6. Generate Report")
    print("7. Exit")
    print("=" * 45)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            update_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            search_student()
        elif choice == "6":
            generate_report()
        elif choice == "7":
            print("Exiting... Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-7.\n")


if __name__ == "__main__":
    main()