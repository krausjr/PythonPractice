#This file is for class practice.

g = 'global'
def outer(p='param'):
    l = 'local'
    print(g,p,l)

outer()

