def display_student(rank, student):
    print(f"\nRank {rank}: {student['name']} - "
          f"{student['registration_number']}")

    print(f"Percentage: {student['percentage']:.2f}%")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['result']}")

    print("Subject marks:")

    for subject, mark in student["subjects"].items():
        subject_result = "Passed" if mark >= 20 else "Failed"
        print(f"  {subject}: {mark:.2f} - {subject_result}")

    if student["weak_subjects"]:
        print(f"Weak subjects: {', '.join(student['weak_subjects'])}")