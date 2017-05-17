mypets = ['rat' , 'snake' , 'snale' , 'monkey']
print('if you want to add any pet to update the my pets list')
while True:
    name = input()
    if name == '':
        break
    mypets = mypets + [name]

print('mypets list' , mypets)

print('please give the keyword which you want to findout')
pet = input()
if pet in mypets:
    print('the given pet' , pet , 'is avalable')
else:
    print('pet is notavalabe')
    
