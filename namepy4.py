#same name
def spam():
    print(eggs) #error!
    eggs = 'spam local'
    #print(eggs)


eggs = 'global'
spam()
