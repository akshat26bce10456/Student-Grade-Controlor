def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def calculate_result(percentage, grade):
    if grade == "F":
        return "Your marks are below 50%, so you are failed."
    return "Passed"