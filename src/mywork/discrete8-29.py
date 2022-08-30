#to get files from prof: git pull upstream main
#to view a markdown file as formatted: ctrl+shift+v
from z3 import *
x = Int('x')
y = Int('y')
print(simplify(x + y + 2*x + 3))
print(simplify(x < y + x + 2))
print(simplify(And(x + 1 >= 3, x**2 + x**2 + y**2 + 2 >= 5)))
x = Real('x')
y = Real('y')
solve(x**2 + y**2 > 3, x**3 + y < 5)


dog, cat, mouse = Ints('dog cat mouse')
solve(dog >= 1,
    cat >= 1,
    mouse >= 1,
    dog + cat + mouse == 100,
    1500 * dog + 100 * cat + 25 * mouse == 10000)