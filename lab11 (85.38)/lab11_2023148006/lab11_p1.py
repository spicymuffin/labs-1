import time

# region constants
DEBUG = False  # set to False to get user input before simulation
FRAMERATE = 1  # framerate (one is boring but oh well)
SIZE = 20  # size of the 2D cellular automaton
INITIAL_WORLD_SIZE = 20  # size of the loaded world
INITAL_WORLD = """----------------------
| x                  | row 0
| x                  | row 1
| x                  | row 2
|                    | row 3
|                    | row 4
|                    | row 5
|                    | row 6
|                    | row 7
|                    | row 8
|                    | row 9
|          xxx       | row 10
|          x         | row 11
|          xxx       | row 12
|                    | row 13
|                    | row 14
|                    | row 15
|                    | row 16
|                    | row 17
|                    | row 18
|                    | row 19
----------------------"""

# calcualted constants
DELAY = round(1/FRAMERATE)  # calculate delay
WORLD = []  # world array (is 2D)
# endregion

# region funcs


def readVal(valType, requestMsg, errorMsg, default=None):
    """reads a value of type valType. makes a prompt and a default value can be set.

    Args:
        valType (type): type of value to be read
        requestMsg (str): prompt
        errorMsg (str): error message
        default (any, optional): default value. Defaults to None.

    Returns:
        valType: value
    """
    while True:  # request value until value
        val = input(requestMsg)
        if val == "" and default != None:
            return default
        try:
            val = valType(val)
            return val
        except ValueError:
            print(val, errorMsg)


def printSep():
    '''Print a separator'''
    for ctr in range(0, SIZE+2):
        print('-', end='')
    print('')


def printWorld(world):
    """prints world

    Args:
        world (list): world
    """
    printSep()

    for i in range(0, SIZE):
        line = []  # use list bc concatenating str is slow
        line.append('|')
        for j in range(0, SIZE):
            if world[i][j] == 0:
                line.append(' ')
            else:
                line.append('x')
        line.append('|')
        line.extend(" row " + str(i))
        print(''.join(line))
    printSep()


def loadWorld(world_str):
    """loads an output of this program as an world (list)

    Args:
        world_str (str): output to load

    Returns:
        list: loaded world
    """
    global INITIAL_WORLD_SIZE
    # loaded worlds are always of this size
    world_out = []
    for i in range(INITIAL_WORLD_SIZE):
        world_out.append([0]*INITIAL_WORLD_SIZE)  # created empty basically

    spl = world_str.split("\n")  # split by lines
    for i in range(1, INITIAL_WORLD_SIZE + 1):
        for j in range(1, INITIAL_WORLD_SIZE + 1):  # again, constant size
            if spl[i][j] == "x":
                world_out[i-1][j-1] = 1  # set living cells

    return world_out


def getLivingNeighbourCount(y, x, world, size):
    size -= 1  # zero indexed

    cnt = 0  # counter

    # set bounds
    bound_w_x = x - 1 if x > 0 else x  # west bound
    bound_e_x = x + 1 if x < size else x  # east bound
    bound_n_y = y - 1 if y > 0 else y  # north bound
    bound_s_y = y + 1 if y < size else y  # south bound

    # iterate through grid constrained by bounds
    for i in range(bound_n_y, bound_s_y + 1):
        for j in range(bound_w_x, bound_e_x + 1):
            # just add value since alive cells are represented as ones
            cnt += world[i][j]

    cnt -= world[y][x]  # self isnt neighbour

    return cnt
# endregion


# get input
if DEBUG == False:
    SIZE = readVal(int, "Grid sidelength (default 20): ",
                   "is an invalid value for this variable", default=20)  # get size

    # get max generation (weed out broken ints)
    MAX_GENERATION = readVal(int, "Max generation: ",
                             "is an invalid value for this variable")

    # get max generation (weed out invalid ints)
    while MAX_GENERATION <= 0:
        MAX_GENERATION = readVal(
            int, "Max generation: ", "is an invalid value for this variable")
else:
    SIZE = 30
    MAX_GENERATION = 100  # no output basically if set to -1
    DELAY = 1/60

# init world
for i in range(SIZE):
    WORLD.append([0]*SIZE)

# load world
LOADED_WORLD = loadWorld(INITAL_WORLD)
for i in range(len(LOADED_WORLD)):
    for j in range(len(LOADED_WORLD)):
        WORLD[i][j] = LOADED_WORLD[i][j]


# main updating loop:
for i in range(MAX_GENERATION + 1):
    # print world
    printWorld(WORLD)

    # init next generation
    NEXT_GENERATION = []
    for i in range(SIZE):
        NEXT_GENERATION.append([0]*SIZE)

    # update next generaion based on world
    for i in range(SIZE):
        for j in range(SIZE):
            n = getLivingNeighbourCount(
                i, j, WORLD, SIZE)  # get neighbour count
            NEXT_GENERATION[i][j] = WORLD[i][j]
            if n < 2:
                NEXT_GENERATION[i][j] = 0
            # is this even needed...? idk just gonna leave it as is
            if WORLD[i][j] == 1 and (n == 2 or n == 3):
                NEXT_GENERATION[i][j] = 1
            if n > 3:
                NEXT_GENERATION[i][j] = 0
            if WORLD[i][j] == 0 and n == 3:
                NEXT_GENERATION[i][j] = 1

    # prepare for next generation
    WORLD = NEXT_GENERATION

    time.sleep(DELAY)
