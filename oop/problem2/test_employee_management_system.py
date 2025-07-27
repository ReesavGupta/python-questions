from datetime import datetime, timedelta
from employee_management_system import Employee

def test_class_setup_and_basic_functionality():
    Employee.company_name = "GlobalTech Solutions"
    Employee.tax_rates = {"USA": 0.22, "India": 0.18, "UK": 0.25}
    Employee.departments = {"Engineering": 0, "Sales": 0, "HR": 0, "Marketing": 0}

    emp1 = Employee("John Smith", "Engineering", 85000, "USA", "john.smith@globaltech.com")
    current_year = datetime.now().year
    assert emp1.employee_id.startswith(f"EMP-{current_year}-")
    assert Employee.total_employees == 1
    assert Employee.departments["Engineering"] == 1

def test_static_methods():
    assert Employee.validate_email("test@company.com") is True
    assert Employee.validate_email("invalid.email") is False
    assert Employee.is_valid_department("Engineering") is True
    assert Employee.is_valid_department("InvalidDept") is False
    assert abs(Employee.calculate_tax(100000, "USA") - 22000) < 0.01

def test_class_methods_and_bulk_operations():
    emp2 = Employee.from_csv_data("Sarah Johnson,Sales,75000,UK,sarah.j@globaltech.com")
    assert emp2.name == "Sarah Johnson"
    assert emp2.department == "Sales"
    assert Employee.departments["Sales"] == 1

    bulk_data = [
        "Mike Wilson,Marketing,65000,India,mike.w@globaltech.com",
        "Lisa Chen,HR,70000,USA,lisa.chen@globaltech.com"
    ]
    Employee.hire_bulk_employees(bulk_data)
    assert Employee.total_employees == 4

    stats = Employee.get_department_stats()
    assert stats["Engineering"]["count"] == 1
    assert stats["Sales"]["count"] == 1

def test_performance_and_bonus_calculations():
    emp = Employee("Jane Doe", "Engineering", 90000, "USA", "jane.doe@globaltech.com")
    emp.add_performance_rating(4.2)
    emp.add_performance_rating(3.8)
    emp.add_performance_rating(4.5)
    assert abs(emp.get_average_performance() - 4.17) < 0.01

    emp.hire_date = datetime.now() - timedelta(days=800)
    assert emp.get_years_of_service() >= 2
    assert emp.is_eligible_for_bonus() is True

def test_salary_calculation():
    emp = Employee("Tom Banner", "HR", 85000, "USA", "tom.banner@globaltech.com")
    net_salary = emp.calculate_net_salary()
    expected_net = 85000 - (85000 * 0.22)
    assert abs(net_salary - expected_net) < 0.01
