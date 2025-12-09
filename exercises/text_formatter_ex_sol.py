def validate_message(msg):
  if msg:
    return "Valid message"
  return "Invalid message"

print("Part 1 TESTS:")
test_values = ["", " ", "Hello", [], [0], None, 0, -1]

for v in test_values:
  print(f"validate_message({repr(v)}):", validate_message(v))

print("\n")


def repeat_text(text, times):
  # times is falsy (0, None, "", [], etc.)
  if not times:
    print("Nothing to repeat.")
    return

  for _ in range(times):
    print(text)

print("Part 2 TESTS:")
repeat_text("Test", 3)
repeat_text("Test", 0)
repeat_text("Test", None)
print("\n")

def fancy_print(text, prefix=">>> ", suffix=" <<<", new_line=True):
  # Include escape sequences: \n and \t
  formatted = f"{prefix}\t{text}\n{suffix}"

  if new_line:
    print(formatted)
  else:
    # Suppress automatic newline
    print(formatted, end="")

print("TESTS:")
fancy_print("Hello\tWorld!", suffix="!!!", new_line=False)
print("\n")

def process_message(msg, repeat=1):
  validation_result = validate_message(msg)

  if validation_result == "Invalid message":
    print("Message rejected: it is falsy.")
    return

  if not repeat:
    print("Cannot process: repeat count is falsy.")
    return

  for _ in range(repeat):
    fancy_print(msg)

print("TESTS:")
process_message("Hello\n!", repeat=3)
process_message("", repeat=5)
process_message("Hi!", repeat=0)
process_message("Escape test: \\t and \\n", repeat=2)

print("\nAll tests complete.")