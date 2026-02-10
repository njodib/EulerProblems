import requests

def solveSudoku(board):
    # row(r) is 9 bits. The nth bit (from right) is 1 if n in row r
    rows = [0]*9
    # col(c) is 9 bits. The nth bit (from right) is 1 if n in col c
    cols = [0]*9
    # box(b) is 9 bits. The nth bit (from right) is 1 if n in box b
    boxs = [0]*9
    # empty cells are tuple (row,col)
    empty_cells = []
    # optimization: precalculate box value
    box_idx = [[(r // 3) * 3 + (c // 3) for c in range(9)] for r in range(9)]

    # Initalize masks and empty cells
    for r in range(9):
        for c in range(9):
            b = 3*(r//3)+c//3
            if board[r][c]=='0':
                empty_cells.append((r,c))
            else:
                m = 1<<(ord(board[r][c])-ord('1'))
                rows[r] |= m
                cols[c] |= m
                boxs[b] |= m

    def back():
        # Base: All empty cells filled
        if not empty_cells: return True

        # Pick the cell with the fewest candidates
        min_candidates = 10
        best_mask = 0
        best_idx = -1
        for i in range(len(empty_cells)):
            r,c = empty_cells[i]
            # set mask as 1 for available bit
            mask = 0x1ff & ~(rows[r] | cols[c] | boxs[box_idx[r][c]])
            candidates = mask.bit_count()
            if candidates == 0: return False
            if candidates < min_candidates:
                min_candidates = candidates
                best_mask = mask
                best_idx = i
            if candidates == 1: break 

        # get r,c,b from best empty cell. remove efficiently
        r, c = empty_cells[best_idx]
        empty_cells[best_idx], empty_cells[-1] = empty_cells[-1], empty_cells[best_idx]
        last_cell = empty_cells.pop()
        b = box_idx[r][c]
        
        #for val in range(9): # Try numbers 1-9 (indexed 0-8)
        temp_mask = best_mask
        while temp_mask:
            m = temp_mask & -temp_mask
            val=m.bit_length()
        
            # Make choice
            board[r][c] = str(val)
            rows[r] |= m
            cols[c] |= m
            boxs[b] |= m

            # Explore next cell
            if back(): return True
            
            # BACKTRACK: Undo choice
            rows[r] ^= m
            cols[c] ^= m
            boxs[b] ^= m
            temp_mask ^= m
        
        # add r,c,b to empty cell if no choices are valid
        empty_cells.append(last_cell)
        empty_cells[best_idx], empty_cells[-1] = empty_cells[-1], empty_cells[best_idx]
        return False
    
    # initial call for backtracking
    back()

# read file
file_url = 'https://projecteuler.net/resources/documents/0096_sudoku.txt'
lines = requests.get(file_url).text.splitlines()

# initialize board and topleft sum
board = []
s = 0

# create board
for line in lines:
    if "Grid" in line: continue
    board.append([digit for digit in line])

    # when board is full: solve, add 3 top-left digits to sum, and reset
    if len(board) == 9:
        solveSudoku(board)
        s += int(board[0][0])*100 + int(board[0][1])*10 + int(board[0][2])
        board = []

# output total sum
print(s)