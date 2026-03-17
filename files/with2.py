def print_file_content(file_name: str) -> int:
  line_count = 0

  with open(file_name) as file_object:
    for line in file_object:
      print(line)
      # print(line.strip())

      line_count += 1

    return line_count

line_count = print_file_content('philosophers.txt')

print('\nline_count:', line_count)