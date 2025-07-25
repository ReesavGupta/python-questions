employees= [
    ("Alice", 50000, "Engineering"),
    ("Carol", 5500, "Engineering"),
    ("Davide", 4500, "Sales"),
    ("Bob", 60000, "Marketing"),
]


def ascending_and_descending():
    asc = sorted(employees, key=lambda x :x[1])
    for i, employee in enumerate(employees):
        print(i, employee)

    for i, emp in enumerate(asc):
        print(f"{i}. {emp}")        
                        
    desc = sorted(employees, key=lambda x: x[1], reverse=True)
    
def sort_by_department():
    # Sort by department, then salary within each department
    sorted_employees = sorted(employees, key=lambda x: (x[2], x[1]))
    
    print("Sorted by Department, then by Salary:")
    for emp in sorted_employees:
        print(emp)


def reversed_employees_list():
    reversed_list = employees[::-1]
    print("Reversed List (original remains unchanged):")
    for emp in reversed_list:
        print(emp)


def sort_by_name_length():
    sorted_employees = sorted(employees, key=lambda x: len(x[0]))
    print("Employees sorted by name length:")
    for emp in sorted_employees:
        print(emp)


def demonstrate_sorting_methods():
    sorted_by_name = sorted(employees, key=lambda x: x[0])
    print("Sorted by name using sorted():")
    for emp in sorted_by_name:
        print(emp)

    print("\nOriginal list after using sorted():")
    for emp in employees:
        print(emp)

    employees.sort(key=lambda x: x[1])  # Sort by salary
    print("\nOriginal list after using .sort() by salary:")
    for emp in employees:
        print(emp)


ascending_and_descending()
sort_by_department()
reversed_employees_list()
sort_by_name_length()
demonstrate_sorting_methods()