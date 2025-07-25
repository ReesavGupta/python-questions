school = {
    "Math": {
        "teacher": "Mr. Smith",
        "students": [("Alice", 85), ("Bob", 92), ("Carol", 78)] 
    },
    "Science": {
        "teacher": "Ms. Jhonson",
        "students": [("David", 88), ("Eve", 94), ("Frank", 82)]
    }
}

def print_teacher_name():
    for subject, details in school.items():
        teacher = details["teacher"]
        print(f"The teacher for {subject} is {teacher}")

def calculate_class_average_grades():
    for subject, details in school.items():
        students=details["students"]
        count = len(students)
        total = 0
        
        for name, grade in students:
            total += grade
        average = total / count

        print(f"{subject} class average: {average:.2f}")

def find_top_students_for_each_class():
    top_student = None
    top_grade = -1
    top_subject = ""

    for subject, details in school.items():
        for name, grade in details["students"]:
            if grade > top_grade:
                top_grade = grade
                top_student = name
                top_subject = subject

    print(f"Top student: {top_student} with grade {top_grade} in {top_subject}")



if __name__ == "__main__":
    print_teacher_name()
    calculate_class_average_grades()
    find_top_students_for_each_class()