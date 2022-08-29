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