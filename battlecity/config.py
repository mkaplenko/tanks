import os

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(PROJECT_DIR, 'data')
IMG_DIR = os.path.join(DATA_DIR, 'img')

# Images
# PLAYER 1 (GREEN TANK)
PLAYER1_IMG_UP = os.path.join(IMG_DIR, 'p1-little-up.bmp')
PLAYER1_IMG_DOWN = os.path.join(IMG_DIR, 'p1-little-down.bmp')
PLAYER1_IMG_LEFT = os.path.join(IMG_DIR, 'p1-little-left.bmp')
PLAYER1_IMG_RIGHT = os.path.join(IMG_DIR, 'p1-little-right.bmp')

# WALL
WALL_IMG = os.path.join(IMG_DIR, 'wall.bmp')
