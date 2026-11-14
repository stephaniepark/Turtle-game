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

# 8. Create a score display
score = 0

# Create a text turtle for the score
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("navy")
score_display.goto(0, 260)

# 10. Create timer
time_left = 30
timer_display = turtle.Turtle()
timer_display.hideturtle()
timer_display.penup()
timer_display.color("darkred")
timer_display.goto(0, 230)

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
  global score
  # If turtle gets close to the coin, move the coin to a new spot!
  if player.distance(coin) < 20:
    score += 1
    update_score()
    coin.goto(random.randint(-250, 250), random.randint(-250, 250))

# 9. Update the score
def update_score():
  score_display.clear()
  score_display.write(
      "Score: " + str(score), align="center", font=("Arial", 16, "bold")
  )

# 11. Update timer

def update_timer():
  global time_left
  if time_left > 0:
    timer_display.clear()
    timer_display.write(
        "Time Left: " + str(time_left) + "s", align="center", font=("Arial", 14, "normal")
    )
    time_left -= 1
    screen.ontimer(update_timer, 1000)  # Call this function again in 1 second
  else:
    timer_display.clear()
    timer_display.write(
        "Game Over! Final Score: " + str(score),
        align="center",
        font=("Arial", 16, "bold"),
    )
    coin.hideturtle()

# Function to cleanly close the turtle window
def quit_game():
    screen.bye()

# Bind the 'q' key to the quit function
screen.onkey(quit_game, "q")

# 4. Keyboard Bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

update_score()
update_timer()

# Keep the window open
turtle.done()