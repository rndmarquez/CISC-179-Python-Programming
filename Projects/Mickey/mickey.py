"""
File: mikcey.py
Author: Ron Marquez
Programming Project - Mickey Mouse

Provide a file that creates a mickey mouse head
1. face is blue  (RGB for Blue = 0,0,255)
2. eyes and ears are red (RGB for Red = 139,0,0)
3. radius of the circle of the face is 2x radius of the ears
4. radius of the eyes are 20% of the radius of teh face
5. ears and face should not intersect  too much
6. eyes should not be too far or too close apart

Adds a command to view a file's contents.
"""
import turtle

def main():
    
    mickeysHead(0,-60,"blue")
    mickeysEars(135,120, "red" )
    mickeysEyes(45,60, "red" )



def mickeysEars(x,y,color):
    mickeysRightEar(x,y,color)
    mickeysLeftEar(-x,y,color)

def mickeysEyes(x,y,color):
    mickeysRightEye(x,y,color)
    mickeysLeftEye(-x,y,color)
   

def mickeysHead(x,y,color):
    ##define t
    t = turtle.Turtle()
    t.speed(10)

    ##set origin
    t.penup()
    t.goto(x,y)       ##bring center point down by 1/2 radius
    t.pendown()
    
    t.color(color,color)   ##make the outline of the shape fill same color
    t.begin_fill()
    t.circle(120,360)      ##draw head 
    t.end_fill()
    t.penup()

    t.hideturtle()

    
def mickeysRightEar(x,y,color):
##    Draws Mickeys right ear with a
##    radius of 60 (50% of 120(radius of Mickeys head))
    
    ##define t
    t = turtle.Turtle()
    t.speed(10)

    t.penup()
    t.goto(x,y)     ##goto to right ear location
    t.pendown()
    
    t.color(color,color)
    t.begin_fill()
    t.circle(60,360)
    t.end_fill()
    t.penup()

    t.hideturtle()

def mickeysLeftEar(x,y,color):
##    Draws Mickeys left ear with a
##    radius of 60 (50% of 120(radius of Mickeys head))


    ##define t
    t = turtle.Turtle()
    t.speed(10)
    
    t.penup()
    t.goto(x,y)    ##goto to left ear location
    t.pendown()
    
    t.color(color,color)
    t.begin_fill()
    t.circle(60,360)
    t.end_fill()
    t.penup()

    t.hideturtle()

def mickeysRightEye(x,y,color):
##    Draws Mickeys right eye with a
##    radius of 24 (20% of 120(radius of Mickeys head))

    
    ##define t
    t = turtle.Turtle()
    t.speed(10)

    t.penup()
    t.goto(x,y)         ##starting position
    t.pendown()
    
    t.color(color,color)
    t.begin_fill()
    t.circle(24,360)      
    t.end_fill()
    t.penup()

    t.hideturtle()      ##hide the turtle

def mickeysLeftEye(x,y,color):
##    Draws Mickeys left eye with a
##    radius of 24 (20% of 120(radius of Mickeys head))
    
    ##define t
    t = turtle.Turtle()
    t.speed(10)

    t.penup()
    t.goto(x,y)         ##recenter
    t.pendown()
    
    t.color(color,color)
    t.begin_fill()
    t.circle(24,360)      ##right eye
    t.end_fill()
    t.penup()

    t.hideturtle()


if __name__ == "__main__":
    main()
