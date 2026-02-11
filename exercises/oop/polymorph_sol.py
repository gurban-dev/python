"""
Exercise: Polymorphism in Python

You are building a notification system that can send messages in
different ways (email, SMS, push, etc.).

Each notification type sends messages differently, but the rest of
your program should be able to send a message without knowing or
caring which type it is.
"""

# ----------------------------------------------------------------
# Starter Code
# ----------------------------------------------------------------

# This base class defines the shared interface so all notifications
# expose the same send() method and can be used interchangeably.
class Notification:
  def send(self, message):
    raise NotImplementedError("Subclasses must implement send()")


class EmailNotification(Notification):
  def send(self, message):
    # Using the class name dynamically helps demonstrate runtime
    # method resolution by showing which implementation is called.
    print(f"{self.__class__.__name__} handling message")

    print(f"Email sent: {message}")


# This class provides a different implementation of the same method,
# reinforcing that objects with a common interface can behave differently.
class SMSNotification(Notification):
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"SMS sent: {message}")


# ----------------------------------------------------------------
# TASK 1
# Identify the polymorphic interface
#
# Answer:
# The polymorphic interface is the send(self, message) method.
# It is important because all notification types expose the same
# method name and signature, allowing objects of different classes
# to be used interchangeably at runtime.
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 2
# Write a polymorphic function
# ----------------------------------------------------------------

# This function relies on behaviour instead of type checking, allowing
# any object with a send() method to work without modification.
def notify_all(notifications, message):
  """
  Sends a message using any object that provides a send() method.
  This relies on polymorphism rather than type checking.
  """

  # Iterating through objects and calling the same method name allows
  # Python to decide at runtime which implementation to execute.
  for notification in notifications:
    notification.send(message)


# ----------------------------------------------------------------
# TASK 3
# Add a new subclass WITHOUT modifying notify_all()
# ----------------------------------------------------------------

# Adding a new subclass proves that extending functionality does not
# require changes to existing polymorphic code when interfaces match.
class PushNotification(Notification):
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"Push notification sent: {message}")


# ----------------------------------------------------------------
# TASK 5
# Break polymorphism on purpose (duck typing)
# ----------------------------------------------------------------

# This class does not inherit from Notification but still works because
# Python uses duck typing: if an object has the required method, it is valid.

# Duck typing is a concept in Python where an object's suitability is
# determined by what it can do (its methods/behavior), not by its class
# or inheritance.
class SlackNotification:
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"Slack message: {message}")


# ----------------------------------------------------------------
# Program Execution
# ----------------------------------------------------------------

if __name__ == "__main__":
  # Creating a mixed list of objects demonstrates that the same function
  # can operate on different classes without caring about their types.
  notifications = [
    EmailNotification(),
    SMSNotification(),
    PushNotification(),
    SlackNotification()
  ]

  notify_all(notifications, "Your order has shipped!")


# ----------------------------------------------------------------
# FINAL REFLECTION
#
# Polymorphism is the ability to treat different objects the same
# way as long as they share a common interface.
#
# This exercise demonstrated polymorphism by allowing a single
# function to call the same method on different objects and get
# different behavior at runtime.
# ----------------------------------------------------------------