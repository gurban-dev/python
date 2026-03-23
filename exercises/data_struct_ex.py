'''
Exercise: Student Course Tracker

Python Concepts Reinforced:
Tuples
- Ordered collections
- Immutability (cannot modify elements)

Lists
- Ordered and mutable collections
- Adding and removing elements (append, remove)
- Index-based access (not key-based)

Dictionaries
- Key-value data modeling
- Iteration using .items()
- Accessing values by key
- Updating and extending dictionaries

Sets
- Unordered collections of unique elements
- No indexing or .append()
- Set operations: equality, difference

for Loops
- Iterating over lists and dictionaries
- Unpacking key-value pairs in loops

Type Errors & Illegal Operations
- Understanding common Python exceptions (TypeError, AttributeError)
- Recognising which operations are valid for each data structure

Goal:
Practice Python data structures and iteration, and learn what operations
are illegal.


Starter Code:

# A tuple of course names (should not change)
courses = ("Python", "SQL", "Statistics", "Business Analytics")

# A list of students
students = ["Sara", "Alex", "Jamal", "Priya"]

# A dictionary mapping students to the courses they completed.
completed_courses = {
	"Sara": {"Python", "SQL"},
	"Alex": {"Python"},
	"Jamal": {"SQL", "Statistics"},
	"Priya": {"Python", "SQL", "Statistics"}
}


Task 1 — Tuples

Print the first and last course in the courses tuple.

Try to add "Machine Learning" to the tuple.

Observe what happens and write a comment explaining why.

Learning outcome:
Tuples are ordered and immutable.


Task 2 — Lists

Add a new student "Lina" to the students list.

Remove "Alex" from the list.

Print the updated list.

Learning outcome:
Lists are mutable and support insert/remove operations.


Task 3 — Dictionaries + for-loop

Use a for loop to print each student and the courses they completed.

Expected output format:

Sara has completed: Python, SQL
Alex has completed: Python


(Order doesn't matter.)

Inside the loop:

Print how many courses each student completed.

Learning outcome:
Iterating over key-value pairs with .items().


Task 4 — Sets

For each student, check if they have completed all courses.

Print:
"Priya has completed all courses"

or "Sara is missing some courses"

Hint: Compare two sets.

Learning outcome:
Sets support comparison, subset, and difference operations.


Task 5 — Illegal Operations (Critical Learning Moment)

Ask students to try these operations, one at a time:

courses[0] = "Java"

completed_courses["Sara"][0]

completed_courses["Alex"].append("SQL")

students["Sara"] = "Advanced"


Questions to answer:
Which lines raise errors?

What type of error is it?

Why is it illegal?
'''