def tear(t):
    for times in range(10):
        t.circle(times * 2)
        t.left(10)
        t.forward(10)
        
def L(t,distance,angle):
    t.forward(distance)
    t.left(angle)
    t.forward(distance)
    

def polygon(t, sides, distance):
    angle = 360 / sides
    t.begin_fill()
    for times in range(sides):
        t.forward(distance)
        t.left(angle)
    t.end_fill()

def cool(t):
    t.color("blue")
    polygon(t,5,100)
    t.color("black")
    polygon(t,4,100)
    t.color("orange")
    polygon(t,3,100)

def coolSquared(t):
    for times in range(4):
        cool(t)
        t.right(90)

def jump(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def flower(t,size):
    for times in range(10):
        t.left(times*36)
        tears(t,size)
        t.penup()
        t.home()
        t.pendown()

def tears(t,size):
    t.width(15)
    for times in range(10):
        t.begin_fill()
        c=(0,0,0)
        t.color(c)
        t.circle(times*2)
        t.left(10)
        t.forward(size)
        t.end_fill()

def star(t,distance):
    t.begin_fill()
    for times in range(4):
        t.forward(distance)
        t.left(60)
        t.forward(distance)
        t.right(150)
    t.end_fill()

def sun(t, c):
    t.color(c)
    print(c)
    polygon(t,4,60)
    t.left(163)
    
    
