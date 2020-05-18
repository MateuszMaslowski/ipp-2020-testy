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
uuid: 899827845
"""
"""
random actions, total chaos
"""
board = gamma_new(3, 5, 4, 2)
assert board is not None


assert gamma_move(board, 1, 1, 2) == 1 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_free_fields(board, 3) == 13 
assert gamma_move(board, 4, 4, 2) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 1, 0, 2) == 1 


board275030387 = gamma_board(board)
assert board275030387 is not None
assert board275030387 == ("...\n"
"...\n"
"11.\n"
"...\n"
"2..\n")
del board275030387
board275030387 = None
assert gamma_move(board, 2, 1, 4) == 1 
assert gamma_move(board, 3, 4, 2) == 0 
assert gamma_move(board, 1, 0, 4) == 1 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 3, 1, 1) == 1 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 1, 2) == 0 
assert gamma_move(board, 1, 3, 2) == 0 
assert gamma_move(board, 2, 1, 0) == 1 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 3, 3, 2) == 0 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_move(board, 4, 1, 2) == 0 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 4, 2) == 0 
assert gamma_move(board, 2, 2, 0) == 1 
assert gamma_move(board, 3, 3, 1) == 0 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_move(board, 4, 2, 2) == 1 
assert gamma_move(board, 4, 2, 3) == 1 
assert gamma_busy_fields(board, 4) == 2 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 4, 0, 3) == 1 
assert gamma_move(board, 1, 4, 2) == 0 
assert gamma_golden_move(board, 1, 0, 1) == 1 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 3, 0, 4) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 2, 4, 2) == 0 
assert gamma_move(board, 2, 0, 1) == 0 


gamma_delete(board)