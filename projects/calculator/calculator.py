# Import the arithmetic functions from the operations module.
from operations import (
    add,
    subtract,
    multiply,
    divide,
)


# Represent a calculator capable of performing registered operations.
class Calculator:

    # Initialize the calculator and register the default operations.
    def __init__(self):

        # Store operator symbols as keys and their corresponding functions
        # as values.
        self._operations = {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide,
        }

    # Perform the requested calculation using the specified operator.
    def calculate(
        self,
        operator,
        first_number,
        second_number,
    ):

        # Verify that the requested operator has been registered.
        if operator not in self._operations:

            # Raise an error if the operator is not supported.
            raise ValueError(
                f"Unsupported operator: {operator}"
            )

        # Retrieve the function associated with the operator.
        operation = self._operations[operator]

        # Execute the selected operation and return the result.
        return operation(
            first_number,
            second_number,
        )

    # Register a new operation with the calculator.
    def register_operation(
        self,
        operator,
        operation,
    ):

        # Prevent existing operators from being overwritten.
        if operator in self._operations:

            # Raise an error if the operator already exists.
            raise ValueError(
                f"Operator '{operator}' already exists."
            )

        # Associate the operator symbol with its function.
        self._operations[operator] = operation

    # Return a list of all registered operator symbols.
    def available_operations(self):

        # Return the dictionary keys as a list.
        return list(
            self._operations.keys()
        )