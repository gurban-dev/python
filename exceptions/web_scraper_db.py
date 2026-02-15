"""
Web Scraper with Database Integration and Error Handling Demo.

This program scrapes book data from a website and attempts to
insert it into SQLite, demonstrating comprehensive exception
handling throughout the process.
"""

# Library for making HTTP requests.
import requests

# Library for parsing HTML.
from bs4 import BeautifulSoup

# Built-in library for SQLite database operations.
import sqlite3

# Specific database exceptions.
from sqlite3 import IntegrityError, OperationalError, DatabaseError

# For adding delays between requests.
import time

# max_books=5 if a second argument is not given for
# the "max_books" parameter, then 5 will be assigned
# to it.
def scrape_books(url, max_books=5):
  """
  Scrapes book information from a website.

  Args:
    url: The URL to scrape
    max_books: Maximum number of books to scrape
  
  Returns:
    List of dictionaries containing book data
  """

  # Initialise an empty list to store book data.
  books = []

  try:
    # Make an HTTP GET request to the website.
    print(f"Connecting to {url}...")

    # 10 second timeout.
    response = requests.get(url, timeout=10)

    # Check if request was successful (status code 200).
    # Raises HTTPError for bad status codes (4xx, 5xx).
    response.raise_for_status()

    print(f"\nSuccessfully connected! Status code: {response.status_code}")
  
    # Parse the HTML content using BeautifulSoup.

    # For accurately parsing the British pound sterling.
    # Encoding is the process of converting characters (letters
    # symbols) into numbers (bytes) that computers can understand.
    response.encoding = 'utf-8'

    # 'html.parser' is a parsing engine that instructs BeautifulSoup
    # how to parse the HTML.

    # Converts raw HTML string into a structured object.

    # BeautifulSoup is a class defined in the bs4 module.
    soup = BeautifulSoup(response.text, 'html.parser')

    print('\ntype(soup):', type(soup))

    # Find all book containers by obtaining the HTML article elements
    # that have 'product_pod' assigned to their CSS class attribute.

    # BeautifulSoup uses class_ to search by CSS class because
    # you cannot use the class parameter name in Python since
    # "class" a Python keyword.
    book_elements = soup.find_all('article', class_='product_pod', limit=max_books)

    print('\ntype(books_elements):', type(book_elements))

    print(f"\nFound {len(book_elements)} books to scrape.\n")

    # Loop through each book element and extract data.
    # enumerate(iterable, start_index=0)
    for idx, book in enumerate(book_elements, start=1):
      try:
        print('book:', book)

        # Extract title from the 'title' attribute of the <a> tag.
        title = book.h3.a['title']

        # Extract price - remove the '£' symbol.
        price_text = book.find('p', class_='price_color').text

        print('price_text:', price_text)

        # Convert the string to a float.
        price = float(price_text.replace('£', ''))

        print('price:', price)
        
        # Extract availability text.
        availability = book.find('p', class_='instock availability').text.strip()

        # Create dictionary with book data.
        book_data = {
          'title': title,
          'price': price,
          'availability': availability
        }
        
        # Add the dictionary containing book data to the list.
        books.append(book_data)

        # title[:50] slices the first 50 characters (indices 0-49)
        # of the title.
        print(f"{idx}. Scraped: {title[:50]}... (£{price})")
      except AttributeError as e:
        # If we can't find expected HTML elements.
        print(f"Error parsing book {idx}: {e}")

        # Skip this book and move to the next one.
        continue
      except ValueError as e:
        # If price conversion fails.
        print(f"Error converting price for book {idx}: {e}")

        continue
    
      print(f"\nSuccessfully scraped {len(books)} books")

    return books
  except requests.exceptions.ConnectionError:
    # Network connection failed.
    print("Connection Error: Could not connect to the website.")

    print("Check your internet connection or the URL.")

    return []
  except requests.exceptions.Timeout:
    # The request took too long.
    print("Timeout Error: The request took too long.")

    return []
  except requests.exceptions.HTTPError as e:
    # Server returned an error status code.
    print(f"HTTP Error: {e}")

    return []
  except requests.exceptions.RequestException as e:
    # Catch-all for any other requests errors.
    print(f"Request Error: {e}")

    return []


def create_database():
  """
  Creates SQLite database and books table.
  
  Returns:
    Connection object if successful, None otherwise
  """

  # Initialise connection variable.
  conn = None
  
  try:
    # Connect to SQLite database (creates file if doesn't exist).
    print("\nConnecting to database...")
    conn = sqlite3.connect('books.db')
    
    # Create a cursor object to execute SQL commands.
    cursor = conn.cursor()
    
    # Create table with UNIQUE constraint on title.
    # This will cause IntegrityError if we try to insert duplicate titles.
    cursor.execute('''
      CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        price REAL NOT NULL,
        availability TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    ''')
    
    # Commit the transaction (save changes).
    conn.commit()
    
    print("✓ Database and table created successfully")
    return conn
      
  except OperationalError as e:
    # Database file issues, locked database, etc.
    print(f"Database Operational Error: {e}")

    if conn:
      conn.close()
    return None
      
  except DatabaseError as e:
    # Generic database error.
    print(f"Database Error: {e}")

    if conn:
      conn.close()
    return None


