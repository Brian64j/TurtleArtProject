def body(t,r):
    t.width(3)
    t.color(255,186,210)
    t.penup()
    t.goto(0,-100)
    t.pendown()
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def eyes(t,x,y):
    for times in range(90):
        t.color(0,0,0)
        t.begin_fill()
        t.circle(25)
        t.goto(x,y-times)
        t.end_fill()

def checks(t,x,y):
    for times in range(30):
        t.color(219,112,147)
        t.begin_fill()
        t.circle(20)
        t.goto(x+times,y)
        t.end_fill()

def pup(t,x,y):
    for times in range(15):
        t.color(255,255,255)
        t.begin_fill()
        t.circle(20)
        t.goto(x,y-times)
        t.end_fill()

def bluepup(t,x,y):
    for times in range(15):
        t.color(0,39,51)
        t.begin_fill()
        t.circle(25)
        t.goto(x,y-times)
        t.end_fill()

def mouth(t):
    t.color(0,0,0)
    t.begin_fill()
    t.circle(30)
    t.end_fill()

def mouthz(t):
    t.color(255,105,180)
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
def leftfoot(t,x,y):
    for times in range(50):
        t.color(156,34,93)
        t.begin_fill()
        t.circle(-10+times+20)
        t.goto(x-times*3,y-10)
        t.end_fill()
def rightfoot(t,x,y):
    for times in range(50):
        t.color(156,34,93)
        t.begin_fill()
        t.circle(-10+times+20)
        t.goto(x+times*3,y-10)
        t.end_fill()
def righthand(t,x,y):
    for times in range(30):
        t.color(255,186,210)
        t.begin_fill()
        t.goto(x-times,y-times)
        t.circle(20)
        t.end_fill()

def circle(t):
    t.color(255,186,210)
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def lefthand(t,x,y):
    for times in range(30):
        t.color(255,186,210)
        t.begin_fill()
        t.goto(x+times,y-times)
        t.circle(20)
        t.end_fill()
