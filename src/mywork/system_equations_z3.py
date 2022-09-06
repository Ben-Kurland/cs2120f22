from z3 import *

def system(a,b,c,d,e,f,g,h,i,j,k,l) :
    x = Real('x')
    y = Real('y')
    z = Real('z')
    s = Solver()
    s.add(a*x + b*y + c*z == d,)
    
    isSat = s.check()
    if (isSat == sat) :
        return s.model()
    return -1
    
print(system(   3, 2,  -1, 1,
                2, 2,   4,-2,
               -1, .5, -1, 0))