import turtle
import time
import random

delay = 0.1
# setting the score and high score
score = 0
high_score = 0
# Set up the screen
Bob = turtle.Screen()
Bob.title("Snake Game")
Bob.bgcolor("blue")
Bob.setup(width=600, height=600)
Bob.tracer(0)
# create snake head
snakehead = turtle.Turtle()
snakehead.speed(0)
snakehead.shape("circle")
snakehead.color("black")
snakehead.penup()
snakehead.goto(0, 0)
snakehead.direction = "stop"

# Set the food for snake
snakefood = turtle.Turtle()
snakefood.speed(0)
snakefood.shape("circle")
snakefood.color("yellow")
snakefood.penup()
snakefood.goto(0, 100)
# set the segments. The body of the snake
segments = []
# set the score
snakescore = turtle.Turtle()
snakescore.speed(0)
snakescore.shape("circle")
snakescore.color("white")
snakescore.penup()
snakescore.hideturtle()
snakescore.goto(0, 260)
snakescore.write("Score: 0 High Score: 0", align="center", font=("Courier", 24, "normal"))


# Functions
def move():
    if snakehead.direction == "up":
        snakehead.sety(snakehead.ycor() + 20)
    if snakehead.direction == "down":
        snakehead.sety(snakehead.ycor() - 20)
    if snakehead.direction == "left":
        snakehead.setx(snakehead.xcor() - 20)
    if snakehead.direction == "right":
        snakehead.setx(snakehead.xcor() + 20)


def go_up():
    if snakehead.direction != "down":
        snakehead.direction = "up"


def go_down():
    if snakehead.direction != "up":
        snakehead.direction = "down"


def go_left():
    if snakehead.direction != "right":
        snakehead.direction = "left"


def go_right():
    if snakehead.direction != "left":
        snakehead.direction = "right"


# Connection with keyboard
Bob.listen()
Bob.onkeypress(go_up, "Up")
Bob.onkeypress(go_down, "Down")
Bob.onkeypress(go_left, "Left")
Bob.onkeypress(go_right, "Right")
man = True
# game main loop
while man:
    Bob.update()
    # Collision with the borders
    if snakehead.ycor() > 290 or snakehead.ycor() < -290 or snakehead.xcor() < -290 or snakehead.xcor() > 290:
        time.sleep(1)
        snakehead.goto(0, 0)
        snakehead.direction = "stop"
        # Hide the segments if you go out of borders
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        snakescore.clear()
        snakescore.write("Score: {} High Score: {}".format(score, high_score),
                         align="center", font=("Courier", 24, "normal"))
    # spawn food in random location
    if snakehead.distance(snakefood) < 20:
        snakefood.goto(random.randint(-290, 290), random.randint(-290, 290))
        # Add a new  segment behind the head of the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        # increase the score and keep a high score
        score += 10
        if score > high_score:
            high_score = score
        snakescore.clear()
        snakescore.write("Score: {} High Score: {}".format(score, high_score),
                         align="center", font=("Courier", 24, "normal"))
    for index in range(len(segments)-1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        segments[0].goto(snakehead.xcor(), snakehead.ycor())
    move()
    # collision head of the snake with his body. if you eat yourself, you lose and try again
    for segment in segments:
        if segment.distance(snakehead) < 20:
            time.sleep(1)
            snakehead.goto(0, 0)
            snakehead.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()  # clear the segments.
    time.sleep(delay)
Bob.tracer()
