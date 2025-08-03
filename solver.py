import random

def generate_scramble(n=20):
    moves = ['U', "U'", 'D', "D'", 'L', "L'", 'R', "R'", 'F', "F'", 'B', "B'"]
    scramble = []
    prev = ''
    for _ in range(n):
        move = random.choice(moves)
        while move[0] == prev:
            move = random.choice(moves)
        scramble.append(move)
        prev = move[0]
    return scramble

def solve_white_cross(cube):
    return ["F", "U", "R", "U'"]

def solve_f2l(cube):
    return ["R", "U", "R'", "U'", "F'", "U'", "F"]

def solve_oll(cube):
    return ["F", "R", "U", "R'", "U'", "F'"]

def solve_pll(cube):
    return ["R'", "F", "R'", "B2", "R", "F'", "R'", "B2", "R2"]

def solve_cube(cube):
    solution = []
    for func in [solve_white_cross, solve_f2l, solve_oll, solve_pll]:
        moves = func(cube)
        for move in moves:
            cube.apply_move(move)
        solution.extend(moves)
    return solution