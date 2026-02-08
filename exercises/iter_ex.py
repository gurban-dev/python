"""
Concepts:
Iterators

Objective:
Learn what iterators are, how they work and how to use them
in Python.

Tasks:

1. Define what an iterator is and state the requirements an
   object must satisfy to be considered an iterator.

2. Create iterators from several iterable types, such as:
   - list
   - tuple
   - string
   - range
   - dictionary

3. Take the list from task 2 and have the same iterator start
   from the beginning of the list and then invoke the following
   methods:
   - __iter__()
   - __next__()

   Call these methods directly to observe their behaviour.

4. Use Python's built-in next() function to retrieve values
   from iterators until StopIteration is raised.

5. Demonstrate how a for-loop internally uses iterators.

6. Implement a custom iterator class that generates a sequence
   of numbers.

Expected Learning Outcomes:
- Understand the difference between iterables and iterators.
- Know how to create iterators using iter().
- Retrieve elements using Python's built-in next() function.
- Recognise StopIteration behavior.
- Understand how iteration works internally in Python.
"""