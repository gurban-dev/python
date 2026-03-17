numerator = 10
denominator = 0

# The source code that is inside of the try block is
# referred to as "protected code" because if it raises
# an exception, the exception will be caught rather than
# stopping the execution of the Python program.

# For source code to be associated with a try block, it must
# be indented.
try:
    # Line 17 raises a ZeroDivisionError exception because
    # like in mathematics, dividing by zero results in an
    # undefined calculation.

    # One / (forward slash) indicates float division.
    calculation = numerator / denominator

    # Syntactically, source code must be included in this
    # try block so 'pass' acts as a placeholder for when
    # no action needs to be taken.
    pass

    # Two // (forward slashes) indicates integer division.
    # calculation = numerator // denominator
except ZeroDivisionError as err:
    print("A number cannot be divided by 0:", err)
except KeyboardInterrupt as err:
    print("Error:", err)

# Comment out line 17 and uncomment the subsequent line to
# see the difference.

# Will line 35 be executed this time?
calculation = numerator / denominator

print("\nProgram continued!")