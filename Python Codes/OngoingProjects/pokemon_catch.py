import random
import numpy as np

def catch(pokemon_name, bcr, max_HP, current_HP, status = "", ball = "poke", wild = True):
    ##You can only catch wild pokemon
    if not wild:
        return False

    ##master balls have a 100% success rate
    if ball.lower() == "master":
        return True

    ##What ball are you using
    if ball == "poke":
        ball = 12
        N = random.randint(0, 255)
    elif ball == "great":
        ball = 8
        N = random.randint(0,200)
    else:
        ball = 12
        N = random.randint(0,150)

    ##Status effects
    if status.lower() == "asleep" or status.lower() == "frozen":
        S = 25
    elif status.lower() == "poisoned" or status.lower() == "burned" or status.lower() == "paralyzed":
        S = 12
    else:
        S = 0


    ##do the status effects have enough weight behind them?
    if (status.lower() == "asleep" or status.lower() == "frozen")and N < 25:
        return True
    elif (status.lower() == "poisoned" or status.lower() == "burned" or status.lower() == "paralyzed")and N < 12:
        return True
    ##If not
    else:
        ##random number - status > base catch rate?
        if (N - S) > bcr:
            return False
        else:
            ##generate new random number
            M = random.randint(0, 255)
            ##calculate f value
            f = round((max_HP * 255 * 4)/(current_HP * ball))
            ##make bounds for f value
            if f < 0:
                f = 0
            if f > 255:
                f = 255
            ##check to see if it was enough
            if f > M:
                return True
            else:
                return False


def simulate_catch(name, bcr, max_HP, current_HP, status, ball = "poke"):
    success = 0
    for i in range(1000):
        if catch(pokemon_name = name, max_HP = max_HP, current_HP = current_HP, bcr = bcr, status = status, ball = ball):
            success += 1
    return success/10
