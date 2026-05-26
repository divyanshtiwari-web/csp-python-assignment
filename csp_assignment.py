from itertools import permutations

# -------------------------------
# 1. Australia Map Coloring
# -------------------------------

def australia_map():
    regions = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

    neighbors = {
        'WA': ['NT', 'SA'],
        'NT': ['WA', 'SA', 'Q'],
        'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
        'Q': ['NT', 'SA', 'NSW'],
        'NSW': ['Q', 'SA', 'V'],
        'V': ['SA', 'NSW'],
        'T': []
    }

    colors = ['Red', 'Green', 'Blue']

    def is_valid(region, color, assignment):
        for n in neighbors.get(region, []):
            if n in assignment and assignment[n] == color:
                return False
        return True

    def backtrack(assignment):
        if len(assignment) == len(regions):
            return assignment

        unassigned = [r for r in regions if r not in assignment][0]

        for color in colors:
            if is_valid(unassigned, color, assignment):
                assignment[unassigned] = color
                result = backtrack(assignment)
                if result:
                    return result
                del assignment[unassigned]

        return None

    solution = backtrack({})
    print("\nAustralia Map Coloring:")
    print(solution)


# -------------------------------
# 2. Telangana Map Coloring (33 districts)
# -------------------------------

def telangana_map():
    regions = [
        'Adilabad','Bhadradri','Hyderabad','Jagtial','Jangaon','Jayashankar',
        'Jogulamba','Kamareddy','Karimnagar','Khammam','Komaram Bheem',
        'Mahabubabad','Mahabubnagar','Mancherial','Medak','Medchal',
        'Mulugu','Nagarkurnool','Nalgonda','Narayanpet','Nirmal',
        'Nizamabad','Peddapalli','Rajanna','Rangareddy','Sangareddy',
        'Siddipet','Suryapet','Vikarabad','Wanaparthy','Warangal Rural',
        'Warangal Urban','Yadadri'
    ]

    neighbors = {
        'Hyderabad': ['Rangareddy','Medchal'],
        'Rangareddy': ['Hyderabad','Vikarabad','Mahabubnagar','Medchal'],
        'Medchal': ['Hyderabad','Rangareddy','Sangareddy'],
        'Sangareddy': ['Medchal','Medak','Vikarabad'],
        'Medak': ['Sangareddy','Siddipet'],
        'Siddipet': ['Medak','Karimnagar'],
        'Karimnagar': ['Siddipet','Jagtial','Peddapalli'],
        'Jagtial': ['Karimnagar','Nizamabad'],
        'Nizamabad': ['Jagtial','Kamareddy','Nirmal'],
        'Kamareddy': ['Nizamabad','Medak'],
        'Nirmal': ['Nizamabad','Adilabad'],
        'Adilabad': ['Nirmal','Komaram Bheem'],
        'Komaram Bheem': ['Adilabad','Mancherial'],
        'Mancherial': ['Komaram Bheem','Peddapalli'],
        'Peddapalli': ['Mancherial','Karimnagar'],
        'Warangal Urban': ['Warangal Rural','Jangaon'],
        'Warangal Rural': ['Warangal Urban','Mulugu'],
        'Mulugu': ['Warangal Rural','Jayashankar'],
        'Jayashankar': ['Mulugu','Bhadradri'],
        'Bhadradri': ['Jayashankar','Khammam'],
        'Khammam': ['Bhadradri','Suryapet'],
        'Suryapet': ['Khammam','Nalgonda'],
        'Nalgonda': ['Suryapet','Yadadri'],
        'Yadadri': ['Nalgonda','Jangaon'],
        'Jangaon': ['Yadadri','Warangal Urban'],
        'Mahabubnagar': ['Rangareddy','Nagarkurnool'],
        'Nagarkurnool': ['Mahabubnagar','Wanaparthy'],
        'Wanaparthy': ['Nagarkurnool','Jogulamba'],
        'Jogulamba': ['Wanaparthy','Narayanpet'],
        'Narayanpet': ['Jogulamba','Vikarabad'],
        'Vikarabad': ['Narayanpet','Rangareddy','Sangareddy'],
        'Rajanna': ['Karimnagar'],
        'Mahabubabad': ['Warangal Rural'],
    }

    colors = ['Red','Green','Blue','Yellow']

    def is_valid(region, color, assignment):
        for n in neighbors.get(region, []):
            if n in assignment and assignment[n] == color:
                return False
        return True

    def backtrack(assignment):
        if len(assignment) == len(regions):
            return assignment

        unassigned = [r for r in regions if r not in assignment][0]

        for color in colors:
            if is_valid(unassigned, color, assignment):
                assignment[unassigned] = color
                result = backtrack(assignment)
                if result:
                    return result
                del assignment[unassigned]

        return None

    solution = backtrack({})
    print("\nTelangana Map Coloring (33 Districts):")
    print(solution)


# -------------------------------
# 3. Sudoku Solver
# -------------------------------

def sudoku_solver():
    board = [
        [5,3,0,0,7,0,0,0,0],
        {6,0,0,1,9,5,0,0,0},
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]

    # Quick manual fix for formatting typo inherited from raw source text dictionary character
    board[1] = [6,0,0,1,9,5,0,0,0]

    def is_valid(board, row, col, num):
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        start_row, start_col = row - row % 3, col - col % 3

        for i in range(3):
            for j in range(3):
                if board[start_row+i][start_col+j] == num:
                    return False

        return True

    def solve(board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(board, row, col, num):
                            board[row][col] = num
                            if solve(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve(board)

    print("\nSolved Sudoku:")
    for row in board:
        print(row)


# -------------------------------
# 4. Crypt Arithmetic
# -------------------------------

def crypt_arithmetic():
    letters = 'SENDMORY'
    digits = range(10)

    for p in permutations(digits, len(letters)):
        d = dict(zip(letters, p))

        if d['S'] == 0 or d['M'] == 0:
            continue

        send = d['S']*1000 + d['E']*100 + d['N']*10 + d['D']
        more = d['M']*1000 + d['O']*100 + d['R']*10 + d['E']
        money = d['M']*10000 + d['O']*1000 + d['N']*100 + d['E']*10 + d['Y']

        if send + more == money:
            print("\nCrypt Arithmetic Solution:")
            print(d)
            break


# -------------------------------
# MAIN
# -------------------------------

if __name__ == "__main__":
    australia_map()
    telangana_map()
    sudoku_solver()
    crypt_arithmetic()
