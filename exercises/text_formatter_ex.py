'''
Concepts:
- Truthy/falsy
- Parameters vs. arguments
- Default parameters
- Escape sequences


Build a Mini Text Formatter

Overview:
Write a small program that formats and prints messages based
on several user-defined functions. The assignment integrates
truthy/falsy logic, parameters/arguments, default values, and
escape sequences.

Part 1: Truthy/Falsy Message Validator

Write a function:
def validate_message(msg):


Requirements:

The function should:
- Return "Valid message" if msg is truthy.
- Return "Invalid message" if msg is falsy.
- Test it with:
""

" "

"Hello"

[]

[0]

None

0

-1


Part 2: Parameter Practice: Create a Repeater

Write a function:
def repeat_text(text, times):


Requirements:
If times is falsy (e.g., 0, None, "", []), the function
should not repeat the text.

Instead, print:
"Nothing to repeat."

Otherwise, print text repeated times times.

Part 3: Default Parameters + Escape Sequences

Create a function:
def fancy_print(text, prefix=">>> ", suffix=" <<<", new_line=True):


Requirements:
Use an f-string.

Insert at least two different escape sequences, such as:
\n new line

\t tab

\\ backslash

\' or \"

If new_line is:

True -> print the message with a newline at the end

False -> print the message without an automatic newline


Example call:
fancy_print("Hello\tWorld!", suffix="!!!", new_line=False)

Part 4: Combine Everything

Write a function:
def process_message(msg, repeat=1):


Requirements:
First call validate_message(msg).

If the message is invalid (falsy), exit the function early.

Otherwise:
Use repeat_text() to determine how many times to print.

For each repetition, call fancy_print() to actually print the message.

Test calls:
process_message("Hello\n!", repeat=3)
process_message("", repeat=5)
process_message("Hi!", repeat=0)
process_message("Escape test: \\t and \\n", repeat=2)
'''