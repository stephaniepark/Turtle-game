import turtle
import random

# 1. Setup the game window
screen = turtle.Screen()
screen.title("Coin Collector Game")
screen.bgcolor("lightblue")
screen.setup(width=600, height=600)

# 2. Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("forestgreen")
player.penup()

# 5. Create the coin
coin = turtle.Turtle()
coin.shape("circle")
coin.color("gold")
coin.penup()
coin.goto(random.randint(-250, 250), random.randint(-250, 250))

# 3. Movement
def move_up():
  player.setheading(90)  # Face North (Up)
  player.forward(20)
  check_collision()

def move_down():
  player.setheading(270)  # Face South (Down)
  player.forward(20)
  check_collision()


def move_left():
  player.setheading(180)  # Face West (Left)
  player.forward(20)
  check_collision()


def move_right():
  player.setheading(0)  # Face East (Right)
  player.forward(20)
  check_collision()

# 6. Check for collision
def check_collision():
  # If turtle gets close to the coin, move the coin to a new spot!
  if player.distance(coin) < 20:
    coin.goto(random.randint(-250, 250), random.randint(-250, 250))

# 4. Keyboard Bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Keep the window open
turtle.done()