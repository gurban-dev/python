# Indexes:        0           1         2         3          4
countries = ['Australia', 'Canada', 'Germany', 'Japan', 'Australia']

# Global variable (accessible anywhere in this file)
indexes_for_australia = []

# Function demonstrating local scope.
def get_indexes_for_australia(countries):

    # Local variable (only exists inside this function)
    indexes_for_australia = []

    """
    Python resolves variable names in the following order (LEGB rule):

    1. Local      - inside the current function
    2. Enclosing  - outer function if nested
    3. Global     - defined at the module level
    4. Built-in   - Python's built-in names (print, len, etc.)
    """

    # enumerate() returns both the index and value.
    for index, value in enumerate(countries):
        print(f"index: {index}, value: {value}")

        if value == 'Australia':
            indexes_for_australia.append(index)

    return indexes_for_australia


print("\nAustralia indexes:", get_indexes_for_australia(countries))


# -----------------------------
# Demonstrating that for loops
# do not create their own scope
# -----------------------------

# Initialise before the loop.
indexes_for_canada = []

for index, value in enumerate(countries):

    print(f"index: {index}, value: {value}")

    if value == 'Canada':
        indexes_for_canada.append(index)

print("\nindexes_for_canada:", indexes_for_canada)

# Variables defined in the loop are still accessible afterwards.
print("\nLast index:", index)
print("Last value:", value)


# ------------------------------
# Demonstrating that while loops
# also do not create scope
# ------------------------------

nums = [1, 2, 3, 4]
index = 0

while index < len(nums):

    if nums[index] == 4:
        found_value = nums[index]

    index += 1

# 'found_value' is accessible outside the loop.
print("\nfound_value:", found_value)