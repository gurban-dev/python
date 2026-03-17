import time

def count():
  print("One")

  time.sleep(1)

  print("Two")

  time.sleep(1)

def main():
  # Run sequentially, not concurrently.
  count()
  count()
  count()

if __name__ == "__main__":
  start = time.perf_counter()

  main()

  elapsed = time.perf_counter() - start

  # Compare how long this synchronous program takes with the
  # asynchronous one.
  print(f"{__file__} executed in {elapsed:0.2f} seconds.")