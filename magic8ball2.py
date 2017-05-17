#magic 8 ball using list 
import random

messages = ['it is certain' ,
            'its decidely so' ,
            'yes definatly',
            'replay hazy try agin',
            'ask again later' ,
            'concentrate and ask again later' ,
            'my reply is no',
            'outlook not so good',
            'very doubtful']
print(messages[random.randint(0,len(messages) - 1)])
