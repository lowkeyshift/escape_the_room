import random

CELLS = [(0,0),(0,1),(0,2),
         (1,0),(1,1),(1,2)
         (2,0),(2,1),(2,2)]

def get_location():
    # monster = random
    # door = random
    # start = random

    # if monster, door, or start are the same, do it again

    # return monster, door, start 

def move_player(player, move):
    # Get the player's current location
    # If move is LEFT, y -1
    # If move is Right, y + 1
    # If move is UP, x -1
    # If move is DOWN, x+1
    return player

def get_moves(player):
    MOVES = ['LEFT','RIGHT','UP','DOWN']
    # If players y is 0, remove LEFT
    # If players x is 0, remove UP
    # If players y is 2, remove RIGHT
    # If players x is 2, remove DOWN
    return MOVES

while True:
    print("Welcome to the dungeon!")
    print("Your're currently in room {}") # fill in with player position
    print("You can move {}") # fill in with available moves
    print("Enter QUIT to quit.")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break

    # if its a good move, change the player's position
    # if its a bad move, don't change the anything
    # if the new player position is the door, they win!
    # if the new player position is the monster, they lose!
    # Otherwise, continue
