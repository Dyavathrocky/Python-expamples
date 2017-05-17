#local and global variables with the same name
def spam():
    eggs = 'spam local'
    print(eggs)   #prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs)    #prints 'baconlocal'
    spam()
    print(eggs)     #prints 'baconlocL'


eggs = 'global'
bacon()
print(eggs)     #prints 'global'