def insert_books(conn, books):
  """
  Inserts scraped books into database.
  This function will demonstrate IntegrityError when duplicate
  titles are inserted.
  
  Args:
    conn: Database connection object
    books: List of book dictionaries
  """
  if not conn:
    print("No database connection available")
    return
  
  # Create cursor for executing SQL.
  cursor = conn.cursor()

  # Counter for successful insertions.
  successful = 0

  # Counter for failed insertions.
  failed = 0
  
  print("\nInserting books into database...")

  # Loop through each book and try to insert it into the database table.
  for idx, book in enumerate(books, 1):
    try:
      # SQL INSERT statement with placeholders (?) to prevent SQL injection.
      cursor.execute('''
        INSERT INTO books (title, price, availability)
        VALUES (?, ?, ?)
      ''', (book['title'], book['price'], book['availability']))
      
      # Commit after each insert to save changes.
      conn.commit()
      
      successful += 1

      print(f"  ✓ Inserted: {book['title'][:50]}...")
    except IntegrityError as e:
      # Triggered when UNIQUE constraint is violated (duplicate title).
      failed += 1

      print(f"IntegrityError for '{book['title'][:40]}...': {e}")
      print(f"This book already exists in the database!")
    except OperationalError as e:
      # Database locked, table doesn't exist, etc.
      failed += 1

      print(f"OperationalError: {e}")
    except DatabaseError as e:
      # Generic database error.
      failed += 1

      print(f"DatabaseError: {e}")
    
    # Summary of insertion results.
    print(f"\n{'='*60}")
    print(f"Insertion Summary:")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Total: {len(books)}")
    print(f"{'='*60}")


def display_database_contents(conn):
  """
  Displays all books currently in the database.
  
  Args:
    conn: Database connection object
  """
  if not conn:
    return
  
  try:
    cursor = conn.cursor()
    
    # Select all books from database.
    cursor.execute('SELECT id, title, price, availability FROM books')

    # Fetch all results.
    rows = cursor.fetchall()
    
    if rows:
      print("\n" + "="*60)
      print("Current Database Contents:")
      print("="*60)
      
      # Display each book.
      for row in rows:
        book_id, title, price, availability = row
        print(f"ID: {book_id}")
        print(f"  Title: {title}")
        print(f"  Price: £{price:.2f}")
        print(f"  Availability: {availability}")
        print("-" * 60)
    else:
      print("\nDatabase is empty")   
  except DatabaseError as e:
    print(f"Error reading database: {e}")


def main():
  """
  Main function that orchestrates the entire process.
  """
  print("="*60)
  print("Web Scraper with Database Integration Demo")
  print("="*60)
  
  # URL to scrape (this is a test website for web scraping practice).
  url = 'http://books.toscrape.com/'

  # Step 1: Scrape data from a website.

  # "url" is a positional argument because a parameter
  # name is not explicitly written.

  # max_books=5 is a keyword argument because the name
  # of the parameter "max_books" is included.
  books = scrape_books(url, max_books=2)
  
  # If no books were scraped, exit.
  if not books:
    print("\nNo books scraped. Exiting...")
    return
  
  # Step 2: Create/connect to database.
  # conn = create_database()
  
  # If database connection failed, exit.
  # if not conn:
  #   print("\n✗ Database connection failed. Exiting...")
  #   return
  
  # try:
  #   # Step 3: Insert books (first attempt - should succeed).
  #   insert_books(conn, books)
    
  #   # Step 4: Display what's in the database.
  #   display_database_contents(conn)
    
  #   # Step 5: Try inserting the SAME books again (will trigger IntegrityError!).
  #   print("\n" + "="*60)
  #   print("Now attempting to insert the SAME books again...")
  #   print("This will trigger IntegrityError due to UNIQUE constraint!")
  #   print("="*60)
  
  #   time.sleep(2)
    
  #   # This will fail because titles already exist.
  #   insert_books(conn, books)
    
  #   # Step 6: Display database contents again (should be unchanged).
  #   display_database_contents(conn)
  # except Exception as e:
  #   # Catch any unexpected errors.
  #   print(f"\nUnexpected error: {e}")
      
  # finally:
  #   # Always close database connection (runs no matter what).
  #   if conn:
  #     conn.close()
  #     print("\nDatabase connection closed")
  
  print("\n" + "="*60)
  print("Demo completed!")
  print("="*60)


# This ensures main() only runs when script is executed directly.
if __name__ == '__main__':
  main()