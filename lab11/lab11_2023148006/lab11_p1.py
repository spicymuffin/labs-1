import time

SIZE = 20  # size of the 2D cellular automaton
FRAMERATE = 60

DELAY = 1/FRAMERATE
LOADED_WORLD_SIZE = 20

WORLD = []
INITAL_WORLD = """----------------------
| x                 x| row 0
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

    line = []  # use list bc concatenating str is slow
    line.append("|")
    for i in range(0, SIZE):
        for j in range(0, SIZE):
            pass


def loadWorld(world_str):
    global LOADED_WORLD_SIZE
    # loaded worlds are always of this size
    world_out = []
    for i in range(LOADED_WORLD_SIZE):
        world_out.append([0]*LOADED_WORLD_SIZE)

    spl = world_str.split("\n")
    for i in range(1, LOADED_WORLD_SIZE + 1):
        for j in range(1, LOADED_WORLD_SIZE + 1):  # again, constant size
            print(i, j)
            if spl[i][j] == "x":
                print("t", i, j)
                world_out[i-1][j-1] = 1
                print(id(world_out[i]), id(world_out[i+1]))

    print(world_out)
    return world_out

#
# Main program
#


SIZE = readVal(int, "Grid sidelength (default 20): ",
               "is an invalid integer", default=20)
MAX_GENERATION = readVal(int, "Max generation: ", "is an invalid integer")
while MAX_GENERATION <= 0:
    MAX_GENERATION = readVal(int, "Max generation: ", "is an invalid integer")

WORLD = [[0]*SIZE]*SIZE
LOADED_WORLD = loadWorld(INITAL_WORLD)

for i in range(len(LOADED_WORLD)):
    for j in range(len(LOADED_WORLD)):
        WORLD[i][j] = LOADED_WORLD[i][j]

# print(WORLD)

# Compute:
for i in range(MAX_GENERATION + 1):
    printWorld(WORLD)
    time.sleep(DELAY)
