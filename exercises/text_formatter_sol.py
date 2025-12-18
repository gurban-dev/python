# Mini Text Formatter Solution

# ------------------------------
# Part 1: Truthy/Falsy Validator
# ------------------------------
def validate_message(msg):
  if msg:
    return "Valid message"
  else:
    return "Invalid message"


# -----------------------------
# Part 2: Repeater with slicing
# -----------------------------
def repeat_text(text, times):
  if not times:
    print("Nothing to repeat.")
    return

  # Slice text if longer than 10 characters
  sliced_text = text[:10] if len(text) > 10 else text

  for _ in range(times):
    print(sliced_text)


# ------------------------------------------------------------
# Part 3: Fancy Print with default params and escape sequences
# ------------------------------------------------------------
def fancy_print(
  text, prefix=">>> ", suffix=" <<<", new_line=True,
  reverse=False, max_length=None
):
  # Optional reversal
  if reverse:
    text = text[::-1]

  # Optional slicing
  if max_length:
    text = text[:max_length]

  # Prepare formatted string with escape sequences
  message = f"{prefix}{text}{suffix}\n\t(printed with escape sequences!)"
  if new_line:
    print(message)
  else:
    print(message, end='')


# --------------------------
# Part 4: Combine Everything
# --------------------------
def process_message(msg, repeat=1, reverse=False, max_length=None):
  validation_result = validate_message(msg)

  print(f"[Validator] {validation_result}")
  
  if validation_result == "Invalid message":
    # Exit early if message is falsy
    return

  # Determine repetitions
  if not repeat:
    print("Nothing to repeat.")
    return
  
  # Repeat and print with fancy formatting
  for _ in range(repeat):
    fancy_print(msg, reverse=reverse, max_length=max_length)


# ---------------------------
# Test Calls
# ---------------------------
print("=== Part 1 Tests ===")

test_msgs = ["", " ", "Hello", [], [0], None, 0, -1]

for m in test_msgs:
  print(f"Message: {repr(m)} -> {validate_message(m)}")

print("\n=== Part 2 Tests ===")
repeat_text("HelloWorldPython", 3)
repeat_text("Short", 0)
repeat_text("123456789012345", 2)

print("\n=== Part 3 Tests ===")
fancy_print("Hello\tWorld!", suffix="!!!", new_line=False)

# For clarity in output
print()

fancy_print(
  "This is a very long message", prefix="*", suffix="*",
  new_line=True, max_length=20)

fancy_print("Reverse me!", reverse=True)

print("\n=== Part 4 Tests ===")
process_message("Hello\n!", repeat=3)

process_message("", repeat=5)

process_message("Hi!", repeat=0)

process_message("Escape test: \\t and \\n", repeat=2)

process_message(
  "A very long message to slice and reverse",
  repeat=1,
  reverse=True,
  max_length=15
)