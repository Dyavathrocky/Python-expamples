#random randidt function

import random

def getanswer(answernumber) :
    if answernumber == 1:
        return 'it is certain'
    elif answernumber == 2 :
        return 'it is decided'
    elif answernumber == 3 :
        return 'yes'
    elif answernumber == 4 :
        return 'replay hazy try again'
    elif answernumber == 5 :
        return 'ask agaun later'
    elif answernumber == 6 :
        return 'concentrate and ask again'
    elif answernumber == 7 :
        return 'my replay is no '
    elif answernumber == 8 :
        return 'outlook not so good '
    elif answernumber ==  9 :
        return 'very doubtful'

#r = random.randint(1,9)
#fortune = getanswer(r)
#print(fortune)

print(getanswer(random.randint(1,9)))
