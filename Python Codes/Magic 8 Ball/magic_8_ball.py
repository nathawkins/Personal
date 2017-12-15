#!/usr/bin/env python3
import os
import random

## Functions
def clear():
    '''Clear the terminal window.'''
    os.system('cls' if os.name == 'nt' else 'clear')

def greeting():
    '''Creates the pop-up message at the top'''
    clear()
    message = "Shake the magic 8 ball and get the answers you seek!"
    print('='*(len(message)+4))
    print('= '+message+' =')
    print('='*(len(message)+4))
    print('\n\n')

## Application Body
greeting()
if input("Ask your question and type `shake`, then hit `return`..."):
    complete = 0
    while complete == 0:
        greeting()
        responses = ["It is certain","It is decidedly so",'Without a doubt','Yes definitely','You may rely on it','As I see it, yes','Most likely','Outlook good','Yes','Signs point to yes','Reply hazy, try again','Ask again later','Better not tell you now','Cannot predict now','Concentrate harder and ask again',"Don't count on it",'My reply is no','My sources say no','Outlook not so good','Very doubtful']
        shake = random.randint(0,len(responses)-1)
        print(responses[shake])
        if input("Do you seek more answers? [y/n]") == 'n':
            goodbye = "May your roads lead you to warm sands..."
            print('-'*len(goodbye))
            print(goodbye)
            print('-'*len(goodbye))
            print('\n\n')
            complete = 1
