#user name and password match
while True:
    print (' who are you ')
    print('enter user name')
    name = input()
    if name != 'joe' :
        continue
    print('hello , joe')
    print('what is the password')
    password = input ()
    if password == 'swordfish' :
        break
print('access granted.')
