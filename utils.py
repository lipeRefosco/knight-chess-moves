def generate_board(dimension = 8):
    board = []
    for n in range(dimension):
        previous = n * dimension
        board.append(range(previous, previous + dimension))
    return board

# board = generate_board()

# def move_up_left(position: tuple, board: list):
#     # move two to up and then one to left
#     return board[position[0] - 2][position[1] - 1]

def find_board_index(board, position):
    for k, line in enumerate(board):
        for i, value in enumerate(line):
            if position == value:
                return (k, i)

def sort_by_less_difference(list, sub):
    tmp = dict()

    for item in list:
        tmp[item - sub] = item

    tmp = sorted(tmp, key=True)
    
    print()
    print()
    print(tmp)
    print()
    print()
    
    return tmp