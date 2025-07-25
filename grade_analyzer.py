grades = [85, 92, 78, 90, 88, 76, 94, 89, 87, 91]

sliced_grades = grades[2:7]
print("Sliced grades (index 2 to 6):", sliced_grades)

grades_above_85 = [grade for grade in grades if grade > 85]
print("Grades above 85:", grades_above_85)

grades[3] = 95
print("After replacing index 3 with 95:", grades)

grades.extend([86, 93, 79])
print("After appending new grades:", grades)

sorted_desc = sorted(grades, reverse=True)
top_5_grades = sorted_desc[:5]
print("Top 5 grades (descending):", top_5_grades)