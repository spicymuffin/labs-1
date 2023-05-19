import time

# region constants
DEBUG = True
FRAMERATE = 60
SIZE = 20  # size of the 2D cellular automaton
LOADED_WORLD_SIZE = 20
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
DELAY = 1/FRAMERATE
WORLD = []
# endregion

# region funcs


def readVal(valType, requestMsg, errorMsg, default=None):
    while True:
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
    '''
    Print one generation.
    Must use printSep() above to print the separators.
    '''
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
        line.extend("row " + str(i))
        print(''.join(line))
    printSep()


def loadWorld(world_str):
    global LOADED_WORLD_SIZE
    # loaded worlds are always of this size
    world_out = []
    for i in range(LOADED_WORLD_SIZE):
        world_out.append([0]*LOADED_WORLD_SIZE)

    spl = world_str.split("\n")
    for i in range(1, LOADED_WORLD_SIZE + 1):
        for j in range(1, LOADED_WORLD_SIZE + 1):  # again, constant size
            if spl[i][j] == "x":
                world_out[i-1][j-1] = 1

    return world_out


def getLiveNeighbourCount(y, x, world, size):
    size -= 1  # zero indexed

    cnt = 0  # counter

    bound_w_x = x - 1 if x > 0 else x
    bound_e_x = x + 1 if x < size else x
    bound_n_y = y - 1 if y > 0 else y
    bound_s_y = y + 1 if y < size else y

    for i in range(bound_n_y, bound_s_y + 1):
        for j in range(bound_w_x, bound_e_x + 1):
            cnt += world[i][j]
            print(i, j)

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
    SIZE = 20
    MAX_GENERATION = -1  # no output basically

# init world
for i in range(SIZE):
    WORLD.append([0]*SIZE)

# load world
LOADED_WORLD = loadWorld(INITAL_WORLD)
for i in range(len(LOADED_WORLD)):
    for j in range(len(LOADED_WORLD)):
        WORLD[i][j] = LOADED_WORLD[i][j]


print(getLiveNeighbourCount(0, 19, WORLD, 20))

# main updating loop:
for i in range(MAX_GENERATION + 1):
    printWorld(WORLD)
    # update world
    time.sleep(DELAY)
