'''
Concepts covered:
Class variables: Define company_name and employee_count
                 shared across all instances.

Instance variables: Store employee_name, salary, and
                    department for each object.

Instance methods: Implement give_raise() and get_info() that
                  work with instance data.

Class methods: Create get_employee_count() and from_monthly_salary()
               (an alternative constructor).

Inheritance: Make a child/derived class called "Manager" inherit
             from the Employee class and override get_info().
'''

class Employee:
  # Class variables.
  company_name = "Eco Fishing"
  employee_count = 0

  def __init__(self, employee_name: str, salary: str, department: str):
    # Instance variables.
    self.employee_name: str = employee_name
    self.salary: str = salary
    self.department: str = department

    Employee.employee_count += 1

  # Alternative constructor for this class.
  @classmethod
  def from_monthly_salary(
    cls, employee_name: str, monthly_salary: str, department: str):
    annual_salary: float = float(monthly_salary) * 12

    cls.employee_count += 1

    # cls refers to the class itself (Employee).
    # cls(employee_name, salary, department) invokes the
    # constructor of the Employee class.
    return cls(employee_name, str(annual_salary), department)

  # Selector/getter because it returns an instance variable.
  def get_employee_name(self):
    return self.employee_name

  def get_salary(self):
    return self.salary

  # Mutator/setter because it modifies an instance variable.
  def set_salary(self, new_salary: str):
    self.salary = new_salary

  def get_info(self):
    return f"Employee Name: {self.employee_name}, Salary: {self.salary}, " \
           f"Department: {self.department}"

  @classmethod
  def get_employee_count(cls):
    return cls.employee_count

# How do I know that Manager is inheriting from Employee?
# Answer:
# The Employee class is included in the parentheses of Manager's
# definition.
class Manager(Employee):
  # Constructor method for Manager class.
  def __init__(
      self, employee_name: str, salary: str, department: str, managed_team: list[str]):
    # Call the parent class' constructor to initialise inherited
    # instance variables/attributes.
    super().__init__(employee_name, salary, department)

    self.managed_team: list[str] = managed_team

  # Override the get_info method to include managed team information.
  # If the Manager class does not have its own get_info() method,
  # it will simply use the one defined in its parent class.
  def get_info(self):
    return f"Manager Name: {self.employee_name}, Salary: {self.salary}, " \
           f"Department: {self.department}, Managed Team: {self.managed_team}"

john: Employee = Employee("John", "50,000", "Sales")
print(john.salary)

print(john.get_salary())

john.set_salary("75,000")

print(john.get_salary())

print(john.get_employee_count())

print(Employee.get_employee_count())

employees: dict[str, dict[str, str]] = {
  "Sales": {"first year": john.get_employee_name()},
}

print(employees.items())

for key, value in employees.items():
  print(key, value)

  for duration, employee_name in value.items():
    print(duration, employee_name)

manager: Manager = Manager("Jane", "90,000", "Sales", ["Alice", "Bob"])

# sep='' remove the space between the two arguments in the print()
# function.
# sep='' is a keyword argument because the parameter name "sep"
# is explicitly specified.
print('\nmanager.get_info():\n', manager.get_info(), sep='')

print('\njohn.get_info():\n', john.get_info(), sep='')

alice: Employee = Employee.from_monthly_salary("Alice", "6000", "Marketing")

print(f'\nalice.get_info():\n{alice.get_info()}', sep='')