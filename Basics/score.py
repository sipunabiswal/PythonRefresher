students_scores = [120, 95, 85, 70, 60, 50, 40, 30, 20, 10, 199, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
total_students = len(students_scores)
total_score = sum(students_scores)
average_score = total_score / total_students
print(f"Total students: {total_students}")
print(f"Total score: {total_score}")
print(f"Average score: {average_score:.2f}")


max_score = max(students_scores)

max_score1=0

for i in students_scores:
    if i > max_score1:
        max_score1 = i

print(f"Max score1: {max_score1}")