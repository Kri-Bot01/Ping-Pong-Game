import turtle

# Score
score_a = 0
score_b = 0

canvas=turtle.Screen()
canvas.title("Pong Game")
canvas.bgcolor("black")
#Size of the widow
canvas.setup(width=800, height=600)#0,0 is center

#Paddle A
pa =turtle.Turtle()#This is our turtle
pa.speed(0)#Speed of animating
pa.shape("square")#different shapes u can try
pa.color("white")
pa.shapesize(stretch_wid=5,stretch_len=1)#uncomment to increase the size
pa.penup()#so that is doesnt draw a line while moving
pa.goto(-350,0)#initial position of paddle

#Paddle B

pb=turtle.Turtle()#This is our turtle
pb.speed(0)#Speed of animating
pb.shape("square")#different shapes u can try
pb.color("white")
pb.shapesize(stretch_wid=5,stretch_len=1)#uncomment to increase the size
pb.penup()#so that is doesnt draw a line while moving
pb.goto(350,0)#initial position of paddle

#Ball
ball =turtle.Turtle()#This is our turtle
ball.speed(0)#Speed of animating
ball.shape("circle")#different shapes u can try
ball.color("white")
ball.penup()
ball.dx=5
ball.dy=5

#Scores
score=turtle.Turtle()
score.penup()
score.speed(0)
score.color("white")
score.hideturtle()
score.goto(0,-270)
score.pen()
score.write("Player A: 0  Player B: 0",align="center",font=("Courier",24,"normal"))

def pa_mov_up():
    y=pa.ycor()
    y=y+20
    pa.sety(y)

def pa_mov_down():
    y=pa.ycor()
    y=y-20
    pa.sety(y)

def pb_mov_up():
    y=pb.ycor()
    y=y+20
    pb.sety(y)

def pb_mov_down():
    y=pb.ycor()
    y=y-20
    pb.sety(y)
    
canvas.listen()
canvas.onkeypress(pa_mov_up,"Up")
canvas.onkeypress(pa_mov_down,"Down")
canvas.onkeypress(pb_mov_up,"w")
canvas.onkeypress(pb_mov_down,"s")

while True:
    canvas.update()#updates screen everytime the loop runs
    
    #Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Edges
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1 # reverse the direction
    elif ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1 # reverse the direction
      
    
    if ball.xcor()>390:
        ball.goto(0,0)
        score_a+=1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx*=-1
    elif ball.xcor()<-390:
        ball.goto(0,0)
        score_b+=1
        score.clear()
        score.write("Player A: {}  Player B: {}".format(score_a,score_b),align="center",font=("Courier",24,"normal"))
        ball.dx*=-1
    if ball.xcor() > 340 and ball.ycor() < pb.ycor() + 50 and ball.ycor() > pb.ycor() - 50:
        ball.setx(340)
        ball.dx*=-1
    elif ball.xcor() < -340 and ball.ycor() < pa.ycor() + 50 and ball.ycor() > pa.ycor() - 50:
        ball.setx(-340)
        ball.dx*=-1