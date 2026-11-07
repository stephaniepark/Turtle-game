import turtle

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

# Keep the window open
turtle.done()