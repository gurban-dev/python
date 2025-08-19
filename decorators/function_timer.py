import time

def timer(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()

    return_value = func(*args, **kwargs)

    total_time = time.time() - start_time

    print('total_time:', total_time)

    return return_value
  return wrapper

# @timer is being used to decorate function test1().
@timer
def test1():
  for _ in range(100000):
    pass

@timer
def test2():
  time.sleep(2)

test1()

test2()