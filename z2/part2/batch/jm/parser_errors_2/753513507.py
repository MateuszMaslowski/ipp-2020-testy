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
uuid: 753513507
"""
"""
random actions, total chaos
"""
board = gamma_new(4, 4, 2, 8)
assert board is not None


assert gamma_move(board, 1, 0, 2) == 1 
assert gamma_move(board, 1, 2, 1) == 1 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_move(board, 1, 3, 1) == 1 
assert gamma_move(board, 1, 0, 3) == 1 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 1, 2, 3) == 1 
assert gamma_move(board, 1, 1, 2) == 1 
assert gamma_move(board, 2, 0, 1) == 1 
assert gamma_move(board, 2, 3, 0) == 1 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 1, 1, 3) == 1 
assert gamma_free_fields(board, 1) == 6 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 1, 1) == 1 


board520860589 = gamma_board(board)
assert board520860589 is not None
assert board520860589 == ("111.\n"
"11..\n"
"2211\n"
"2..2\n")
del board520860589
board520860589 = None
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_busy_fields(board, 1) == 7 
assert gamma_move(board, 2, 2, 2) == 1 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 1, 3, 2) == 1 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 2, 3, 3) == 1 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_busy_fields(board, 1) == 8 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 1, 3, 2) == 0 
assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_move(board, 2, 0, 1) == 0 


board859646833 = gamma_board(board)
assert board859646833 is not None
assert board859646833 == ("1112\n"
"1121\n"
"2211\n"
"21.2\n")
del board859646833
board859646833 = None
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_busy_fields(board, 1) == 9 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_busy_fields(board, 2) == 6 
assert gamma_free_fields(board, 2) == 1 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_golden_move(board, 2, 2, 3) == 1 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 2, 2) == 0 
assert gamma_move(board, 2, 3, 2) == 0 


gamma_delete(board)
