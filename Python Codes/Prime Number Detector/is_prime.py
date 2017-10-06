import numpy as np

def is_prime(number):
    is_prime = False
    
    if number == 1:
        is_prime = False
    elif number == 2:
        is_prime = True
    elif number == 3:
        is_prime = True
    elif (number%2 == 0) or (number%3 == 0):
        is_prime = False
    else:
        x = number**(1/2)
        
        if number%x == 0:
            is_prime = False
        else:
            test = np.arange(2, x, 1)
            
            failure = [i for i in test if number%i==0]
        
            if len(failure) != 0:
                is_prime = False
            else:
                is_prime = True
    #print("The number {} is prime: {}".format(number, is_prime))
    return is_prime

#print(len([i for i in range(1,100000) if is_prime(i) == True]))