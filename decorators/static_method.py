class Math:
  # Methods that are decorated with @staticmethod
  # belong to the class rather than a particular
  # instance of the class.

  # The @staticmethod decorator removes the
  # implicit first self or cls parameter.
  @staticmethod
  def add(num1, num2):
    print('num1 + num2:', num1 + num2)

    return num1 + num2
  
  @staticmethod
  def multiply(num1, num2):
    print('num1 * num2:', num1 * num2)

    return num1 * num2

math = Math()

math.add(10, 10)

math.multiply(10, 10)