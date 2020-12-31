a = 500
def printlocalA():
    print('Local value of a=', a)

a = 100
print('Global value of a=', a)
printlocalA()
print('Global value of a=', a)
