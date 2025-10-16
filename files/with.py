# Create a sample file
with open("notes.txt", "w") as f:
  f.write("First line\nSecond line\nThird line")

'''
The open() function in Python, when used with the with
statement, acts as a context manager.

When the with block is entered, the __enter__ method of
the file object returned by open() is called, opening
the file.

The as f part assigns the opened file object to the
variable f.

When the with block is exited (either normally or due
to an exception), the __exit__ method of the file object
is automatically called, ensuring that the file is
properly closed, releasing the resource.
'''

# read the file
with open("notes.txt", "r") as f:
  contents = f.read()

print(contents)

new_lines = ["Fourth line", "Fifth line"]

# Opening the file to append new data.
with open("notes.txt", "a") as f:
  for line in new_lines:
    f.write(line + "\n")

with open("notes.txt", "r") as f:
  # Reading the file line by line.
  for line in f:
    print(line.strip())

# with open(...) automatically closes the file when done.

# "r" = read mode, "w" = write mode (overwrites file), "a" = append mode.