#!/usr/bin/env python3

#Import the needed libraries into the python script
from more_itertools import sliced
import os
import random
import sys


def roll(string):
	'''Does the action of generating the random number, correlating to rolling a die.'''
	array = string.split('d')
	val = 0
	for _ in range(int(array[0])):
		val += random.randint(1, int(array[1]))
	return val


def clear():
	'''Clears terminal display.'''
	os.system('cls' if os.name == 'nt' else 'clear')


def greeting():
    '''Creates the pop-up message at the top'''
    clear()
    message = "WELCOME TO D&D DICE ROLLER. MAY YOUR ROLLS BE EXCELLENT."
    print('='*(len(message)+4))
    print('= '+message+' =')
    print('='*(len(message)+4))
    print('\n\n')


def make_divide():
	'''Makes a visual break.'''
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if __name__ == "__main__":
	#Greets the user
	greeting()
	#Defines condition for the breaking of the menu loop
	answer = False
	#Initiates a basic menu for navigation.
	while not answer:
		#Visual niceness.
		greeting()
		make_divide()

		#Prompts the user for what kind of roll is going to occur.
		dice_roll = input("What would you like to roll?: ")
		#Makes it into a nice format for working with.
		die = dice_roll.split('d')
		#Calls the roll() function.
		rolled = roll(str(dice_roll))

		#Special roll conditions.
		if die[1] == "20" and rolled == 1:
			print('Critica Fail!!!')
		elif die[1] == "20" and rolled == 20:
			print("CRIT!!!")

		#Enters into adding the bonuses.
		else:
			#Prompts the user for a bonus.
			bonus = input('Bonuses? ')
			make_divide()
			bonus_list = list(sliced(bonus, 1))
			total_bonus = ""

			#Takes care of instances where bonus is larger than 9.
			for i in range(1,len(bonus_list)):
				total_bonus += bonus_list[i]
			net_roll = 0
			if bonus_list[0] == '+':
				net_roll = rolled + int(total_bonus)
			elif bonus_list[0] == '-':
				net_roll = rolled - int(total_bonus)
			elif bonus_list[0] == "0":
				net_roll = rolled
			else:
				#You can only add or subtract if you have a nonzero bonus.
				raise ValueError("Bonus operation undefined.")

			#Tells the user what the roll was.
			message = "You rolled {}.".format(net_roll)
			print("#"*len(message))
			print(message)
			print("#"*len(message))

		#Creates condition for repeating the menu.
		again = input("Would you like to roll again? (y/n)")
		if again == 'n':
			goodbye = "May your roads lead you to warm sands..."
			print("\n\n")
			print("-"*len(goodbye))
			print(goodbye)
			print("-"*len(goodbye))
			print("\n\n")
			answer = True
