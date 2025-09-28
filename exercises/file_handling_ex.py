'''
Instructions

1. Create a file and write to it
   Ask the user to type in a short note (e.g., “Today was a good day!”).

   Save that note into a file called notes.txt.

2. Read from the file
   Open notes.txt and display its contents to the user.

3. Append a new note
   Ask the user for another note.
   Add this note to the end of the file without erasing the previous one.

4. Read again
   Show the user the updated file with both notes.
'''

# Starter code

# Step 1: Ask the user for their first note
note = input("Write your first note: ")

# TODO: Open "notes.txt" in WRITE mode and save the note


# Step 2: Read the file and display the contents
print("\nHere are your notes so far:")
# TODO: Open "notes.txt" in READ mode and print what's inside


# Step 3: Ask the user for another note
new_note = input("\nWrite another note to add: ")

# TODO: Open "notes.txt" in APPEND mode and add the new note


# Step 4: Read again and show all notes
print("\nUpdated notes:")
# TODO: Open "notes.txt" in READ mode and print the updated contents