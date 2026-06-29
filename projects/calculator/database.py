# Import Python's built-in SQLite library.
# This allows the program to create and interact with databases.
import sqlite3

# A class is called a blueprint because it defines what a single entity
# should have:
# 1. Data (attributes), which describe the entity's state.
# 2. Actions (methods), which allow the entity to interact with or modify
#    that state.

# This single entity is called an object.

# Imagine you're designing a blueprint for a bank account object.

# Every bank account should have some data:
# • Name of the owner
# • Balance

# And every bank account should be able to perform certain actions:
# • Deposit Money
# • Withdraw Money

# This blueprint says:
# Every bank account object should store an owner's name and a balance.

# Manage the application's database connection and tables.
class Database:

    # The constructor method (__init__()) initialises the state of
    # a new Database object.

    # Type annotations provide hints about the expected data types.
    # • db_name: str means db_name should be a string.
    # • -> None means this method does not return a value.

    # = "calculator.db" provides the db_name parameter with a default
    # value if no argument is passed.

    # db_name is the name of the SQLite database file.
    # If the file does not exist, SQLite will create it.
    def __init__(self, db_name: str = "calculator.db") -> None:

        # Open a connection to the database.

        # Think of this as opening a communication channel
        # between our Python program and the database.
        self.connection = sqlite3.connect(db_name)

        # Ensure all required database tables exist.
        self.create_tables()

    # Create any database tables needed by the application.
    def create_tables(self) -> None:

        # Create a cursor object.

        # A cursor is used to send SQL commands to the database.
        cursor = self.connection.cursor()

        # Execute a SQL command.

        # This command creates a table named calculations
        # if it does not already exist.
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS calculations (

                -- A unique identifier for each calculation.
                --
                -- AUTOINCREMENT means SQLite automatically
                -- assigns the next available number.
                id INTEGER PRIMARY KEY AUTOINCREMENT,

                -- Store the first number entered by the user.
                first_number REAL,

                -- Store the operator such as +, -, *, or /.
                operator TEXT,

                -- Store the second number entered by the user.
                second_number REAL,

                -- Store the result of the calculation.
                result REAL,

                -- Store when the calculation was created.
                --
                -- CURRENT_TIMESTAMP automatically records
                -- the current date and time.
                created_at TIMESTAMP
                    DEFAULT CURRENT_TIMESTAMP
            )
            """
        )

        # Save the changes to the database.

        # Without commit(), the table creation may not be
        # permanently written to the database file.
        self.connection.commit()