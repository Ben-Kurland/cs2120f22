from z3 import *

def hw2():
    X, Y, Z = Bools('X Y Z')
    
    s = Solver()
    
    # 1. X ∨ Y, X ⊢ ¬Y
    # As a proposition in PL: (X \/ Y) /\ X -> ~Y
    C1 = Implies(And(Or(X, Y),X),Not(Y))
    s.add(Not(C1))
    # If X \/ Y is true and X is true, then it must be that Y is not true.
    # I believe it's not valid
    r1 = s.check()
    if (r1 == unsat):
        print("C1 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    # Counter example: It is true that I got a pizza and burger for lunch. I needed to get a pizza or burger for lunch, and i did get a pizza, therefore i did not get a burger.
    # This doesnt make sense because there is no reason why i couldnt have gotten both
    
    
    # 2. X, Y ⊢ X ∧ Y
    # As a proposition in PL: (X) /\ (Y) -> (X /\ Y)
    C2 = Implies(And((X),(Y)),And(X,Y))
    s.add(Not(C2))
    # If X is true and Y is true, then it must be that X /\ Y is true.
    # I believe it is valid
    r2 = s.check()
    if (r2 == unsat):
        print("C2 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 3. X ∧ Y ⊢ X
    # As a proposition in PL: X /\ Y -> X
    C3 = Implies(And(X,Y),X)
    s.add(Not(C3))
    # If X /\ Y is true, then it must be that X is true.
    # I believe it is valid
    r3 = s.check()
    if (r3 == unsat):
        print("C3 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 4. X ∧ Y ⊢ Y
    # As a proposition in PL: X /\ Y -> Y
    C4 = Implies(And(X,Y),Y)
    s.add(Not(C4))
    # If X /\ Y is true, then it must be that Y is true.
    # I believe it is valid
    r4 = s.check()
    if (r4 == unsat):
        print("C4 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 5. ¬¬X ⊢ X
    # As a proposition in PL: ~(~X) -> X
    C5 = Implies(Not(Not(X)),X)
    s.add(Not(C5))
    # If not X is not true, then it must be that X is true.
    # I believe it is valid
    r5 = s.check()
    if (r5 == unsat):
        print("C5 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    


hw2()
