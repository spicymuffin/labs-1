# Horse Racing Program (Stage 1)

import turtle


def newHorse():
    horse = turtle.Turtle()
    return horse


def generateHorses(num_horses):
    horses = []
    for k in range(0, num_horses):
        horse = newHorse()
        horses.append(horse)

    return horses


def placeHorses(horses, loc, separation):
    for k in range(0, len(horses)):
        horses[k].hideturtle()
        horses[k].penup()
        horses[k].setposition(loc[0], loc[1] + k * separation)
        horses[k].setheading(180)
        horses[k].showturtle()

# ---- main


# init number of horses
num_horses = 10

# set window size
turtle.setup(750, 800)

# get turtle window
window = turtle.Screen()

# set window title bar
window.title('Horse Race Simulation Program')

# init screen layout parameters
start_loc = (240, -200)
track_separation = 60

# generate and init horses
horses = generateHorses(num_horses)

# place horses at starting line
placeHorses(horses, start_loc, track_separation)

# terminate program when close window
turtle.exitonclick()
