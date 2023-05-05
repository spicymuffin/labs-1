# Horse Racing Program (Stage 3)

import turtle
import random


def getHorseImages(num_horses):
    # init empty list
    images = []

    # get all horse images
    for k in range(0, num_horses):
        images = images + ['img/horse_' + str(k+1) + '_image.gif']

    return images


def registerHorseImages(images):
    for k in range(0, len(images)):
        turtle.register_shape(images[k])


def newHorse(image_file):
    horse = turtle.Turtle()
    horse.hideturtle()
    horse.shape(image_file)

    return horse


def generateHorses(images, num_horses):
    horses = []
    for k in range(0, num_horses):
        horse = newHorse(images[k])
        horses.append(horse)

    return horses


def placeHorses(horses, loc, separation):
    for k in range(0, len(horses)):
        horses[k].hideturtle()
        horses[k].penup()
        horses[k].setposition(loc[0], loc[1] + k * separation)
        horses[k].setheading(180)
        horses[k].showturtle()
        horses[k].pendown()


def startHorses(horses, finish_line, forward_incr):
    # init
    have_winner = False

    k = 0
    while not have_winner:
        horse = horses[k]
        horse.forward(random.randint(1, 3) * forward_incr)

        # check for horse over finish line
        if horse.position()[0] < finish_line:
            have_winner = True
        else:
            k = (k+1) % len(horses)
    return k


def displayWinner(winning_horse):
    print('Horse', winning_horse, 'the winner!')

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
finish_line = -240
track_separation = 60
forward_incr = 6

# register images
horse_images = getHorseImages(num_horses)
registerHorseImages(horse_images)

# generate and init horses
horses = generateHorses(horse_images, num_horses)

# place horses at starting line
placeHorses(horses, start_loc, track_separation)

# start horses
winner = startHorses(horses, finish_line, forward_incr)

# display winning horse
displayWinner(winner + 1)

# terminate program when close window
turtle.exitonclick()
