employees = {
  101: {"name": "Alexander", "years_at_company": 2},
  102: {"name": "Maria", "years_at_company": 5},
  103: {"name": "John", "years_at_company": 1}
}

# -Get the first employee's record.
# The following line returns:
# {"name": "Alexander", "years_at_company": 2}
first_employee = employees[101]

# Extract the keys of the first inner dictionary.
all_keys_in_first_record = list(first_employee.keys())

print('all_keys_in_first_record:', all_keys_in_first_record)

# Get the first key which is "name".
first_key = all_keys_in_first_record[0]

print("First key of the first inner dictionary:", first_key)