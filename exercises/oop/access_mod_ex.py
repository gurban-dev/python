'''
Exercise: Employee System with Polymorphism and Attribute Naming Conventions


Concepts:

Polymorphism in Python

Public, protected, and private attribute naming conventions

__str__ and __repr__ methods

You are building a small system that models employees at a company.

All employees have:

name -> public

base salary -> protected

internal ID -> private

Different types of employees calculate their annual pay differently.


Part 1: Base Class

Create a class called Employee.

Requirements:

Attributes
name -> public instance variable

_base_salary -> protected instance variable

__employee_id -> private instance variable

Methods
get_annual_pay() -> Returns the annual pay. For a basic employee, this
is base_salary * 12.

get_id() -> Returns the employee's ID (the only legal way to access it).

__str__() -> Returns a human-readable string for the object. Example:

Employee(name: Alice, annual_pay: $36,000.00)


__repr__() -> Returns a detailed string representation for debugging,
ideally enough to recreate the object. Example:

Employee(name='Alice', base_salary=3000, employee_id=101)


Part 2: Subclasses

Create two subclasses:

Manager

Gets a 20% bonus on top of annual pay.

Overrides get_annual_pay().

Contractor

Paid hourly using _base_salary as the hourly rate.

Annual pay = hourly rate x 40 hours/week x 52 weeks/year.

Overrides get_annual_pay().


Part 3: Testing

Create a list of employees that includes an Employee, a Manager, and a Contractor.

Print the employees using print() (calls __str__()) and also print the
list of employees (calls __repr__() on each object).

Use str() to convert each employee to a string.
Join the results using newline characters ('\n') and print the final formatted
output.
'''