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
uuid: 143206060
"""
"""
random actions, total chaos
"""
board = gamma_new(4, 2, 4, 1)
assert board is not None


assert gamma_move(board, 1, 3, 1) == 1 
assert gamma_golden_move(board, 1, 0, 3) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_free_fields(board, 2) == 7 
assert gamma_move(board, 3, 1, 1) == 1 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_free_fields(board, 1) == 2 
assert gamma_move(board, 2, 3, 0) == 1 
assert gamma_move(board, 3, 0, 0) == 0 
assert gamma_move(board, 3, 2, 0) == 0 
assert gamma_golden_possible(board, 3) == 1 


board550079128 = gamma_board(board)
assert board550079128 is not None
assert board550079128 == (".3.1\n"
"...2\n")
del board550079128
board550079128 = None
assert gamma_move(board, 4, 0, 0) == 1 
assert gamma_move(board, 4, 2, 0) == 0 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 1, 0) == 1 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_move(board, 4, 0, 1) == 1 
assert gamma_move(board, 1, 1, 2) == 0 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_busy_fields(board, 1) == 1 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_move(board, 3, 2, 1) == 1 
assert gamma_move(board, 4, 3, 1) == 0 


gamma_delete(board)