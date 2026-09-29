def performance(percentage):
    if percentage >= 90:
        return "Excellent"
    elif percentage >= 80:
        return "Very Good"
    elif percentage >= 70:
        return "Good"
    elif percentage >= 60:
        return "Satisfactory"
    elif percentage >= 50:
        return "Needs Improvement"
    else:
        return "Poor"
