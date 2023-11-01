from time import sleep
from knight import knight

def solution(src, dest, total_moves = 0, memo = dict()):
    if src == dest:
        return total_moves
    
    total_moves += 1
    print('src:', src, 'dest:', dest)
    if not src in memo.keys():
        src_moves = list()
        src_moves.append(knight.move_up_left(src))
        src_moves.append(knight.move_up_right(src))
        src_moves.append(knight.move_left_up(src))
        src_moves.append(knight.move_right_up(src))
        src_moves.append(knight.move_down_left(src))
        src_moves.append(knight.move_down_right(src))
        src_moves.append(knight.move_left_down(src))
        src_moves.append(knight.move_right_down(src))
        print(src_moves)
        memo[src] = sorted(src_moves, key=lambda x: abs(dest - x) if dest - x >= 0 else 0)

    src_moves = memo[src]
    print(src_moves)
    sleep(.3)
    # for move in src_moves:
    if not dest == src_moves[0]:
        return solution(src_moves[0], dest, total_moves, memo)

    return total_moves

    
# def solution(src, dest):
#     # pegar a posicao do src na matriz
#     index_src = find_board_index(board, src)
#     print(board[index_src[0]][index_src[1]])