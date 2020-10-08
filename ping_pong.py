import turtle, random, winsound
# winsound.PlaySound("pat.wav",winsound.SND_ASYNC) - playing sound files on  windows,
# os.system("aplay pat.wav&") - play on linux, & is to not stop programing and run without any stop
# os.system("afplay pat.wav&") - play on linux, & is to not stop programing and run without any stop

new_window = turtle.Screen()
new_window.title('*Ping Pong Game*')
new_window.bgcolor('grey')
new_window.setup(width=800,height=600)
new_window.tracer(0)

# Score
score_a = 0
score_b = 0
end_match_number = 10

# OBJECTS: Paddle A (mustukas)
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set to maximum speed
paddle_a.shape('square')
paddle_a.color('black')
paddle_a.shapesize(7,0.4)
paddle_a.penup()
paddle_a.goto(-370,0)

# OBJECTS: Paddle B (mustukas)
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set to maximum speed
paddle_b.shape('square')
paddle_b.color('black')
paddle_b.shapesize(7,0.4)
paddle_b.penup()
paddle_b.goto(370,0)

# OBJECTS: Ball (kamuolis)
ball = turtle.Turtle()
ball.speed(0) # set to maximum speed
ball.shape('circle')
ball.color('black')
ball.penup()
ball.goto(0,0)
# Ball  movement
ran_choice = [1,-1]
ball.dx = 0.2 * random.choice(ran_choice)
ball.dy = 0.2 * random.choice(ran_choice)

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('#622e0c')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=('Gravtrac',20,'normal'))


### Functions ###
def paddle_a_up():
    y = paddle_a.ycor()
    if y < 240:
        y += 20
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y > -220:
        y -= 20
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y < 240:
        y += 20
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y > -220:
        y -= 20
        paddle_b.sety(y)

# Keybaord binding
new_window.listen()
new_window.onkeypress(paddle_a_up,'w')
new_window.onkeypress(paddle_a_down,'s')
new_window.onkeypress(paddle_b_up,'Up')
new_window.onkeypress(paddle_b_down,'Down')
# new_window.onkeypress(endGame,'n')


def border_check_balls(obj_b, p_a, p_b):
    global score_a,score_b, ran_choice
    # Checking vertical liens if hitting the roof
    if obj_b.ycor() > 290:
        obj_b.sety(290)
        obj_b.dy *=-1
        winsound.PlaySound("pat.wav",winsound.SND_ASYNC)

    if obj_b.ycor() < -290:
        obj_b.sety(-290)
        obj_b.dy *=-1
        winsound.PlaySound("pat.wav",winsound.SND_ASYNC)
        # os.system("aplay pat.wav")

    # Checking horizontaly lines, going off the grid or passing the panel
    if obj_b.xcor() > 390:
        obj_b.goto(0,0)
        obj_b.dx *= random.choice(ran_choice)
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=('Gravtrac',20,'normal'))

    if obj_b.xcor() < -390:
        obj_b.goto(0,0)
        obj_b.dx *= random.choice(ran_choice)
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=('Gravtrac',20,'normal'))

    # paddle and ball colision (Right side ->)
    if (obj_b.xcor() > 360 and obj_b.xcor() < 370) and (obj_b.ycor() < p_b.ycor()+60 and obj_b.ycor() > p_b.ycor() -60):
        obj_b.setx(360)
        obj_b.dx *= -1
        winsound.PlaySound("pat.wav",winsound.SND_ASYNC)

    # paddle and ball colision (Left side <-)
    if (obj_b.xcor() < -360 and obj_b.xcor() > -370) and (obj_b.ycor() < p_a.ycor()+60 and obj_b.ycor() > p_a.ycor() -60):
        obj_b.setx(-360)
        obj_b.dx *= -1
        winsound.PlaySound("pat.wav",winsound.SND_ASYNC)

### MAIN GAME LOOP ###
while True:
    new_window.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if score_a == end_match_number:
        cont_g = new_window.textinput("Player A won","Want to continue? Y/N")
        if cont_g == None or cont_g.lower() != "y":
            new_window.bye()
        else:
            score_a,score_b = 0,0
            paddle_a.goto(-370,0)
            paddle_b.goto(370,0)
            ball.goto(0,0)
            pen.clear()
            pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=('Gravtrac',20,'normal'))
            new_window.listen()
    elif score_b == end_match_number:
        cont_g = new_window.textinput("Player B won","Want to continue? Y/N")
        if cont_g == None or cont_g.lower() != "y":
            new_window.bye()
        else:
            score_a,score_b = 0,0
            paddle_a.goto(-370,0)
            paddle_b.goto(370,0)
            ball.goto(0,0)
            pen.clear()
            pen.write(f"Player A: {score_a} Player B: {score_b}", align='center', font=('Gravtrac',20,'normal'))
            new_window.listen()
    else:
        border_check_balls(ball,paddle_a,paddle_b)
