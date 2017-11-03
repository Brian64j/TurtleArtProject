import turtle
bob = turtle.Turtle()
from MyFuntionki import*
bob.speed(100)

turtle.colormode(255) 
bob.penup()
bob.goto(-70,-100)#makes the pen not draw as it moves to a certain location
bob.pendown()
leftfoot(bob,-70,-90) #Brings the foot before the body so the body can overlap
bob.penup()
bob.goto(70,-100)
bob.pendown()
rightfoot(bob,70,-90)#Brings the foot before the body so the body can overlap
body(bob,200)#brings the body
bob.penup()
bob.goto(-50,100)
bob.pendown()
bob.left(90)
bob.forward(100)#not really necessary but its still there
eyes(bob,-50,200)#the eyes before the pupil or the blue shade
bob.penup()
bob.goto(50,100)
bob.pendown()
bob.forward(100)
bob.color(0,0,0)
eyes(bob,50,200)#the eyes before the pupil or the blue shade
bob.penup()
bob.goto(100,85)
bob.pendown()
checks(bob,100,85)
bob.penup()
bob.goto(-130,85)
bob.pendown()
checks(bob,-130,85)
bob.penup()
bob.goto(-50,200)
bob.pendown()
pup(bob,-50,200)
bob.penup()
bob.goto(-50,120)
bob.pendown
bluepup(bob,-50,120)#adds another color in his eyes
bob.penup()
bob.goto(50,200)
bob.pendown()
pup(bob,50,200)
bob.penup()
bob.goto(50,120)
bob.pendown()
bluepup(bob,50,120)#adds another color in his eyes
bob.penup()
bob.goto(20,50)
bob.pendown()
mouth(bob)
bob.penup()
bob.goto(20,40)
mouthz(bob)#Acts like a tounge
bob.penup()
bob.goto(-185,100)
bob.pendown()
righthand(bob,-185,130)
bob.penup()
bob.goto(-180,65)
bob.pendown()
circle(bob)#makes it look like he has nubs as fingers
bob.penup()
bob.goto(235,130)
bob.pendown()
lefthand(bob,220,130)
bob.penup()
bob.goto(275,65)
bob.pendown()
circle(bob)#makes it look like he has nubs as fingers
