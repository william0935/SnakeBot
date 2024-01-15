import turtle
import snakeBot
import snakeFunctions

# Basics
distance = 20
square_length = 20
screen = turtle.Screen()
score = 0

# Turns stores the coordinates and direction of the turn
turns = []

# Set up screen, grid, board
snakeFunctions.setUpScreen(screen)
grid = turtle.Turtle()
grid.speed(0)
grid.shape("square")
grid.color("blue")
grid.penup()
grid.hideturtle()
snakeFunctions.setUpGrid(grid, square_length)

scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("black")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 260)
scoreBoard.write("Score: 0", align="center", font=("Arial", 20, "normal"))

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake apple
apple = turtle.Turtle()
apple.speed(0)
apple.shape("circle")
apple.color("red")
apple.penup()
apple.goto(0,100)

# Snake body
segments = []

# Main game loop
while True:
    screen.update()

    # Check for a collision with the border
    score = snakeFunctions.checkCollisionBorder(head, score)

    # Check for a collision with the apple
    score = snakeFunctions.checkCollisionApple(head, scoreBoard, segments, apple, score, turns)

    # Bot change direction
    snakeBot.botDirectionChange(head, segments, apple, distance, turns)

    # Move segments and head
    snakeFunctions.moveSegments(head, segments)
    snakeFunctions.move(head, distance)

    # Check for head collision with the body segments
    score = snakeFunctions.checkCollisionBody(head, segments, score, distance)

wn.mainloop()