# Store each book title and the number of times it is borrowed.
books = {}

# Keep reading input until the user exits the program.

# Non-entry controlled while loop since the condition is hardcoded to
# be True.
while True:
    try:
        # .strip() removes the leading and trailing whitespace
        # characters.
        # .lower() makes all character lowercase

        # This ensures that every title is stored in the same format.
        title = input("Book title: ").strip().lower()

        # Stop the loop if the user wants to quit.
        if title == "quit":
            break

        # Increase the count if the title already exists.
        elif title in books:
            books[title] += 1

        # Otherwise, add the title to the dictionary with a count of one.
        else:
            books[title] = 1

    # Exit the loop when an EOFError is raised.
    # EOF means "End Of File", indicating that the user has
    # finished entering input.

    # This also catches Ctrl+D safely.
    except EOFError:
        break

print()

# Print the books in alphabetical order.
for title in sorted(books):
    print(f"{books[title]} {title.title()}")