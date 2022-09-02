#Name: Benjamin Kurland
#Email ID: tqf5au

from z3 import *
s = Solver()

#create grid
grid = [
        [Int(f'cell_{r}_{c}') for c in range(9)]
        for r in range (9)
        ]

#assert every num between 1 and 9 and only one num in every row
for r in range(9):
    for c in range(9):
        s.add(grid[r][c] >= 1, grid[r][c] <= 9)
    s.add(Distinct(grid[r]))

#assert only one num in every column
for c in range (9):
    s.add(Distinct( [grid[r][c] for r in range(9)] ))

#assert only one number in every box
for x in range(3):
    for y in range(3):
        s.add(Distinct({grid[x*3][y*3], 
                        grid[x*3][y*3+1], 
                        grid[x*3][y*3+2], 
                        grid[x*3+1][y*3], 
                        grid[x*3+1][y*3+1], 
                        grid[x*3+1][y*3+2], 
                        grid[x*3+2][y*3], 
                        grid[x*3+2][y*3+1], 
                        grid[x*3+2][y*3+2], } ))

puzzle = [
        '4..7.25..',
        '9...5....',
        '.214...98',
        '2....7...',
        '.6..2..4.',
        '...5....7',
        '83...615.',
        '....1...3',
        '..49.5..2'
        ]

#assert initial numbers on grid
for r in range(9):
    for c in range(9):
        n = puzzle[r][c]
        if n != '.':
            s.add(grid[r][c] == int (n))


s.check()
m = s.model()

#print formatting
for r in range(9):
    print(''.join( str(m.eval(grid[r][c])) for c in range(9) ))
    if r % 3 == 2:
        print('-' * 9) 


from z3 import *

# 9x9 matrix of integer variables
X = [[Int("x_%s_%s" % (i+1, j+1)) for j in range(9)]
    for i in range(9)]

# each cell contains a value in {1, ..., 9}
cells_c = [And(1 <= X[i][j], X[i][j] <= 9)
            for i in range(9) for j in range(9)]

# each row contains a digit at most once
rows_c = [Distinct(X[i]) for i in range(9)]

# each column contains a digit at most once
cols_c = [Distinct([X[i][j] for i in range(9)])
            for j in range(9)]

# each 3x3 square contains a digit at most once
sq_c = [Distinct([X[3*i0 + i][3*j0 + j]
                for i in range(3) for j in range(3)])
        for i0 in range(3) for j0 in range(3)]

sudoku_c = cells_c + rows_c + cols_c + sq_c

# sudoku instance, we use '0' for empty cells
instance = ((0, 0, 0, 0, 9, 4, 0, 3, 0),
            (0, 0, 0, 5, 1, 0, 0, 0, 7),
            (0, 8, 9, 0, 0, 0, 0, 4, 0),
            (0, 0, 0, 0, 0, 0, 2, 0, 8),
            (0, 6, 0, 2, 0, 1, 0, 5, 0),
            (1, 0, 2, 0, 0, 0, 0, 0, 0),
            (0, 7, 0, 0, 0, 0, 5, 2, 0),
            (9, 0, 0, 0, 6, 5, 0, 0, 0),
            (0, 4, 0, 9, 7, 0, 0, 0, 0))

instance_c = [If(instance[i][j] == 0,
                True,
                X[i][j] == instance[i][j])
            for i in range(9) for j in range(9)]

s = Solver()
s.add(sudoku_c + instance_c)
if s.check() == sat:
    m = s.model()
    r = [[m.evaluate(X[i][j]) for j in range(9)]
        for i in range(9)]
    print_matrix(r)
else:
    print("failed to solve")
