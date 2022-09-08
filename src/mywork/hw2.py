from z3 import *


def isValid(P):
    s = Solver()
    s.add(Not(P))  # replace True with required declarative spec
    return (s.check() == unsat)


# Declare X to be a Z3 Bool variable
X = Bool('X')
# Print the result of testing (X Or Not X) for validity
print(isValid(Or(X, Not(X))))
# Print the result of testing (X And Not X) for validity
print(isValid(And(X, Not(X))))



from z3 import *

def hw2():
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y
    # As a proposition in PL: (X \/ Y) /\ X -> ~Y
    C1 = Implies(And(Or(X, Y),X),Not(Y))
    s.add(Not(C1))
    # I believe it's not valid
    r = s.check()
    if (r == unsat):
        print("C1 is valid")
    else :
        print("Here's a counter-example: ", s.model)
        
    #

hw2()
