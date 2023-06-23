# Horse Racing Program (Stage 2)

import turtle


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

# register images
horse_images = getHorseImages(num_horses)
registerHorseImages(horse_images)

# generate and init horses
horses = generateHorses(horse_images, num_horses)

# place horses at starting line
placeHorses(horses, start_loc, track_separation)

# terminate program when close window
turtle.exitonclick()
