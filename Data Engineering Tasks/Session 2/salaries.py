""" you're given a list of dictionaries containing information about
different employees in a company. Each dictionary has keys for the
employee's name, salary, and department. Your task is to write a Python
function that returns a dictionary containing the total salary for each
department. employees = [ {'name': 'Alice', 'salary': 50000,
'department': 'Sales'}, {'name': 'Bob', 'salary': 60000, 'department':
'Sales'}} Output: {'Sales': 110000, 'Marketing': 150000, 'Engineering':
190000}
"""

employees = [
    {'name': 'Alice', 'salary': 50000, 'department': 'Sales'},
    {'name': 'Bob', 'salary': 60000, 'department': 'Sales'},
    {'name': 'Charlie', 'salary': 70000, 'department': 'Marketing'},
    {'name': 'David', 'salary': 80000, 'department': 'Marketing'},
    {'name': 'Eve', 'salary': 90000, 'department': 'Engineering'},
    {'name': 'Frank', 'salary': 100000, 'department': 'Engineering'}
]

def department_salaries(employees):
    department_totals = {}
    for employee in employees:
        if employee['department'] not in department_totals:
            department_totals[employee['department']] = employee['salary']
           # print(department_totals)
        else:
            department_totals[employee['department']] += employee['salary']
    return department_totals
print(department_salaries(employees))


