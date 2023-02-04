
students = {}

for _ in range(int(input())):
    name, grade = input().split()
    if name not in students.keys():
        students[name] = []
    students[name].append(float(grade))

for student, grades in students.items():
    average_grade = sum(grades) / len(grades)
    all_grades = ' '.join(map(lambda current_grade: f'{current_grade:.2f}', grades))
    print(f"{student} -> {all_grades} (avg: {average_grade:.2f})")
