from student_package.student_module import Student

Student.school_name = "Global"
Student.school_address = "rajasthan"

stu1 = Student(1001, "jack", "jack@gmail.com", 45.2)
stu2 = Student(1002, "peter", "peter@gmail.com", 85.2)
stu3 = Student(1003, "mark", "mark@gmail.com", 56.5)

name = stu2.get_student_name()
print(name)

res = stu2.get_name_with_percentage()
print(res)

print(Student.get_school_name())

print(stu3.get_name_with_percentage())

print(stu2.print_grade())
