from demo4_employee_class.employee_module import Employee


Employee.company_name = "Einfochips"
Employee.company_location = "Ahemdabad"
print(Employee.company_name)
print(Employee.company_location)


emp1 = Employee()
emp2 = Employee()
emp3 = Employee()

emp1.emp_id = "1"
emp1.emp_name="kim3"
emp1.emp_salary="103300"
emp1.emp_performance="A"

emp2.emp_id = "2"
emp2.emp_name="kim"
emp2.emp_salary="1000"
emp2.emp_performance="A"

emp3.emp_id = "3"
emp2.emp_name="okau"
emp2.emp_salary="3000"
emp2.emp_performance="C"


print(emp1.emp_id)
print(emp2.emp_id)
print(emp3.emp_id)
