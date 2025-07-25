students = [
    (101, "Alice", 85, 20),
    (102, "Bob", 92, 21),
    (103, "Carol", 78, 22),
    (104, "David", 88, 20)
]

def find_top_student(students):
    top_student = max(students ,key=lambda x: x[2])
    print("Student with the highest grade:")
    print(f"ID: {top_student[0]}, Name: {top_student[1]}, Grade: {top_student[2]}, Age: {top_student[3]}")

def create_name_grade_list(students):
    name_grade_list = [(name, grade) for _, name, grade, _ in students]
    print("\nName-Grade List:")
    print(name_grade_list)

def demonstrate_tuple_immutability(students):
    print("\nAttempting to change a student's grade (should fail)...")
    try:
        students[0][2] = 100
    except TypeError as e:
        print("Error:", e)
        print("Explanation: Tuples are immutable — their elements cannot be changed after creation.")
        print("This is why tuples are preferred for fixed records like student data.")

find_top_student(students)
create_name_grade_list(students)
demonstrate_tuple_immutability(students)
