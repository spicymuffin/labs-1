import turtle
turtle.setup(500, 500)

window = turtle.Screen()
window.title("this is so fun!!11!")  # title for fun!!!

t = turtle.getturtle()  # make turtle
t.speed(0)

t.penup()
t.setposition(-250, -250)  # lower left
t.pendown()
t.setposition(250, 250)  # upper right
t.penup()
t.setposition(-250, 250)  # upper left
t.pendown()
t.setposition(250, -250)  # lower left

window.exitonclick()
