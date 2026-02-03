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

class Notification:
  def send(self, message):
    raise NotImplementedError("Subclasses must implement send()")


class EmailNotification(Notification):
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"Email sent: {message}")


class SMSNotification(Notification):
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"SMS sent: {message}")


# ----------------------------------------------------------------
# TASK 1
# Identify the polymorphic interface
#
# ANSWER:
# The polymorphic interface is the send(self, message) method.
# It is important because all notification types expose the same
# method name and signature, allowing objects of different classes
# to be used interchangeably at runtime.
# ----------------------------------------------------------------


# ----------------------------------------------------------------
# TASK 2
# Write a polymorphic function
# ----------------------------------------------------------------

def notify_all(notifications, message):
  """
  Sends a message using any object that provides a send() method.
  This relies on polymorphism rather than type checking.
  """
  for notification in notifications:
    notification.send(message)


# ----------------------------------------------------------------
# TASK 3
# Add a new subclass WITHOUT modifying notify_all()
# ----------------------------------------------------------------

class PushNotification(Notification):
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"Push notification sent: {message}")


# ----------------------------------------------------------------
# TASK 5
# Break polymorphism on purpose (duck typing)
# ----------------------------------------------------------------

class SlackNotification:
  def send(self, message):
    print(f"{self.__class__.__name__} handling message")
    print(f"Slack message: {message}")


# ----------------------------------------------------------------
# Program Execution
# ----------------------------------------------------------------

if __name__ == "__main__":
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