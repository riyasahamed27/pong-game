import turtle

# player
score_a = 0
score_b = 0
# display window
win = turtle.Screen()
win.setup(800, 600)
win.bgcolor("blue")
win.title("Pong Game")
win.tracer(0)

# left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380, 0)

# right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(380, 0)

# ball paddle
ball_paddle = turtle.Turtle()
ball_paddle.shape("circle")
ball_paddle.color("white")
ball_paddle.penup()
ball_paddle.dx = 0.20
ball_paddle.dy = 0.20

# score board
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Ariel", 24, "normal"))

def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)

def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)

def right_paddle_up():
    right_paddle.sety(right_paddle.ycor()+20)

def right_paddle_down():
    right_paddle.sety(right_paddle.ycor()-20)

# moving paddle
win.listen()
win.onkeypress(left_paddle_up, "w")
win.onkeypress(left_paddle_down, "s")
win.onkeypress(right_paddle_up, "Up")
win.onkeypress(right_paddle_down, "Down")

while True:
    win.update()

    # moving ball
    ball_paddle.setx(ball_paddle.xcor() + ball_paddle.dx)
    ball_paddle.sety(ball_paddle.ycor() + ball_paddle.dy)

    # top wall
    if ball_paddle.ycor() > 290:
        ball_paddle.sety(290)
        ball_paddle.dy *= -1

    # bottom wall
    if ball_paddle.ycor() < -290:
        ball_paddle.sety(-290)
        ball_paddle.dy *= -1

    # right wall
    if ball_paddle.xcor() > 390:
        ball_paddle.setx(390)
        ball_paddle.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))

    # left wall
    if ball_paddle.xcor() < -390:
        ball_paddle.setx(-390)
        ball_paddle.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Ariel", 24, "normal"))

    # collision with paddle
    if ball_paddle.xcor() > 370 and right_paddle.ycor()-50 < ball_paddle.ycor() < right_paddle.ycor()+50:
        ball_paddle.dx *= -1

    if ball_paddle.xcor() < -370 and left_paddle.ycor()-50 <  ball_paddle.ycor() < left_paddle.ycor()+50:
        ball_paddle.dx *= -1