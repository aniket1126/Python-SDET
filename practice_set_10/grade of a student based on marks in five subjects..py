def calculate_grade(marks):
    total_marks = sum(marks)
    average_marks = total_marks / 5
    if average_marks >= 90:
        grade = 'A'
    elif average_marks >= 75:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'D'
    return f"Average Marks: {average_marks:}, Grade: {grade}"

marks = [85, 90, 78, 92, 88]
print(calculate_grade(marks))
