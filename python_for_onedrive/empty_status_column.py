import httpx

def find_letter_value_for_col(df, title):
  # Find the index of the column that
  # contains the header title.
  column_index = None

  print('\ndf.columns:\n', df.columns)

  for index, col in enumerate(df.columns):
    # if col.lower() == 'status':
    if col.lower() == title:
      column_index = index

      # The program exits the
      # for loop.
      break

  if column_index is None:
    return None

  # Convert the column index to the appropriate
  # Excel column letter.
  # 'A' = 65 in ASCII, so 0 -> 'A', 1 -> 'B', etc.
  if column_index < 26:
    # Single letter (A-Z)
    return chr(65 + column_index)
  else:
    # Handle columns beyond 'Z' (AA, AB, etc.)
    first_char = chr(65 + column_index // 26 - 1)
    second_char = chr(65 + column_index % 26)
    return first_char + second_char

def empty_status_column(headers, df):
  # File ID for the Excel workbook
  # in Microsoft OneDrive.
  FILE_ID = '66AF906D87EB4A94!s0f9c5d8f0e534ba4ab12452c17a3a95c'
  SHEET_NAME = 'Sheet1'

  column_letter = find_letter_value_for_col(df, 'status')

  print('\nlen(df):', len(df))

  range_address = f'{column_letter}2:{column_letter}{len(df) + 1}'

  print('\nrange_address:', range_address)

  # Construct the URL to update the column with
  # empty strings.
  url = (
    f"https://graph.microsoft.com/v1.0/me/drive/items/{FILE_ID}/"
    f"workbook/worksheets/{SHEET_NAME}/"
    f"range(address='{range_address}')"
  )

  data = {
    # Empty string for each row in the column.
    "values": [[''] for _ in range(len(df))]
  }

  # Send the PATCH request to update the column values.
  # Remember that PATCH is a partial update.
  response = httpx.patch(url, headers=headers, json=data)

  if response.status_code == 200:
    print(f"\nSuccessfully cleared all values "
          f"in the \"status\" column.")
  else:
    print(f"\nError clearing column values:"
          f"{response.status_code} - {response.text}")