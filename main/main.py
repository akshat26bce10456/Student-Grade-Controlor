from display import display_student
from grading import calculate_grade, calculate_result
from performance import performance


SUBJECTS = {
    "evs": "EVS",
    "calculus": "Calculus",
    "programming": "Programming",
}


def collect_student(student_number):
    print(f"\nStudent {student_number} details")
    name = input("Enter your name: ").strip()
    registration_number = input("Enter your registration number: ").strip()
    subjects = {}

    for subject, display_name in SUBJECTS.items():
        while True:
            try:
                marks = float(input(f"Enter your {display_name} marks (0-100): "))
            except ValueError:
                print("Please enter a numeric mark.")
                continue

            if 0 <= marks <= 100:
                subjects[subject] = marks
                break

            print("Marks must be between 0 and 100.")

    percentage = sum(subjects.values()) / len(subjects)
    grade = calculate_grade(percentage)
    weak_subjects = [subject for subject, marks in subjects.items() if marks < 20]

    return {
        "name": name,
        "registration_number": registration_number,
        "subjects": subjects,
        "percentage": percentage,
        "grade": grade,
        "result": calculate_result(percentage, grade),
        "performance": performance(percentage),
        "weak_subjects": weak_subjects,
    }


def main():
    students = [collect_student(number) for number in range(1, 6)]
    students.sort(key=lambda student: student["percentage"], reverse=True)

    print("\nFinal results")
    for rank, student in enumerate(students, start=1):
        display_student(rank, student)
        print(f"Performance: {student['performance']}")
 
    topper = students[0]
    print(f"\nTopper: {topper['name']} ({topper['percentage']:.2f}%)")


if __name__ == "__main__":
    main()
