# Survival first

import turtle
import snakeFunctions
import random

class turnObject:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

# give the path to a given coordinate (endx, endy)
# returns True if it does intersect self, False if there is a valid path
def intersectSelf(beginning, initial_segments, endx, endy, distance, turns):
    test = create_new_head(beginning)
    testSegments = create_new_segments(initial_segments)

    count = 0
    while True:
        count += 1
        if (test.xcor() > 290) or (test.xcor() < -290) or (test.ycor() > 290) or (test.ycor() < -290):
            return True
        
        if abs(test.xcor() - endx) < distance and abs(test.ycor() - endy) < distance:
            return False
        
        # look at the three possible directions it could take, which ones ensure survival
        upOk = True
        if test.direction != "down":
            if test.ycor() == 280:
                upOk = False
            elif trapSelf(test, testSegments, distance, "up"):
                upOk = False
            else:
                for segment in testSegments:
                    if equalCoordinates(segment, test.xcor(), test.ycor() + 20):
                        # don't go up
                        upOk = False
                        break
            
        downOk = True
        if test.direction != "up":
            if test.ycor() == -280:
                downOk = False
            elif trapSelf(test, testSegments, distance, "down"):
                downOk = False
            else:
                for segment in testSegments:
                    if equalCoordinates(segment, test.xcor(), test.ycor() - 20):
                        # don't go down
                        downOk = False
                        break
            
        leftOk = True
        if test.direction != "right":
            if test.xcor() == -280:
                leftOk = False
            elif trapSelf(test, testSegments, distance, "left"):
                leftOk = False
            else:
                for segment in testSegments:
                    if equalCoordinates(segment, test.xcor() - 20, test.ycor()):
                        # don't go left
                        leftOk = False
                        break

        rightOk = True
        if test.direction != "left":
            if test.xcor() == 280:
                rightOk = False
            elif trapSelf(test, testSegments, distance, "right"):
                rightOk = False
            else:
                for segment in testSegments:
                    if equalCoordinates(segment, test.xcor() + 20, test.ycor()):
                        # don't go right
                        rightOk = False
                        break
            
        # if all three possible directions are bad, return True
        if upOk + downOk + leftOk + rightOk == 1:
            return True

        # look at the booleans that are true, find optimal direction
        # that benefits the path to the end coordinates
        direction = ""
    
        if upOk and test.direction != "down":
            if test.ycor() < endy:
                direction = "up"
                
        if downOk and test.direction != "up":
            if test.ycor() > endy:
                direction = "down"
                
        if leftOk and test.direction != "right":
            if test.xcor() > endx:
                direction = "left"
    
        if rightOk and test.direction != "left":
            if test.xcor() < endx:
                direction = "right"
                
        # if after all this, direction has not been altered, then there is
        # no good path, and we have to ensure survival first, so pick any
        # path that will survive
        if direction == "":
            randomDirection = []

            if upOk and test.direction != "down":
                randomDirection.append("up")
            if downOk and test.direction != "up":
                randomDirection.append("down")
            if leftOk and test.direction != "right":
                randomDirection.append("left")
            if rightOk and test.direction != "left":
                randomDirection.append("right")
            
            direction = random.choice(randomDirection)
                
        # add the pathway to turns
        newTurn = turnObject(test.xcor(), test.ycor(), direction)
        if (len(turns) == 0) or (direction != turns[len(turns) - 1].direction):
            turns.append(newTurn)
    
        # make "test" move in the optimal direction
        test.direction = direction
        snakeFunctions.moveSegments(test, testSegments)
        snakeFunctions.move(test, distance)

