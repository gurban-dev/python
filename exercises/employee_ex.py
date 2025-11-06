'''
Class variables: Define company_name and employee_count
                 shared across all instances.

Instance variables: Store individual name, salary, and
                    department for each object.

Instance methods: Implement give_raise() and get_info() that
                  work with instance data.

Class methods: Create get_employee_count() and from_monthly_salary()
               (an alternative constructor).

Inheritance: Make Manager inherit from Employee and override
             get_info().
'''

class Employee: 
  company_name = "Ecofriendlyfishing"
  employee_count = 0

  def __init__(self, employee_name, salary, department):
    self.employee_name = employee_name
    self.salary = salary
    self.department = department

    Employee.employee_count += 1

  def get_employee_name(self):
    return self.employee_name

  def get_salary(self):
    return self.salary

  def set_salary(self, new_salary):
    self.salary = new_salary

  @classmethod
  def get_employee_count(cls):
    return cls.employee_count

john = Employee("John", "50,000", "Sales")
print(john.salary)

print(john.get_salary())

john.set_salary("75,000")

print(john.get_salary())

print(john.get_employee_count())

print(Employee.get_employee_count())

employees = {
  "Sales": {"first year": john.get_employee_name()},
}
print(employees.items())

for key, value in employees.items():
  print(key, value)

  for duration, employee_name in value.items():
    print(duration, employee_name)