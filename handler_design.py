# Design 1

# Each language-specific function only knows how to produce
# the language-specific greeting word.
def greet_in_french() -> str:
    return "Bonjour"


def greet_in_spanish() -> str:
    return "Hola"


greeting_handlers = {
    "french": greet_in_french,
    "spanish": greet_in_spanish,
}


def greet_in_language(first_name: str, language: str) -> str:
    handler = greeting_handlers[language]

    # The generic function is responsible for knowing how
    # to construct the final greeting.
    return f"{handler()} {first_name}!"


# Design 2

# Each language-specific function is responsible for
# constructing the complete greeting.
def greet_in_french(first_name: str) -> str:
    return f"Bonjour {first_name}!"


def greet_in_spanish(first_name: str) -> str:
    return f"Hola {first_name}!"


greeting_handlers = {
    "french": greet_in_french,
    "spanish": greet_in_spanish,
}


def greet_in_language(first_name: str, language: str) -> str:
    handler = greeting_handlers[language]

    # The generic function does not need to know how the
    # greeting is constructed. It only selects the handler
    # and gives it the information it needs.
    return handler(first_name)

# KEY DESIGN DIFFERENCE

# Design 1:

# greet_in_language() knows both:
# 1. Which function to call.
# 2. How to construct the final greeting.

# This means the generic function contains knowledge about
# the details of the greeting.


# Design 2:

# greet_in_language() only knows:
# 1. Which function to call.
# 2. What information to give that function.

# The language-specific function owns the responsibility of
# constructing the greeting.

# This is the main reason Design 2 is cleaner:

# Each function has a clear, focused responsibility. The
# language-specific function handles how the greeting is
# created, while greet_in_language() only handles selecting
# and calling the appropriate function.

print(greet_in_language("John", "french"))
print(greet_in_language("John", "spanish"))