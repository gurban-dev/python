'''
Concepts:
- Truthy/falsy
- Parameters vs. arguments
- Default parameters
- Escape sequences
- String slicing
- Reversing a string

Mini Text Formatter Exercise

Overview:
Write a small program that formats and prints messages based on
several user-defined functions. The assignment integrates
truthy/falsy logic, parameters/arguments, default values, escape
sequences, slicing, and string reversal.

Part 1: Truthy/Falsy Message Validator

Write a function:

def validate_message(msg):
  # Your code here


Requirements:
Return "Valid message" if msg is truthy.

Return "Invalid message" if msg is falsy.

Test it with:

"", " ", "Hello", [], [0], None, 0, -1


Part 2: Parameter Practice: Create a Repeater

Write a function:

def repeat_text(text, times):
  # Your code here


Requirements:
If times is falsy (0, None, "", []), print:

Nothing to repeat.


Otherwise, print text repeated times times.

Extend it to optionally slice the text: if text is longer than 10
characters, only repeat the first 10 characters.


Part 3: Default Parameters + Escape Sequences

Write a function:
def fancy_print(text, prefix=">>> ", suffix=" <<<", new_line=True):
  # Your code here


Requirements:
Use an f-string.

Insert at least two different escape sequences, such as:
\n new line

\t tab

\\ backslash

\' or \"

If new_line is:
True -> print with a newline

False -> print without a newline


Extra Practice:
Use slicing to print only the first 20 characters if the message is too long.

Add an option to print the message reversed (using string slicing).


Example call:
fancy_print("Hello\tWorld!", suffix="!!!", new_line=False)
fancy_print("This is a very long message", prefix="*", suffix="*", new_line=True)


Part 4: Combine Everything

Write a function:
def process_message(msg, repeat=1):
  # Your code here


Requirements:
Call validate_message(msg).

If the message is invalid (falsy), exit the function early.

Otherwise, use repeat_text() to determine how many times to print.

For each repetition, call fancy_print() to print the message.

Include optional arguments for slicing or reversing in fancy_print().


Test calls:
process_message("Hello\n!", repeat=3)
process_message("", repeat=5)
process_message("Hi!", repeat=0)
process_message("Escape test: \\t and \\n", repeat=2)
process_message("A very long message to slice and reverse", repeat=1)
'''