# if there is a path to the tail that doesn't intersect self, then we are safe
# returns true if we are trapped, false if we are safe
def trapSelf(head, segments, distance, direction):
    if len(segments) > 1:
        # going from the test to the tail, is there a path?
        test = create_new_head(head)
        testSegments = create_new_segments(segments)
        lastOne = len(testSegments) - 1

        # move in the direction
        test.direction = direction
        snakeFunctions.moveSegments(test, testSegments)
        endx = testSegments[lastOne].xcor()
        endy = testSegments[lastOne].ycor()
        snakeFunctions.move(test, distance)


        count = 0
        # set the variables
        while True:
            count += 1
            if (test.xcor() > 290) or (test.xcor() < -290) or (test.ycor() > 290) or (test.ycor() < -290):
                return True
            
            if abs(test.xcor() - endx) < distance and abs(test.ycor() - endy) < distance:
                return False
            
            # look at the three possible directions it could take, which ones ensure survival
            upOk = True
            if test.direction != "down":
                if test.ycor() == 280:
                    upOk = False
                else:
                    for segment in testSegments:
                        if equalCoordinates(segment, test.xcor(), test.ycor() + 20):
                            # don't go up
                            upOk = False
                            break
                
            downOk = True
            if test.direction != "up":
                if test.ycor() == -280:
                    downOk = False
                else:
                    for segment in testSegments:
                        if equalCoordinates(segment, test.xcor(), test.ycor() - 20):
                            # don't go down
                            downOk = False
                            break
                
            leftOk = True
            if test.direction != "right":
                if test.xcor() == -280:
                    leftOk = False
                else:
                    for segment in testSegments:
                        if equalCoordinates(segment, test.xcor() - 20, test.ycor()):
                            # don't go left
                            leftOk = False
                            break

            rightOk = True
            if test.direction != "left":
                if test.xcor() == 280:
                    rightOk = False
                else:
                    for segment in testSegments:
                        if equalCoordinates(segment, test.xcor() + 20, test.ycor()):
                            # don't go right
                            rightOk = False
                            break
                
            # if all three possible directions are bad, return True
            if upOk + downOk + leftOk + rightOk == 1:
                return True

            # look at the booleans that are true, find optimal direction
            # that benefits the path to the end coordinates
            direction = ""
        
            if upOk and test.direction != "down":
                if test.ycor() < endy:
                    direction = "up"
                    
            if downOk and test.direction != "up":
                if test.ycor() > endy:
                    direction = "down"
                    
            if leftOk and test.direction != "right":
                if test.xcor() > endx:
                    direction = "left"
        
            if rightOk and test.direction != "left":
                if test.xcor() < endx:
                    direction = "right"
                    
            # if after all this, direction has not been altered, then there is
            # no good path, and we have to ensure survival first, so pick any
            # path that will survive
            if direction == "":
                randomDirection = []

                if upOk and test.direction != "down":
                    randomDirection.append("up")
                if downOk and test.direction != "up":
                    randomDirection.append("down")
                if leftOk and test.direction != "right":
                    randomDirection.append("left")
                if rightOk and test.direction != "left":
                    randomDirection.append("right")
                
                direction = random.choice(randomDirection)
        
            # make "test" move in the optimal direction
            test.direction = direction
            snakeFunctions.moveSegments(test, testSegments)
            snakeFunctions.move(test, distance)
    return False

def botDirectionChange(head, segments, food, distance, turns):
    # if our set of moves has not been made yet, then make it
    if len(turns) == 0:
        intersected = intersectSelf(head, segments, food.xcor(), food.ycor(), distance, turns)

    # make the proper adjustments to head based on the values in "turns"
    for turn in turns:
        if turn.x == head.xcor() and turn.y == head.ycor():
            head.direction = turn.direction

# HELPER FUNCTIONS

def equalCoordinates(turtle, x, y):
    if (turtle.xcor() == x):
        if (turtle.ycor() == y):
            return True
    return False

def create_new_turtle(original_turtle):
    new_turtle = turtle.Turtle()
    new_turtle.penup()
    new_turtle.goto(original_turtle.position())
    new_turtle.speed(original_turtle.speed())
    new_turtle.shape(original_turtle.shape())
    new_turtle.hideturtle()
    return new_turtle

def create_new_head(original_turtle):
    new_turtle = create_new_turtle(original_turtle)
    new_turtle.direction = original_turtle.direction
    return new_turtle

def create_new_segment(original_segment):
    new_turtle = create_new_turtle(original_segment)
    return new_turtle

def create_new_segments(original_segments):
    new_segments = []
    for segment in original_segments:
        one_new_segment = create_new_segment(segment)
        new_segments.append(one_new_segment)
    return new_segments
