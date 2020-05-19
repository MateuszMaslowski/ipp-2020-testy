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
uuid: 522367919
"""
"""
random actions, total chaos
"""
board = gamma_new(5, 4, 3, 2)
assert board is not None


assert gamma_move(board, 1, 2, 3) == 1 
assert gamma_move(board, 1, 1, 3) == 1 
assert gamma_free_fields(board, 1) == 18 
assert gamma_move(board, 2, 3, 3) == 1 


board861069519 = gamma_board(board)
assert board861069519 is not None
assert board861069519 == (".112.\n"
".....\n"
".....\n"
".....\n")
del board861069519
board861069519 = None
assert gamma_move(board, 3, 3, 0) == 1 
assert gamma_free_fields(board, 3) == 16 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 1, 1, 2) == 1 
assert gamma_move(board, 2, 2, 3) == 0 
assert gamma_move(board, 2, 4, 0) == 1 
assert gamma_move(board, 3, 2, 1) == 1 
assert gamma_move(board, 3, 0, 1) == 0 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_free_fields(board, 3) == 4 


board621179980 = gamma_board(board)
assert board621179980 is not None
assert board621179980 == (".112.\n"
".1...\n"
"..3..\n"
"...32\n")
del board621179980
board621179980 = None
assert gamma_move(board, 1, 1, 1) == 1 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_free_fields(board, 2) == 3 
assert gamma_golden_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 2, 4) == 0 
assert gamma_move(board, 1, 1, 4) == 0 
assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_free_fields(board, 1) == 5 
assert gamma_golden_move(board, 1, 3, 3) == 1 
assert gamma_move(board, 2, 2, 2) == 1 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_move(board, 3, 2, 4) == 0 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_golden_move(board, 3, 3, 1) == 0 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 4, 2) == 0 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 1, 2, 2) == 0 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_golden_possible(board, 1) == 0 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_move(board, 1, 0, 2) == 1 
assert gamma_free_fields(board, 1) == 5 
assert gamma_move(board, 2, 2, 4) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_golden_move(board, 1, 2, 2) == 0 
assert gamma_move(board, 3, 2, 3) == 0 
assert gamma_move(board, 1, 0, 3) == 1 
assert gamma_golden_possible(board, 1) == 0 
assert gamma_move(board, 3, 0, 1) == 0 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 2, 1, 3) == 0 
assert gamma_move(board, 2, 4, 3) == 0 
assert gamma_move(board, 3, 4, 1) == 0 
assert gamma_move(board, 1, 3, 4) == 0 
assert gamma_busy_fields(board, 1) == 9 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_golden_move(board, 2, 1, 2) == 1 
assert gamma_move(board, 3, 2, 4) == 0 
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 1, 4, 0) == 0 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_move(board, 1, 1, 3) == 0 
assert gamma_move(board, 1, 3, 2) == 1 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_golden_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 3, 1, 3) == 0 
assert gamma_move(board, 3, 3, 2) == 0 
assert gamma_busy_fields(board, 3) == 2 
assert gamma_move(board, 1, 2, 2) == 0 
assert gamma_free_fields(board, 1) == 5 


gamma_delete(board)