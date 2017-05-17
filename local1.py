#local scopes cannot use variables in other local scopes
def spam () :
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
