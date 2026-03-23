"""
Exercise: Polymorphism in Python

You are building a notification system that can send messages in
different ways (email, SMS, push, etc.).

Each notification type sends messages differently, but the rest of
your program should be able to send a message without knowing or
caring which type it is.
"""

# ------------------------------------------------------
# Starter Code
# ------------------------------------------------------

class Notification:
	def send(self, message):
		raise NotImplementedError("Subclasses must implement send()")


class EmailNotification(Notification):
	def send(self, message):
		print("EmailNotification handling message")
		print(f"Email sent: {message}")


class SMSNotification(Notification):
	def send(self, message):
		print("SMSNotification handling message")
		print(f"SMS sent: {message}")


# ------------------------------------------------------
# TASK 1
# Identify the polymorphic interface
#
# TODO:
# Write a comment explaining which method enables
# polymorphism and why that method is important.
# ------------------------------------------------------


# ------------------------------------------------------
# TASK 2
# Write a polymorphic function
#
# TODO:
# Implement notify_all so that it sends the message
# using ANY notification object in the list.
#
# Constraints:
# - Do NOT use isinstance()
# - Do NOT use type()
# - Do NOT use if/elif statements
# ------------------------------------------------------

def notify_all(notifications, message):
	# TODO: Implement this function
	pass


# ------------------------------------------------------
# TASK 3
# Add a new subclass WITHOUT modifying notify_all()
#
# TODO:
# Create a PushNotification class that sends a message.
# ------------------------------------------------------

class PushNotification(Notification):
	# TODO: Implement send()
	pass


# ------------------------------------------------------
# TASK 4
# Demonstrate runtime method resolution
#
# TODO:
# Ensure each send() method prints its class name
# before sending the message.
#
# Run the program and observe how the SAME function call
# results in DIFFERENT behaviour at runtime.
# ------------------------------------------------------


# ------------------------------------------------------
# TASK 5
# Break polymorphism on purpose (duck typing)
#
# TODO:
# Create a class that does NOT inherit from Notification
# but still works with notify_all().
#
# After running, answer:
# Why does this work even without inheritance?
# ------------------------------------------------------

class SlackNotification:
	def send(self, message):
		print("SlackNotification handling message")
		print(f"Slack message: {message}")

if __name__ == "__main__":
	notifications = [
		EmailNotification(),
		SMSNotification(),
		# TODO: Add PushNotification here
		SlackNotification()
	]

	notify_all(notifications, "Your order has shipped!")


# ---------------------------------------------------------------
# FINAL REFLECTION
#
# In 1-2 sentences:
# What is polymorphism, and how did this exercise demonstrate it?
# ---------------------------------------------------------------