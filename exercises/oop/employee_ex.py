'''
Exercise: Employee and Manager Classes


Concepts:

Class variables:
Define company_name and employee_count shared across all instances.

Instance variables:
Store employee_name, salary, and department for each object.

Instance methods:
Implement give_raise() and get_info() that work with instance data.

Class methods:
Create get_employee_count() and from_monthly_salary() (an
alternative constructor).

Inheritance: Make a child/derived class called Manager inherit from
the Employee class and override get_info().


Instructions

1. Create the Employee class

   Define a class named Employee.

2. Add class variables

   Add a class variable company_name with the value "Eco Fishing".

   Add a class variable employee_count initialized to 0.

3. Implement the constructor

   Define the __init__ method with the parameters:
   employee_name
   salary
   department
   
   Store these values as instance variables.

   Increment Employee.employee_count each time a new employee object is created.

4. Create an alternative constructor

   Implement a class method named from_monthly_salary.

   Parameters:
   employee_name
   monthly_salary
   department

   Convert the monthly salary to an annual salary by multiplying by 12.

   Convert the result to a string before passing it to the constructor.

   Return a new Employee object using cls(...).

5. Create getter methods

   Implement get_employee_name() to return the employee's name.

   Implement get_salary() to return the employee's salary.

6. Create a setter method

   Implement set_salary(new_salary) to update the employee's salary.

7. Create an information method

   Implement get_info() that returns a formatted string containing:
    Employee name
    Salary
    Department

8. Create a class method

   Implement get_employee_count() that returns the value of employee_count.

9. Create the Manager class

   Define a class named Manager that inherits from Employee.

10. Implement the Manager constructor

    Parameters:
    employee_name
    salary
    department
    managed_team

    Call the parent constructor using super().__init__().

    Store managed_team as an instance variable.

11. Override the get_info() method

    Return a formatted string containing:

      Manager name
      Salary
      Department
      Managed team

12. Create and test objects

    Create an Employee object named john.

    Print John's salary directly and using get_salary().

    Update John's salary using set_salary().

    Print the updated salary.

    Print the employee count using both:
    john.get_employee_count()
    Employee.get_employee_count().

13. Create a dictionary of employees

    Create a dictionary called employees structured like:

    Department -> employment duration -> employee name.

    Iterate through the dictionary using nested loops and print
    the keys and values.

14. Create a Manager object

    Instantiate a Manager named Jane with a managed team list.

15. Print manager and employee information

    Print the result of manager.get_info().
    Print the result of john.get_info().

16. Create an employee using the alternative constructor

    Use Employee.from_monthly_salary() to create an employee named Alice.

    Use a monthly salary of "6000" and department "Marketing".

17. Print Alice's information

    Call alice.get_info() and print the result.
'''