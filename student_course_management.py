from collections import defaultdict

class Course:
    all_courses = []
    total_enrollment_count = 0
    def __init__(self, course_code, title, instructor, credits, max_enrollment):
        self.course_code = course_code
        self.title = title
        self.instructor = instructor
        self.credits = credits
        self.max_enrollment = max_enrollment
        self.enrolled_students = {}
        self.grades = {}
        self.waitlist = []
        Course.all_courses.append(self)

    def __str__(self):
        return f"{self.course_code} - {self.title} by {self.instructor}"

    def get_available_spots(self):
        return self.max_enrollment - len(self.enrolled_students)

    def enroll(self, student):
        if len(self.enrolled_students) < self.max_enrollment:
            self.enrolled_students[student.student_id] = student
            Course.total_enrollment_count += 1
            return True
        else:
            self.waitlist.append(student)
            return False

    def add_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_enrollment_count(self):
        return len(self.enrolled_students)

    def is_full(self):
        return len(self.enrolled_students) >= self.max_enrollment

    def get_course_statistics(self):
        if not self.grades:
            return {"average": None, "highest": None, "lowest": None}
        grades = list(self.grades.values())
        return {
            "average": sum(grades) / len(grades),
            "highest": max(grades),
            "lowest": min(grades)
        }
    @classmethod        
    def get_enrollment_count(cls):
        return cls.total_enrollment_count
    

class Student:
    all_students = {}

    def __init__(self, student_id, name, email, program):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.program = program
        self.enrollments = {}
        self.transcript = {}
        Student.all_students[student_id] = self

    def __str__(self):
        return f"{self.name} ({self.student_id}) - {self.program}"

    def enroll_in_course(self, course):
        success = course.enroll(self)
        if success:
            self.enrollments[course.course_code] = course
        return success

    def add_grade(self, course_code, grade):
        self.transcript[course_code] = grade

    def calculate_gpa(self):
        if not self.transcript:
            return 0.0
        total_points = sum(self.transcript.values())
        return round(total_points / len(self.transcript), 2)

    def get_transcript(self):
        return self.transcript

    @classmethod
    def get_total_students(cls):
        return len(cls.all_students)

    @classmethod
    def get_total_enrollments(cls):
        total = 0
        for course in Course.all_courses:
            total += len(course.enrolled_students)
        return total

    @classmethod
    def get_average_gpa(cls):
        gpas = [s.calculate_gpa() for s in cls.all_students.values() if s.transcript]
        return round(sum(gpas) / len(gpas), 2) if gpas else 0.0

    @classmethod
    def get_top_students(cls, n=1):
        students_with_gpa = [
            (student.name, student.calculate_gpa())
            for student in cls.all_students.values()
            if student.transcript
        ]
        students_with_gpa.sort(key=lambda x: x[1], reverse=True)
        return students_with_gpa[:n]


# ---------------- TEST CASES ---------------- #

# Test Case 1: Creating courses with enrollment limits
math_course = Course("MATH101", "Calculus I", "Dr. Smith", 3, 30)
physics_course = Course("PHYS101", "Physics I", "Dr. Johnson", 4, 25)
cs_course = Course("CS101", "Programming Basics", "Prof. Brown", 3, 20)

print(f"\nCourse: {math_course}")
print(f"Available spots in Math: {math_course.get_available_spots()}")

# Test Case 2: Creating students with different programs
student1 = Student("S001", "Alice Wilson", "alice@university.edu", "Computer Science")
student2 = Student("S002", "Bob Davis", "bob@university.edu", "Mathematics")
student3 = Student("S003", "Carol Lee", "carol@university.edu", "Physics")

print(f"\nStudent: {student1}")
print(f"Total students: {Student.get_total_students()}")

# Test Case 3: Course enrollment
enrollment1 = student1.enroll_in_course(math_course)
enrollment2 = student1.enroll_in_course(cs_course)
enrollment3 = student2.enroll_in_course(math_course)

print(f"\nAlice's enrollment in Math: {enrollment1}")
print(f"Math course enrollment count: {math_course.get_enrollment_count()}")

# Test Case 4: Adding grades and calculating GPA
student1.add_grade("MATH101", 85.5)
student1.add_grade("CS101", 92.0)
student2.add_grade("MATH101", 78.3)

print(f"\nAlice's GPA: {student1.calculate_gpa()}")
print(f"Alice's transcript: {student1.get_transcript()}")

# Test Case 5: Course statistics
math_course.add_grade("S001", 85.5)
math_course.add_grade("S002", 78.3)

course_stats = math_course.get_course_statistics()
print(f"\nMath course statistics: {course_stats}")

# Test Case 6: University-wide analytics
total_enrollments = Course.get_enrollment_count()
print(f"\nTotal enrollments across all courses: {total_enrollments}")

average_gpa = Student.get_average_gpa()
print(f"University average GPA: {average_gpa}")

top_students = Student.get_top_students(2)
print(f"Top 2 students: {top_students}")

# Test Case 7: Enrollment limits and waitlist
for i in range(25):  # Assuming math course limit is 30 (already has 2 enrolled)
    temp_student = Student(f"S100{i}", f"Student {i}", f"student{i}@uni.edu", "General")
    result = temp_student.enroll_in_course(math_course)

print(f"\nCourse full status: {math_course.is_full()}")
print(f"Waitlist size: {len(math_course.waitlist) if hasattr(math_course, 'waitlist') else 0}")
