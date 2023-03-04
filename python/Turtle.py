import turtle

t = turtle.Turtle()
t.home()

def OtherShape() :
  q4 = input("Do you want another shape? ")
  if q4 == "yes" or q4 == "Yes" :
    q5 = int(input("How far away(Horizontal)? "))
    t.penup()
    t.forward(q5)
    q6 = int(input("How far away(Vertical)? "))
    if q6 != 0:
      t.left(90)
      t.forward(q6)
    t.pendown()
    DrawShape()

    
    


def DrawShape():
 q = input("which shape do you want? ")
 q7 = input("what color do you want? ")
 t.pencolor(q7)
 q8 = int(input("what thickness do want for the pen? "))
 t.pensize(q8)
 if q == "square":
  q2 = int(input("What size do you want? "))
  
  t.forward(q2)
  t.left(90)
  t.forward(q2)
  t.left(90)
  t.forward(q2)
  t.left(90)
  t.forward(q2)
  t.left(90)
  OtherShape()

 elif q == "diamond":
  q2 = int(input("What size do you want? "))

  t.left(60)
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  t.left(60)
  t.left(60)
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  t.left(60)
  OtherShape()

 elif q == "hexagon" :
  q2 = int(input("What size do you want? "))
 
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  t.left(60)
  t.forward(q2)
  OtherShape()

 elif q == "triangle" :
  q2 = int(input("What size do you want? "))

  t.forward(q2)
  t.left(120)
  t.forward(q2)
  t.left(120)
  t.forward(q2)
  OtherShape()

 elif q == "circle" :
   q2 = int(input("What size do you want? "))
   q3 = int(input("How many degrees do you want? "))
  
   t.circle(q2, q3)
   OtherShape()


DrawShape()