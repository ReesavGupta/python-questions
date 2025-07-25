students = ["Alice", "Bob", "Carol", "David", "Eve"]
scores  =[85, 92, 78, 88, 95]

def print_numbered_student_list():
    for i, name in enumerate(students, start=1):
        print(f"{i}. {name}")

def pair_students_with_scores():
    for i, (name, score) in enumerate(zip(students, scores), start=1):
        print(f"{i}. {name} - {score}")
        
def print_positions_of_high_scores():
    for i, (name, score) in  enumerate(zip(students, scores), start=0):
        if score > 90:
            print(f"{name} scored {score} and their index is {i}")

def map_position_to_student_names():
    dictionay = {}
    for i, (name, score) in enumerate(zip(students, scores)):
        dictionay[i] = name

    print(dictionay)


# Map Positions to Student Names

# Create a dictionary where keys are positions (starting from 0) and values are the student names.


print_numbered_student_list()
pair_students_with_scores()
print_positions_of_high_scores()
map_position_to_student_names()