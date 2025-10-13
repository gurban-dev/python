# create a sample file
with open("notes.txt", "w") as f:
  f.write("First line\nSecond line\nThird line")

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