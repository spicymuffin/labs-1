
from globals import FOODMAX, STEPMAX, WIDTH, HEIGHT, X_MAX, Y_MAX, MS_TO_QUIT
from globals import FOOD as food, GHOSTS as ghosts
# Import our own constants

from characters import ghost, doboggi, doboggi_man
# Import our game character classes

from lab13_p3 import auto_doboggi_man
# Import your self-moving auto_doboggi_man class

import turtle
import random


def shutDownHander():
    """Outputs score and terminates the program"""
    global score
    print('Your score:', score)
    window.bye()


def checkCollision(t1, t2):
    """Input: 2 coordinate tuples.
       Return: True if the coordinates are sufficiently close
               False otherwise
    """
    if (abs(t1[0] - t2[0]) < 25) and (abs(t1[1] - t2[1]) < 25):
        return True
    return False


def periodicTimer():
    """Timer function which is called periodically by Python.
       This function implements the game logic:
       - creating all objects
       - arranging objects on the screen
       - calling object's move() methods
       - checking for collisions
       - checking for invalid moves
       - detection program termination conditions (all food eaten, ...)
       - initiate termination
    """
    global phase
    global isQuit
    global food
    global score         # doboggi_man's achieved score
    turtle.tracer(0, 0)  # disable screen updates
    for g in ghosts:
        g.updateShape()   # make ghost change its shape
        g.move()          # move ghost
    if phase % 4 == 0:
        # pm shape is updated every 4th iteration.
        pm.updateShape()  # make doboggi_man change its shape
    p_old = pm.getPosition()
    pm.move()           # move doboggi_man
    p_new = pm.getPosition()
    # Check for illegal moves:
    if (abs(p_old[0] - p_new[0]) > 12) or (abs(p_old[1] - p_new[1]) > 12):
        print('Illegal move, game terminated.')
        isQuit = True
    turtle.update()       # force turtle module's screen update
    turtle.tracer(1, 10)  # re-enable periodic screen updates
    pm.decrementSteps()  # doboggi_man made one step, decrement counter
    if pm.getRemainingSteps() == 0:
        print('You ran out of steps!')
        isQuit = True
    # check collisions pm versus ghosts:
    pm_pos = pm.getPosition()
    for g in ghosts:
        if checkCollision(pm_pos, g.getPosition()):
            isQuit = True
            print('You bumped into a ghost!')
    # check collisions pm versus food:
    eaten_dishes = []
    for dish in food:
        if checkCollision(pm_pos, dish.getPosition()):
            pm.setIsYum()
            dish.setIsEaten()
            eaten_dishes.append(dish)
            score += 1
    # Remove eaten dishes (cannot remove while iterating!):
    for dish in eaten_dishes:
        food.remove(dish)
    # Check if all food has been eaten already:
    if len(food) == 0:
        print('Congratulation, all food collected.')
        isQuit = True

    if phase == 7:
        phase = 0
    else:
        phase += 1
    if isQuit:
        # Game will terminate, put the "Game Over" image:
        game_over.setposition(0, -HEIGHT // 2 + 22)
        game_over.shape('img/game_over.gif')
        game_over.showturtle()
        # Trigger the shutdown handler function to be called in MS_TO_QUIT ms
        # from now:
        window.ontimer(shutDownHander, MS_TO_QUIT)
    else:
        # Trigger the next firing of our timer function, in 90ms from now:
        window.ontimer(periodicTimer, 90)


def RightKeyHandler():
    """Handler function for key-right events."""
    pm.turnEast()


def LeftKeyHandler():
    """Handler function for key-left events."""
    pm.turnWest()


def UpKeyHandler():
    """Handler function for key-up events."""
    pm.turnNorth()


def DownKeyHandler():
    """Handler function for key-down events."""
    pm.turnSouth()


def quitKeyHandler():
    """Handler function for the 'q' key."""
    global isQuit
    isQuit = True


def placeFood():
    """
    Compute doboggi screen positions and instantiate doboggi objects.
    Returns: a list of doboggi objects.
    """
    food = []
    Upper = True
    for i in range(0, FOODMAX):
        ok = False
        while not ok:  # loop until proper position was computed:
            r_x = random.randrange(-X_MAX + 20, X_MAX - 20)
            if Upper:
                # Position above the ghosts:
                r_y = random.randrange(160, Y_MAX)
            else:
                # Position below the ghosts:
                r_y = random.randrange(-Y_MAX, -40)
            new_pos = (r_x, r_y)
            HaveCollision = False
            for i in food:
                HaveCollision = HaveCollision \
                    or checkCollision(new_pos, i.getPosition())
            if not HaveCollision:
                food.append(doboggi(r_x, r_y))
                ok = True
        # Toggle between ``above'' and ``below" ghost's screen part:
        Upper = not Upper
    return food


#################
# Main program: #
#################

isQuit = False  # Set to true to initiate game termination.
score = 0
turtle.setup(WIDTH, HEIGHT)
window = turtle.Screen()
window.title('Doboggi-Man')
window.bgcolor('black')

turtle.register_shape('img/ghost_phase_0.gif')
turtle.register_shape('img/ghost_phase_1.gif')
turtle.register_shape('img/dbm_north_phase_0.gif')
turtle.register_shape('img/dbm_north_phase_1.gif')
turtle.register_shape('img/dbm_south_phase_0.gif')
turtle.register_shape('img/dbm_south_phase_1.gif')
turtle.register_shape('img/dbm_east_phase_0.gif')
turtle.register_shape('img/dbm_east_phase_1.gif')
turtle.register_shape('img/dbm_west_phase_0.gif')
turtle.register_shape('img/dbm_west_phase_1.gif')
turtle.register_shape('img/doboggi.gif')
turtle.register_shape('img/yum.gif')
turtle.register_shape('img/game_over.gif')
#
# Instantiate ghost objects:
#
ghosts.append(ghost('inky'))
ghosts.append(ghost('pinky', 120, 120))
#
# Comment-out the following line and uncomment the next line to
# use your auto-doboggi_man:
#
# pm = doboggi_man(120, -40)  # Instantiate doboggi_man object
pm = auto_doboggi_man(120, -40)  # Instantiate your auto_doboggi_man object
#
#
#
food += placeFood()
# Prepare the "game over" turtle already:
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.speed('fastest')
phase = 0
# Install the keyboard handlers:
window.onkey(RightKeyHandler, 'Right')
window.onkey(LeftKeyHandler, 'Left')
window.onkey(UpKeyHandler, 'Up')
window.onkey(DownKeyHandler, 'Down')
window.onkey(quitKeyHandler, 'q')
# Call periodic timer function for the first time.
# Subsequent calls will be triggered from inside
# this function, by setting up a timer:
periodicTimer()

window.listen()
window.mainloop()
