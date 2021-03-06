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
uuid: 434375004
"""
"""
random actions, total chaos
"""
board = gamma_new(3, 4, 3, 1)
assert board is not None


assert gamma_move(board, 1, 2, 2) == 1 
assert gamma_move(board, 1, 0, 3) == 0 
assert gamma_move(board, 2, 2, 3) == 1 
assert gamma_free_fields(board, 2) == 1 
assert gamma_move(board, 3, 1, 2) == 1 
assert gamma_move(board, 3, 0, 0) == 0 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 3, 2, 0) == 0 
assert gamma_move(board, 3, 0, 2) == 1 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_busy_fields(board, 1) == 1 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_busy_fields(board, 2) == 1 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 1, 1, 2) == 0 
assert gamma_free_fields(board, 1) == 1 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 2, 0, 1) == 0 


board883965693 = gamma_board(board)
assert board883965693 is not None
assert board883965693 == ("..2\n"
"331\n"
"...\n"
"...\n")
del board883965693
board883965693 = None
assert gamma_move(board, 3, 0, 3) == 1 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_golden_move(board, 2, 2, 2) == 1 
assert gamma_move(board, 3, 0, 0) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 3, 1, 1) == 1 
assert gamma_move(board, 3, 2, 3) == 0 
assert gamma_move(board, 1, 0, 1) == 1 
assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_busy_fields(board, 1) == 2 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_golden_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 3, 3, 1) == 0 


board902176761 = gamma_board(board)
assert board902176761 is not None
assert board902176761 == ("3.2\n"
"332\n"
"13.\n"
"1..\n")
del board902176761
board902176761 = None
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_free_fields(board, 2) == 2 
assert gamma_move(board, 3, 3, 1) == 0 


gamma_delete(board)
