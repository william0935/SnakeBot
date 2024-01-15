import turtle
import time
import random

# Set up the screen
def setUpScreen(screen):
    screen.setup(width = 600, height = 600)
    screen.tracer(0)

def setUpGrid(grid, square_length):
    # Set up grid
    grid.speed(100)
    grid.left(90)
    grid.color('blue')

    # Drawing y-axis lines
    def drawy(val):
        grid.setpos(val + square_length, -310)
        grid.down()
        grid.forward(800)
        grid.up()
        grid.setpos(val, -310)
        grid.down()
        grid.backward(800)
        grid.up()
        
    # Drawing x-axis lines
    def drawx(val):
        grid.setpos(-310, val + square_length)
        grid.down()
        grid.forward(800)
        grid.up()
        grid.setpos(-310, val)
        grid.down()
        grid.backward(800)
        grid.up()

    for i in range(30):
        drawy(square_length * (i + 1) - 330)

    grid.right(90)

    for i in range(30):
        drawx(square_length * (i + 1) - 330)

def go_up(head):
    if head.direction != "down":
        head.direction = "up"

def go_down(head):
    if head.direction != "up":
        head.direction = "down"

def go_left(head):
    if head.direction != "right":
        head.direction = "left"

def go_right(head):
    if head.direction != "left":
        head.direction = "right"

def move(head, distance):
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + distance)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - distance)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - distance)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + distance)

def checkCollisionBorder(head, score):
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1000)
        exit()
    return score

def checkCollisionApple(head, pen, segments, apple, score, turns):
    if head.distance(apple) < 20:
        # Move the apple to a random spot
        # TEMPORARY FIX FOR MAKING SURE APPLE NOT IN BODY
        while True:
            notBody = True
            x = 20 * random.randint(-14, 14)
            y = 20 * random.randint(-14, 14)
            for segment in segments:
                if x == segment.xcor() and y == segment.ycor():
                    notBody = False
            if notBody:
                apple.goto(x, y)
                break

        # New segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Increase score, clear turns
        score += 1
        turns.clear()
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
    return score

def checkCollisionBody(head, segments, score, distance):
    for segment in segments:
        if segment.distance(head) < distance:
            time.sleep(1000)
            exit()
    return score

def moveSegments(head, segments):
    # Move segments by reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)