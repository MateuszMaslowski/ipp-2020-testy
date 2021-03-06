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
uuid: 612847053
"""
"""
random actions, total chaos
"""
board = gamma_new(2, 2, 4, 1)
assert board is not None


assert gamma_move(board, 1, 1, 1) == 1 
assert gamma_busy_fields(board, 2) == 0 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_free_fields(board, 3) == 1 


board173911469 = gamma_board(board)
assert board173911469 is not None
assert board173911469 == ("31\n"
"..\n")
del board173911469
board173911469 = None
assert gamma_move(board, 4, 0, 1) == 0 
assert gamma_move(board, 4, 1, 0) == 1 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 1, 0, 0) == 0 
assert gamma_busy_fields(board, 1) == 1 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 0, 1) == 0 


gamma_delete(board)
