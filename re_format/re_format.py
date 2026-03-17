import os

def add_whitespace_to_html_comment(line):
  if '<!--' in line:
    line = line.replace('<!--', '<!-- ')

  if '-->' in line:
    line = line.replace('-->', ' -->')

  return line

def deindent_line(line):
  if len(line) >= 2 and line[:2].isspace():
    return line[2:]
  else:
    return line

def process_file(file_path):
  # Obtain all of the lines from the file.
  with open(file_path, 'r') as file:
    lines = file.readlines()

  with open(file_path, 'w') as file:
    for line in lines:
      # Append a whitespace character after "<!--"
      # and before "-->".
      line = add_whitespace_to_html_comment(line)

      # De-indent each line by removing the two
      # leading whitespace characters.
      line = deindent_line(line)

      file.write(line)

def process_folder(folder_path):
  # Process all files in a folder to de-indent them.
  print(f'os.listdir({folder_path}): {os.listdir(folder_path)}')

  for root, dirs, files in os.walk(folder_path):
    print('files:', files)
    for file in files:
      file_path = os.path.join(root, file)

      print('file_path:', file_path)

      if file.endswith('.py') or file.endswith('.txt'):
        print(f"Processing file: {file_path}")
        process_file(file_path)

if __name__ == "__main__":
  # folder_path = input("Enter the folder path: ")

  # file_path = input("Enter the file path: ")

  # process_folder(folder_path)

  file_path = './sample.txt'

  process_file(file_path)

  print("Re-formatting process completed.")