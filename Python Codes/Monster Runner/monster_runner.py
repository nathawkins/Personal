import numpy as np
import os
import random
import copy

def clear():
    '''Clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')

clear()
print("**** MONSTER MASH ****")
print("Escape the maze by getting to the X, but be careful, there's a monster looking for you...")
print("X marks your escape, you're standing on @.")

##Create the Board
shape = 12
game_board = np.zeros((shape, shape))

##X marks the spot for where to get out
end_location = [random.randint(0,shape-1), random.randint(0,shape-1)]
game_board[end_location[0]][end_location[1]] = 1

##Create starting position for the player
class Player():
    def __init__(self):
        self.position = [0,0]
        self.win = False
        self.eaten = False

    def redraw(self):
        game_board[self.position[0]][self.position[1]] = 2
        tile = "| {} |"
        string_board = str(game_board).replace(' ','').replace('.','').replace('[','').replace(']','')
        string_board = string_board.replace("0", tile.format("_"))
        string_board = string_board.replace("1", tile.format("X"))
        string_board = string_board.replace("2", tile.format("@"))
        print(string_board)

    def check_win(self):
        if self.position == end_location:
            self.win = True

    def check_monster(self):
        if self.position == monster:
            self.eaten = True

    def check(self):
        if self.win and not self.eaten:
            clear()
            print("Congratulations!! You escaped with your life!")
        if self.eaten and not self.win:
            clear()
            print("Oh no! The Monster got you!!!")
        if self.win and self.eaten:
            clear()
            print("The monster snagged you just as you went to escape. You lose.")


    def move_right(self):
        if self.position[1] + 1 < game_board.shape[1]:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[1] += 1
            self.check_monster()
            self.check_win()
            self.check()
            self.redraw()
        else:
            print("Walls are hard, try going a different way!")

    def move_up(self):
        if self.position[0] - 1 >= 0:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[0] -= 1
            self.check_monster()
            self.check_win()
            self.check()
            self.redraw()
        else:
            print("Walls are hard, try going a different way!")

    def move_down(self):
        if self.position[0] + 1 < game_board.shape[1]:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[0] += 1
            self.check_monster()
            self.check_win()
            self.check()
            self.redraw()
        else:
            print("Walls are hard, try going a different way!")

    def move_left(self):
        if self.position[1] - 1 >= 0:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[1] -= 1
            self.check_monster()
            self.check_win()
            self.check()
            self.redraw()
        else:
            print("Walls are hard, try going a different way!")

class Monster():
    def __init__(self):
        self.position = [random.randint(0,shape-1), random.randint(0,shape-1)]

    def move_right(self):
        if self.position[1] + 1 < game_board.shape[1]:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[1] += 1
        else:
            self.move_left()

    def move_up(self):
        if self.position[0] - 1 >= 0:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[0] -= 1
        else:
            self.move_down()

    def move_down(self):
        if self.position[0] + 1 < game_board.shape[1]:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[0] += 1
        else:
            self.move_up()

    def move_left(self):
        if self.position[1] - 1 >= 0:
            game_board[self.position[0]][self.position[1]] = 0
            self.position[1] -= 1
        else:
            self.move_right()

    def chase(self):
        monster_move = random.randint(1,4)
        if monster_move == 1:
            self.move_up()

        if monster_move == 2:
            self.move_down()

        if monster_move == 3:
            self.move_left()

        if monster_move == 4:
            self.move_right()




Player = Player()
Monster = Monster()
Player.redraw()

while (Player.win == False) and (Player.eaten == False):
    move = input("What's your move? up/left/right/down ").lower()
    clear()
    monster = Monster.position
    if move == "up":
        Player.move_up()

    if move == "down":
        Player.move_down()

    if move == "left":
        Player.move_left()

    if move == "right":
        Player.move_right()
