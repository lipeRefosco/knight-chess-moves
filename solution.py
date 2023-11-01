from time import sleep
from knight import knight

def solution(src, dest):
    if src == dest:
        return 0

    total_moves = 0
    position = 0
    moves = dict()

    moves[0] = knight.move_down_right
    moves[1] = knight.move_right_up
    moves[2] = knight.move_left_up
    while not position == dest:
        # print('while')
        for move in moves:
            # print('for')
            # sleep(.1)
            total_moves += 1

            position = moves[move](src)
            # print(position)
            if position < 0 or position > 63:
                continue
            
            if position == dest:
                break

            src = position

    return total_moves
    
# def solution(src, dest):
#     # pegar a posicao do src na matriz
#     index_src = find_board_index(board, src)
#     print(board[index_src[0]][index_src[1]])