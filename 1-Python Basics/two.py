import one

def myfun2():

    print('myfun2() in two.py is being run')

print('top-level 2 fun in two.py')

if __name__=="__main__":
    print('two.py is being run directly')
else:
    print('two.py is imported into another module')