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
uuid: 576919046
"""
"""
random actions, total chaos
"""
board = gamma_new(5, 3, 4, 4)
assert board is not None


assert gamma_move(board, 1, 0, 1) == 1 
assert gamma_move(board, 1, 3, 0) == 1 
assert gamma_busy_fields(board, 1) == 2 
assert gamma_move(board, 2, 2, 1) == 1 
assert gamma_move(board, 3, 1, 2) == 1 
assert gamma_busy_fields(board, 3) == 1 
assert gamma_move(board, 4, 1, 1) == 1 
assert gamma_move(board, 1, 2, 2) == 1 


board426144255 = gamma_board(board)
assert board426144255 is not None
assert board426144255 == (".31..\n"
"142..\n"
"...1.\n")
del board426144255
board426144255 = None
assert gamma_move(board, 2, 2, 0) == 1 


board215183212 = gamma_board(board)
assert board215183212 is not None
assert board215183212 == (".31..\n"
"142..\n"
"..21.\n")
del board215183212
board215183212 = None
assert gamma_move(board, 4, 4, 0) == 1 
assert gamma_busy_fields(board, 4) == 2 
assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_move(board, 1, 4, 1) == 0 


board842793690 = gamma_board(board)
assert board842793690 is not None
assert board842793690 == (".31..\n"
"142..\n"
".1214\n")
del board842793690
board842793690 = None
assert gamma_busy_fields(board, 2) == 2 
assert gamma_move(board, 3, 2, 3) == 0 
assert gamma_move(board, 4, 2, 3) == 0 
assert gamma_move(board, 4, 4, 2) == 1 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_move(board, 3, 3, 0) == 0 
assert gamma_move(board, 4, 1, 3) == 0 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_move(board, 2, 1, 3) == 0 
assert gamma_move(board, 3, 2, 0) == 0 
assert gamma_move(board, 4, 0, 0) == 1 
assert gamma_move(board, 4, 4, 0) == 0 
assert gamma_free_fields(board, 4) == 2 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 2, 1, 4) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_busy_fields(board, 2) == 2 
assert gamma_free_fields(board, 2) == 4 
assert gamma_move(board, 3, 2, 3) == 0 
assert gamma_move(board, 4, 2, 3) == 0 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 4, 0) == 0 
assert gamma_golden_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 3, 2, 3) == 0 
assert gamma_move(board, 3, 4, 1) == 1 
assert gamma_move(board, 4, 2, 3) == 0 
assert gamma_move(board, 2, 3, 2) == 1 
assert gamma_move(board, 2, 3, 0) == 0 


gamma_delete(board)