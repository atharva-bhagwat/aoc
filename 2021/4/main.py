import sys
from collections import Counter
# sys.argv[1]
with open(sys.argv[1],'r') as f:
    input = [int(x) for x in f.readline().strip().split(',')]
    remaining = f.read().strip().split('\n\n')

# '2021/4/sample.txt'
# with open('2021/4/sample.txt','r') as f:
#     input = [int(x) for x in f.readline().strip().split(',')]
#     remaining = f.read().strip().split('\n\n')

all_boards = []
for entry in remaining:
    board = []
    for row_str in entry.split('\n'):
        row = []
        for x in row_str.split(' '):
            if x.isdigit():
                row.append(int(x))
        board.append(row)
    all_boards.append(board)

# Part 1
nrow = ncol = 5

def mark(val, board):
    for row in board:
        for col in range(ncol):
            if row[col] == val:
                row[col] = 'x'

def calc_sum(board):
    sum = 0
    for row in board:
        for val in row:
            if val != 'x':
                sum += val
    return sum

def check(board):
    # vertical
    for col in range(ncol):
        winner = all(elem in ['x'] for elem in [row[col] for row in board])

        if winner:
            return winner

    # horizontal
    for row in board:
        winner = all(elem in ['x'] for elem in row)

        if winner:
            return winner

    return False

def part1():
    boards = all_boards
    for val in input:
        for board in boards:
            mark(val, board)

            if check(board):
                return calc_sum(board) * val

def part2():
    boards = all_boards
    board_status = [1] * len(all_boards)
    one_remaining = False
    for val in input:
        if Counter(board_status)[1] == 1:
            one_remaining = True
        for itr, flag in enumerate(board_status):
            if flag:
                cur_board = boards[itr]

                mark(val, cur_board)

                if check(cur_board):
                    if one_remaining:
                        return calc_sum(cur_board) * val
                    board_status[itr] = 0

print(f'Part 1: {part1()}')
print(f'Part 2: {part2()}')