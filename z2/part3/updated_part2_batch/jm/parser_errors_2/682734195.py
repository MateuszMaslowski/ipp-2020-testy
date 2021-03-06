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
uuid: 682734195
"""
"""
random actions, total chaos
"""
board = gamma_new(2, 5, 2, 4)
assert board is not None


assert gamma_move(board, 1, 1, 2) == 1 
assert gamma_move(board, 1, 0, 2) == 1 
assert gamma_move(board, 2, 0, 1) == 1 
assert gamma_move(board, 2, 0, 4) == 1 


board177517380 = gamma_board(board)
assert board177517380 is not None
assert board177517380 == ("2.\n"
"..\n"
"11\n"
"2.\n"
"..\n")
del board177517380
board177517380 = None
assert gamma_move(board, 1, 4, 1) == 0 
assert gamma_busy_fields(board, 1) == 2 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_free_fields(board, 2) == 6 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 2, 0, 0) == 1 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_busy_fields(board, 2) == 3 
assert gamma_move(board, 1, 4, 1) == 0 
assert gamma_move(board, 1, 0, 3) == 1 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_busy_fields(board, 2) == 4 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_golden_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 1, 1, 3) == 1 
assert gamma_move(board, 2, 1, 4) == 1 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_busy_fields(board, 1) == 4 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_golden_possible(board, 2) == 1 
assert gamma_move(board, 1, 0, 3) == 0 


board767137320 = gamma_board(board)
assert board767137320 is not None
assert board767137320 == ("22\n"
"11\n"
"11\n"
"22\n"
"2.\n")
del board767137320
board767137320 = None
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_move(board, 2, 1, 1) == 0 


gamma_delete(board)
