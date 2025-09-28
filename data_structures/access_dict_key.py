employees = {
  101: {"name": "Alexander", "years_at_company": 2},
  102: {"name": "Maria", "years_at_company": 5},
  103: {"name": "John", "years_at_company": 1}
}

# Get the first employee's record.
first_employee = employees[101]

# Extract the first key of the inner dictionary
first_key_list = list(first_employee.keys())
first_key = first_key_list[0]

print("First key inside an employee record:", first_key)