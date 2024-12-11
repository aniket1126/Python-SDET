students = [{"name": "Aniket", "age": 23}, {"name": "ansh", "age": 21}, {"name": "Charan", "age": 22}]
sorted_students = sorted(students, key=lambda student: student["age"])
print(sorted_students)
