import turtle
turtle.speed(2)
turtle.penup() #Pick up the pen so it doesn’t

#draw

turtle.goto(-200,-100) #Move the turtle to the

#position (-200, -100)

#on the screen

turtle.pendown() #Put the pen down to start

#drawing

#Draw the M:

turtle.goto(-200,-100+200)

turtle.goto(-200+50,-100)

turtle.goto(-100,+100)

turtle.goto(-100,-100)

#E
turtle.penup()
turtle.goto(-80, -100)
turtle.pendown()
turtle.goto(-80, +100)
turtle.goto(-10, +100)

turtle.penup()
turtle.goto(-80, 0)
turtle.pendown()
turtle.goto(-10, 0)

turtle.penup()
turtle.goto(-80, -100)
turtle.pendown()
turtle.goto(-10, -100)


#E2
turtle.penup()
turtle.goto( 10, -100)
turtle.pendown()
turtle.goto(80, -100)
turtle.goto(10, -100)
turtle.goto(10, 100)
turtle.goto(80, 100)
turtle.penup()
turtle.goto(10, 0)
turtle.pendown()
turtle.goto(80, 0)

#T
turtle.penup()
turtle.goto(100, 100)
turtle.pendown()
turtle.goto(170, 100)
turtle.goto(135, 100)
turtle.goto(135, -100)

turtle.mainloop()
