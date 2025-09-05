import turtle
import time

# Setup turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor("black")
t.speed(0)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]

# For loop goes through each color
for colour in colours:
  print('colour:', colour)

  # colour is a string variable.
  t.color(colour)

  # Integer variable
  t.forward(100)

  # Integer variable
  t.right(60)

time.sleep(30)

dishes = ['spaghetti', 'salami pizza', 'lamb chops']

for dish in dishes:
  print(dish)

destinations = ['Athens', 'Istanbul', 'Tunis']