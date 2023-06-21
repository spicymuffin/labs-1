#
# This module contains global constants that are used throughout the game.
#

FOODMAX = 3
# Nr of dishes to eat

STEPMAX = 300
# Maximum number of steps until the game terminates.

WIDTH, HEIGHT = 500, 500
# Screen resolution

X_MAX = (WIDTH // 2) - (47 // 2)
Y_MAX = (HEIGHT // 2) - (47 // 2)
# Max coordinate values for pacman to prevent it from leaving the screen.

MS_TO_QUIT = 2000
# Milli-seconds from termination to removal of window.
# We give the user some time to read the "Game Over..." message.

FOOD = []
GHOSTS = []
