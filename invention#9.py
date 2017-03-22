from myfunction import *
import turtle

bob=turtle.Turtle()
turtle.colormode(255)
bob.speed(0)
turtle.bgcolor("black")

for times in range(256):
    c=(times,times,255-times)
    bob.color(c)
    print(c)
    polygon(bob,4,50)
    bob.left(163)
    bob.forward(times)
    
jump(bob,350,-200)    
for times in range(256):
    jump(bob,350,-200)
    c=(times,0,255-times)
    bob.color(c)
    print(c)
    polygon(bob,4,50)
    bob.left(163)
    bob.forward(times)

jump(bob,350,-200)
for times in range(256):
    jump(bob,350,200) 
    c=(0,times,255-times)
    bob.color(c)
    print(c)
    polygon(bob,4,50)
    bob.left(163)
    bob.forward(times)

jump(bob,350,-200) 
for times in range(256):
    jump(bob,-350,200) 
    c=(times,255-times,255-times)
    bob.color(c)
    print(c)
    polygon(bob,4,50)
    bob.left(163)
    bob.forward(times)

jump(bob,350,-200) 
for times in range(256):
    jump(bob,-350,-200) 
    c=(times,0,times)
    bob.color(c)
    print(c)
    polygon(bob,4,50)
    bob.left(163)
    bob.forward(times)
