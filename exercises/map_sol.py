def safe_to_float(entry: str) -> float | None:
	"""Attempt to convert a string to a float. Return None if invalid."""
	try:
		return float(entry)
	except ValueError:
		return None
  
user_input: str = "3.1 abc 7.0 -2.5 cat 9"

# Return a list made up of the substrings declared in user_input.
entries: list[str] = user_input.split()

# Apply safe conversion to each part.
converted: list[float | None] = list(map(safe_to_float, entries))

# Separate valid and invalid values.
valid_numbers: list[float] = [entry for entry in converted if entry is not None]

no_of_invalid_entries: int = converted.count(None)

print('Valid_numbers:', valid_numbers)

print('\nNumber of invalid entries:', no_of_invalid_entries)