errors = 3

if errors > 0:
  # F-string format:
  # f"sequence_of_text {variable} sequence_of_text."
  # f'sequence_of_text {variable} sequence_of_text.'
  print(f'You have {errors} errors to fix.')
else:
  print('You have no errors to fix.')