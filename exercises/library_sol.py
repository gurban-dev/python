# Store each book title and the number of times it is borrowed.
books = {}

# Keep reading input until the user exits the program.
while True:
    try:
        # Remove extra spaces and convert the title to lowercase so
        # every title is stored in the same format.
        title = input("Book title: ").strip().lower()

        # Stop the loop if the user wants to quit.
        if title == "quit":
            break

        # Increase the count if the title already exists.
        if title in books:
            books[title] += 1

        # Otherwise, add the title to the dictionary with a count of one.
        else:
            books[title] = 1

    # Exit the loop when an EOFError is raised.
    # EOF means "End Of File", indicating that the user has finished entering input.
    except EOFError:
        break

print()

# Print the books in alphabetical order.
for title in sorted(books):
    print(f"{books[title]} {title.title()}")