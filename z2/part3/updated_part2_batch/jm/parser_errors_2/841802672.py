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
uuid: 841802672
"""
"""
random actions, total chaos
"""
board = gamma_new(2, 5, 3, 1)
assert board is not None


assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 1, 0, 4) == 1 
assert gamma_move(board, 2, 0, 1) == 1 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 3, 2, 0) == 0 
assert gamma_move(board, 3, 0, 2) == 1 
assert gamma_golden_move(board, 3, 1, 0) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_move(board, 1, 1, 4) == 1 


board203723783 = gamma_board(board)
assert board203723783 is not None
assert board203723783 == ("11\n"
"..\n"
"3.\n"
"2.\n"
"..\n")
del board203723783
board203723783 = None
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 3, 0) == 0 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_move(board, 1, 1, 4) == 0 
assert gamma_free_fields(board, 1) == 2 
assert gamma_move(board, 2, 1, 4) == 0 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_free_fields(board, 1) == 2 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_busy_fields(board, 2) == 2 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 1, 1, 4) == 0 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 3, 2, 1) == 0 
assert gamma_move(board, 3, 0, 3) == 1 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_move(board, 1, 0, 4) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 2, 1, 0) == 1 


gamma_delete(board)
