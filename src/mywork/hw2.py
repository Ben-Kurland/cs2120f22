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
    # Counter example: I got a pizza or burger for lunch, and i did get a pizza, therefore i did not get a burger.
    # This doesnt make sense because there is no reason why I couldnt have gotten both pizza and burger.
    
    
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
    # If ~X is not true, then it must be that X is true.
    # I believe it is valid
    r5 = s.check()
    if (r5 == unsat):
        print("C5 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 6. ¬(X ∧ ¬X)
    # As a proposition in PL: ~(X /\ ~X)
    C6 = Not(And(X,Not(X)))
    s.add(Not(C6))
    # X /\ ~X is not true.
    # I believe it is valid
    r6 = s.check()
    if (r6 == unsat):
        print("C6 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 7. X ⊢ X ∨ Y
    # As a proposition in PL: X -> X \/ Y
    C7 = Implies(X,Or(X,Y))
    s.add(Not(C7))
    # If X is true, then it must be that X \/ Y is true.
    # I believe it is valid
    r7 = s.check()
    if (r7 == unsat):
        print("C7 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 8. Y ⊢ X ∨ Y
    # As a proposition in PL: Y -> X \/ Y
    C8 = Implies(Y,Or(X,Y))
    s.add(Not(C8))
    # If Y is true, then it must be that X \/ Y is true.
    # I believe it is valid
    r8 = s.check()
    if (r8 == unsat):
        print("C8 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 9. X → Y, ¬X ⊢ ¬ Y
    # As a proposition in PL: (X -> Y) /\ ~X -> ~Y
    C9 = Implies(And(Implies(X,Y),Not(X)),Not(Y))
    s.add(Not(C9))
    # If whenever X is true, Y is also true, and X is not true, then it must be that Y is not true.
    # I believe it's not valid
    r9 = s.check()
    if (r9 == unsat):
        print("C9 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    # Counter example: When its raining outside the ground must be wet, and it is not raining, therefore the gound is not wet.
    # This doesnt make sense because the ground could be wet for reasons other than rain.
    
    
    # 10. X → Y, Y → X ⊢ X ↔ Y
    # As a proposition in PL: (X -> Y) /\ (Y -> X) -> (X <-> Y)
    C10 = Implies(And(Implies(X,Y),Implies(Y,X)),X==Y)
    s.add(Not(C10))
    # If whenever X is true, Y is also true, and whenever Y is true, X is also true, then it must be that X is true if and only if Y is true.
    # I believe it is valid
    r10 = s.check()
    if (r10 == unsat):
        print("C10 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 11. X ↔ Y ⊢ X → Y
    # As a proposition in PL: (X <-> Y) -> (X -> Y)
    C11 = Implies(X==Y, Implies(X,Y))
    s.add(Not(C11))
    # If X is true if and only if Y is true, then it must be that whenever X is true, Y is also true.
    # I believe it is valid
    r11 = s.check()
    if (r11 == unsat):
        print("C11 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 12. X ↔ Y ⊢ Y → X
    # As a proposition in PL: (X <-> Y) -> (Y -> X)
    C12 = Implies(X==Y, Implies(Y,X))
    s.add(Not(C12))
    # If X is true if and only if Y is true, then it must be that whenever Y is true, X is also true.
    # I believe it is valid
    r12 = s.check()
    if (r12 == unsat):
        print("C12 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 13. X ∨ Y, X → Z, Y → Z ⊢ Z
    # As a proposition in PL: (X \/ Y) /\ (X -> Z) /\ (Y -> Z) -> Z
    C13 = Implies(And(Or(X,Y),Implies(X,Z),Implies(Y,Z)), Z)
    s.add(Not(C13))
    # If X \/ Y is true, and whenever X is true, Z is also true, and whenever Y is true, Z is also true, then it must be that Z is true.
    # I believe it is valid
    r13 = s.check()
    if (r13 == unsat):
        print("C13 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 14. X → Y, Y ⊢ X
    # As a proposition in PL: (X -> Y) /\ Y -> X
    C14 = Implies(And(Implies(X,Y),Y),X)
    s.add(Not(C14))
    # If whenever X is true, Y is also true, and Y is true, then it must be that X is true.
    # I believe it's not valid
    r14 = s.check()
    if (r14 == unsat):
        print("C14 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    # Counter example: When its raining outside the ground must be wet, and the ground is wet, therefore it is raining.
    # This doesnt make sense because the ground could be wet for reasons other than rain.
    
    
    # 15. X → Y, X ⊢ Y
    # As a proposition in PL: (X -> Y) /\ X -> Y
    C15 = Implies(And(Implies(X,Y),X),Y)
    s.add(Not(C15))
    # If whenever X is true, Y is also true, and X is true, then it must be that Y is true.
    # I believe it is valid
    r15 = s.check()
    if (r15 == unsat):
        print("C15 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 16. X → Y, Y → Z ⊢ X → Z
    # As a proposition in PL: (X -> Y) /\ (Y -> Z) -> (X -> Z)
    C16 = Implies(And(Implies(X,Y),Implies(Y,Z)),Implies(X,Z))
    s.add(Not(C16))
    # If whenever X is true, Y is also true, and whenever Y is true, Z is also true, then it must be that whenever X is true, Z is also true.
    # I believe it is valid
    r16 = s.check()
    if (r16 == unsat):
        print("C16 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 17. X → Y ⊢ Y → X 
    # As a proposition in PL: (X -> Y) -> (Y -> X)
    C17 = Implies(Implies(X,Y),Implies(Y,X))
    s.add(Not(C17))
    # If whenever X is true, Y is also true, then it must be that whenever Y is true, X is also true.
    # I believe it's not valid
    r17 = s.check()
    if (r17 == unsat):
        print("C17 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    # Counter example: When its raining outside the ground must be wet, therefore when the ground is wet outside it must be raining.
    # This doesnt make sense because the ground could be wet for reasons other than rain.
    
    
    # 18. X → Y ⊢ ¬Y → ¬X 
    # As a proposition in PL: (X -> Y) -> (~Y -> ~X)
    C18 = Implies(Implies(X,Y),Implies(Not(Y),Not(X)))
    s.add(Not(C18))
    # If whenever X is true, Y is also true, then it must be that whenever Y is not true, X is also not true.
    # I believe it is valid
    r18 = s.check()
    if (r18 == unsat):
        print("C18 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 19. ¬(X ∨ Y) ↔ ¬X ∧ ¬Y 
    # As a proposition in PL: ~(X \/ Y) <-> ~X /\ ~Y
    C19 = Not(Or(X,Y))==And(Not(X),Not(Y))
    s.add(Not(C19))
    # X \/ Y is not true if and only if X is not true and Y is not true.
    # I believe it is valid
    r19 = s.check()
    if (r19 == unsat):
        print("C19 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()
    
    
    # 20. ¬(X ∧ Y) ↔ ¬X ∨ ¬Y 
    # As a proposition in PL: ~(X /\ Y) <-> ~X \/ ~Y
    C20 = Not(And(X,Y))==Or(Not(X),Not(Y))
    s.add(Not(C20))
    # X /\ Y is not true if and only if X is not true or Y is not true.
    # I believe it is valid
    r20 = s.check()
    if (r20 == unsat):
        print("C20 is valid")
    else :
        print("Here's a counter-example: ", s.model())
    s.reset()


hw2()
