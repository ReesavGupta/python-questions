from datetime import datetime

class Employee:
    company_name = "GlobalTech Solutions"
    total_employees = 0
    departments = {"Engineering": 0, "Sales": 0, "HR": 0, "Marketing": 0}
    tax_rates = {"USA": 0.22, "India": 0.18, "UK": 0.25}
    next_employee_id = 1

    def __init__(self, name, department, base_salary, country, email):
        if not Employee.is_valid_department(department):
            raise ValueError("Invalid department")
        if not Employee.validate_email(email):
            raise ValueError("Invalid email")

        self.name = name
        self.department = department
        self.base_salary = base_salary
        self.country = country
        self.email = email
        self.hire_date = datetime.now()
        self.performance_ratings = []

        self.employee_id = Employee.generate_employee_id()
        Employee.total_employees += 1
        Employee.departments[department] += 1

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email.split("@")[-1]

    @staticmethod
    def is_valid_department(dept):
        return dept in Employee.departments

    @staticmethod
    def calculate_tax(salary, country):
        return salary * Employee.tax_rates.get(country, 0)

    @staticmethod
    def generate_employee_id():
        year = datetime.now().year
        eid = f"EMP-{year}-{str(Employee.next_employee_id).zfill(4)}"
        Employee.next_employee_id += 1
        return eid

    @classmethod
    def from_csv_data(cls, csv_line):
        parts = csv_line.split(",")
        return cls(parts[0], parts[1], float(parts[2]), parts[3], parts[4])

    @classmethod
    def get_department_stats(cls):
        stats = {}
        for dept, count in cls.departments.items():
            stats[dept] = {"count": count}
        return stats

    @classmethod
    def set_tax_rate(cls, country, rate):
        cls.tax_rates[country] = rate

    @classmethod
    def hire_bulk_employees(cls, employee_list):
        for line in employee_list:
            cls.from_csv_data(line)

    def add_performance_rating(self, rating):
        if 1 <= rating <= 5:
            self.performance_ratings.append(rating)

    def get_average_performance(self):
        if not self.performance_ratings:
            return 0
        return sum(self.performance_ratings) / len(self.performance_ratings)

    def calculate_net_salary(self):
        tax = Employee.calculate_tax(self.base_salary, self.country)
        return self.base_salary - tax

    def get_years_of_service(self):
        return (datetime.now() - self.hire_date).days / 365

    def is_eligible_for_bonus(self):
        return self.get_average_performance() > 3.5 and self.get_years_of_service() > 1
