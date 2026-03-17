import pandas as pd
import csv
from datetime import datetime


class CSV:
  # Class variable.
  # It's associated with this class as opposed
  # to an instance of this class.
  CSV_FILE = 'finance_data.csv'

  COLUMNS = ["date", "amount", "category", "description"]

  # The @classmethod decorate gives the following
  # method access to this class itself, but not to
  # an instance of this class.
  @classmethod
  def initialise_csv(cls):
    # Attempt to read in the CSV file.
    try:
      pd.read_csv(cls.CSV_FILE)
    except FileNotFoundError:
      # Specify the four columns that the CSV file should
      # consist of.
      df = pd.DataFrame(columns=cls.COLUMNS)

      # Export the Pandas Dataframe to the CSV file.
      # The keyword argument index=False means that the
      # DataFrame will not be sorted by indexing.
      df.to_csv(cls.CSV_FILE, index=False)

      # The CSV file will have the name that is assigned to
      # the class variable and will be generated in the same
      # directory as this Python program.

  @classmethod
  def add_entry(cls, date, amount, category, description):
    # A Python dictionary containing all of the data that
    # will be added into the CSV file.
    # An example of a data structure.
    new_entry = {
      "date": date,
      "amount": amount,
      "category": category,
      "description": description
    }

    '''
    A with statement is an example of a Python context manager.

    In the with statement, the open() function returns a file
    object that acts as a context manager. When the with block
    is entered, the file is opened. When the with block is
    exited (either normally or due to an exception), the __exit__
    method of the file object is automatically called, ensuring
    that the file is closed, thereby releasing the resource.
    '''

    # Argument "a" makes it clear that the CSV file should be
    # opened in append mode.

    # Whenever you see a with statement in Python, you can deduce
    # that you are looking at a context manager.

    # The open() function returns a file object that is itself a
    # context manager.

    # The file object satisfies the context manager protocol
    # (__enter__, __exit__) because when the program enters the
    # with block, the file object's __enter__() method is called
    # and after exiting the with block, the file object's __exit__()
    # method is called, which closes the file.

    # The advantage of using a context manager is that there is zero
    # possibility for memory leaks.

    # A memory leak occurs when a program retains references to memory
    # that is no longer needed, preventing the operating system (or
    # the Python garbage collector) from reclaiming it.
    with open(cls.CSV_FILE, "a", newline="") as csv_file:
      # The DictWriter() class takes a dictionary and writes
      # it to a CSV file.
      writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)

      # Write a new row in the CSV file.
      writer.writerow(new_entry)

    print('Entry added successfully.')



# Test the initialise_csv() method.
# Watch what transpires in the directory where this program
# is located.
CSV.initialise_csv()