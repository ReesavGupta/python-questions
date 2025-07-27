from collections import defaultdict

class GradeManager:
    def __init__(self):
        self.data = defaultdict(lambda: defaultdict(list))

    def add_grade(self, student_name, subject, grade):
        self.data[student_name][subject].append(grade)

    def get_student_average(self, student_name):
        subjects = self.data.get(student_name)
        if not subjects:
            return 0
        all_grades = [grade for grades in subjects.values() for grade in grades]
        return sum(all_grades) / len(all_grades) if all_grades else 0

    def get_subject_statistics(self, subject):
        subject_grades = []
        for student_subjects in self.data.values():
            subject_grades.extend(student_subjects.get(subject, []))

        if not subject_grades:
            return {'average': 0, 'highest': 0, 'lowest': 0, 'student_count': 0}

        return {
            'average': sum(subject_grades) / len(subject_grades),
            'highest': max(subject_grades),
            'lowest': min(subject_grades),
            'student_count': len(subject_grades)
        }

    def get_top_students(self, n=3):
        averages = [
            (student, self.get_student_average(student))
            for student in self.data
        ]
        sorted_averages = sorted(averages, key=lambda x: x[1], reverse=True)
        return sorted_averages[:n]

    def get_failing_students(self, passing_grade=60):
        return [
            (student, avg)
            for student, avg in [
                (s, self.get_student_average(s)) for s in self.data
            ]
            if avg < passing_grade
        ]


# ---------------- Test the implementation ----------------

manager = GradeManager()

# Sample grade data
grades_data = [
    ("Alice", "Math", 85),
    ("Alice", "Science", 92),
    ("Alice", "English", 78),

    ("Bob", "Math", 75),
    ("Bob", "Science", 68),
    ("Bob", "English", 82),

    ("Charlie", "Math", 95),
    ("Charlie", "Science", 88),
    ("Charlie", "History", 91),

    ("Diana", "Math", 55),
    ("Diana", "Science", 62),
    ("Diana", "English", 70),

    ("Eve", "Math", 88),
    ("Eve", "Science", 94),
    ("Eve", "English", 86),
    ("Eve", "History", 89)
]


for student, subject, grade in grades_data:
    manager.add_grade(student, subject, grade)

print("Alice's average:", manager.get_student_average("Alice"))

print("Math statistics:", manager.get_subject_statistics("Math"))

print("Top 3 students:", manager.get_top_students(3))

print("Failing students:", manager.get_failing_students(75))
