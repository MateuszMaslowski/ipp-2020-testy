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
uuid: 467631444
"""
"""
random actions, total chaos
"""
board = gamma_new(5, 4, 4, 1)
assert board is not None


assert gamma_move(board, 1, 0, 3) == 1 
assert gamma_move(board, 2, 1, 4) == 0 
assert gamma_busy_fields(board, 2) == 0 
assert gamma_free_fields(board, 2) == 19 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 3, 2, 2) == 1 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_golden_move(board, 3, 3, 0) == 0 
assert gamma_move(board, 4, 0, 2) == 1 
assert gamma_busy_fields(board, 4) == 1 
assert gamma_golden_move(board, 4, 3, 0) == 0 
assert gamma_move(board, 1, 4, 1) == 0 
assert gamma_move(board, 2, 1, 0) == 1 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 3, 0, 0) == 0 
assert gamma_move(board, 4, 2, 1) == 0 
assert gamma_move(board, 1, 0, 3) == 0 
assert gamma_move(board, 2, 2, 2) == 0 
assert gamma_move(board, 2, 2, 3) == 0 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_busy_fields(board, 3) == 1 


board696212447 = gamma_board(board)
assert board696212447 is not None
assert board696212447 == ("1....\n"
"4.3..\n"
".....\n"
".2...\n")
del board696212447
board696212447 = None
assert gamma_move(board, 4, 2, 2) == 0 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_move(board, 2, 2, 4) == 0 
assert gamma_move(board, 2, 4, 1) == 0 
assert gamma_move(board, 3, 4, 3) == 0 
assert gamma_move(board, 4, 4, 0) == 0 
assert gamma_move(board, 1, 1, 4) == 0 
assert gamma_move(board, 3, 3, 2) == 1 
assert gamma_free_fields(board, 3) == 6 
assert gamma_move(board, 4, 3, 4) == 0 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_move(board, 3, 3, 3) == 1 
assert gamma_move(board, 4, 3, 2) == 0 
assert gamma_move(board, 4, 0, 1) == 1 
assert gamma_golden_possible(board, 4) == 1 
assert gamma_move(board, 1, 0, 3) == 0 
assert gamma_move(board, 2, 0, 3) == 0 
assert gamma_golden_move(board, 2, 2, 0) == 0 
assert gamma_move(board, 3, 3, 1) == 1 
assert gamma_move(board, 4, 0, 2) == 0 
assert gamma_move(board, 1, 2, 4) == 0 
assert gamma_move(board, 2, 2, 3) == 0 
assert gamma_move(board, 3, 0, 1) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 4, 3, 4) == 0 
assert gamma_move(board, 4, 4, 0) == 0 
assert gamma_move(board, 1, 1, 3) == 1 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_move(board, 2, 2, 2) == 0 
assert gamma_golden_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 2, 1) == 1 
assert gamma_busy_fields(board, 3) == 5 
assert gamma_move(board, 4, 3, 2) == 0 
assert gamma_move(board, 1, 2, 4) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_move(board, 3, 0, 3) == 0 
assert gamma_move(board, 4, 0, 3) == 0 
assert gamma_move(board, 4, 3, 1) == 0 
assert gamma_busy_fields(board, 4) == 2 


gamma_delete(board)
