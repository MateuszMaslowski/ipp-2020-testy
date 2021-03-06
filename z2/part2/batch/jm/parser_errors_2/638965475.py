from part1 import (
    gamma_board,
    gamma_busy_fields,
    gamma_delete,
    gamma_free_fields,
    gamma_golden_move,
    gamma_golden_possible,
    gamma_move,
    gamma_new,
)

"""
scenario: test_random_actions
uuid: 638965475
"""
"""
random actions, total chaos
"""
board = gamma_new(4, 2, 4, 1)
assert board is not None


assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_busy_fields(board, 1) == 1 
assert gamma_free_fields(board, 1) == 2 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_busy_fields(board, 2) == 1 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_move(board, 4, 3, 1) == 1 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_free_fields(board, 3) == 0 
assert gamma_move(board, 4, 2, 1) == 1 
assert gamma_golden_move(board, 4, 0, 0) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_busy_fields(board, 1) == 1 
assert gamma_golden_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 0 


board257599198 = gamma_board(board)
assert board257599198 is not None
assert board257599198 == ("3244\n"
"1...\n")
del board257599198
board257599198 = None
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_move(board, 4, 0, 2) == 0 
assert gamma_golden_possible(board, 4) == 1 


gamma_delete(board)
