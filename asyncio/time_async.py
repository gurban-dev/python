import asyncio

async def count():
  print("One")

  await asyncio.sleep(1)

  print("Two")

  await asyncio.sleep(1)

async def main():
  await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
  import time

  start = time.perf_counter()

  asyncio.run(main())

  elapsed = time.perf_counter() - start

  # Compare how long this asynchronous program takes with the
  # synchronous one.
  print(f"{__file__} executed in {elapsed:0.2f} seconds.")