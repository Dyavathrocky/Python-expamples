#birthday
birthdays = {'alice' : 'apr1' ,
             'rakesh': 'aug21' ,
             'carol' : 'mar4' ,
             'rajesh' : 'mar31' }

while True :
    print('enter a name: (blank to quit)')
    name = input()
    if name == '':
        break

    if name in birthdays :
        print(birthdays[name] + 'is the birthday of ' + name)
    else :
        print('i dont have information of the given ' + name)
        print('what is their birthday')
        bday = input()
        birthdays[name] = bday
        print('birthday data base updated .')
        
             
