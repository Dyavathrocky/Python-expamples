#guessthe number

import random
secretnumber = random.randint(1, 20)
#print(secretnumber)
print('i am thinking the number between 1 to 20')

#ask player to take gueuss 6  times
for gussesTaken in range(1,7):
    print('take a secretnumber guess')
    guess = int(input())


    if guess < secretnumber :
        print('your guess is low compair to actual number')

    elif guess > secretnumber :
        print('your guess is high compair to actual number')

    else :
        break

if guess == secretnumber :
    print('cool you find the correcct number'  + str(gussesTaken) + 'guesses!')
    
else :
    print('youe unable to find the guess number in 6 attemps  , the corrcet number is ' + str(secretnumber))
 
