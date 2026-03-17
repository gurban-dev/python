class Employee:
    def __init__(self, name, base_salary, employee_id):
        # Public naming convention.
        self.name = name

        # Protected naming convention.
        self._base_salary = base_salary

        # Private naming convention.
        self.__employee_id = employee_id

    def get_annual_pay(self):
        return self._base_salary * 12

    def get_id(self):
        return self.__employee_id

    # The __str__() method defines the human-readable string representation
    # of an object. It makes objects human-readable.
    def __str__(self):
        # Called by print() and str().
        return (
            f"{self.__class__.__name__}("
            f"name: {self.name}, "
            f"annual_pay: ${self.get_annual_pay():,.2f}"
            f")"
        )
    
    # The purpose of __repr__() is to produce a string that, ideally, could be
    # used to recreate the object.

    # Using !r ensures that if you printed a list of objects, you see quotes
    # around strings and exact values for numbers as opposed to numbers that
    # were rounded for readability.

    # Unlike the __str__() method, the __repr__() method will print
    # object details of objects that are in a list.
    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"name: {self.name!r}, "
            f"base_salary: {self._base_salary!r}, "
            f"employee_id: {self.get_id()!r})"
        )


class Manager(Employee):
    def get_annual_pay(self):
        return super().get_annual_pay() * 1.20


class Contractor(Employee):
    def get_annual_pay(self):
        return self._base_salary * 40 * 52

employees = [
    Employee("Alice", 3000, 101),
    Manager("Bob", 5000, 102),
    Contractor("Charlie", 60, 103)
]

emp = employees[0]

print('emp:', emp, '\n')

# Invokes __str__().
print('str(emp):', str(emp), '\n')

# Invokes __repr__().
print('repr(emp):', repr(emp), '\n')

# __repr__() is used for printing out objects that are list elements.
print("employees:\n", employees, '\n', sep='')

# '\n' is a newline escape sequence.

# .join(iterable) is a string method that takes an iterable of strings
# and concatenates them with the string as separator.

# In this case, the iterable of strings is 'employees' and they are being
# concatenated with '\n'.
print(f'\n'.join(str(employee) for employee in employees))