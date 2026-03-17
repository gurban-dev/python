# This script reads a server log file line by line,
# extracts the status ("SUCCESS" or "FAIL"),
# counts occurrences of each, and prints a summary.

# Dictionary to store the count of each status type
status_count = {}

# Open the log file safely using a context manager
with open("server.log", "r") as f:
  # Read each line in the file
  for line in f:
    # Remove any extra spaces or newline characters
    line = line.strip()

    # Each line has format: "2025-10-01 12:01:01 - SUCCESS"
    # Split on " - " and take the last part as the status
    parts = line.split(" - ")
    if len(parts) == 2:
      status = parts[1]

      # Count each status type
      if status in status_count:
        status_count[status] += 1
      else:
        status_count[status] = 1

# Print a summary report
print("Server Log Summary:")
for status, count in status_count.items():
  print(f"{status}: {count}")