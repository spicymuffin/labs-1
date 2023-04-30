import turtle
turtle.setup(500, 500)

window = turtle.Screen()
window.title("this is so fun!!11!")

t = turtle.getturtle()
t.speed(0)

t.penup()
t.setposition(-250, -250)
t.pendown()
t.setposition(250, 250)
t.penup()
t.setposition(-250, 250)
t.pendown()
t.setposition(250, -250)

window.exitonclick()
