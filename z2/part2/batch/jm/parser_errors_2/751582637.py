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
uuid: 751582637
"""
"""
random actions, total chaos
"""
board = gamma_new(4, 4, 2, 4)
assert board is not None


assert gamma_move(board, 1, 1, 0) == 1 
assert gamma_move(board, 1, 3, 1) == 1 
assert gamma_busy_fields(board, 1) == 2 
assert gamma_move(board, 1, 2, 1) == 1 
assert gamma_move(board, 1, 0, 1) == 1 
assert gamma_move(board, 2, 3, 2) == 1 
assert gamma_move(board, 2, 3, 0) == 1 
assert gamma_move(board, 1, 0, 0) == 1 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_golden_move(board, 1, 0, 3) == 0 
assert gamma_move(board, 2, 1, 1) == 1 


board238663772 = gamma_board(board)
assert board238663772 is not None
assert board238663772 == ("....\n"
"...2\n"
"1211\n"
"11.2\n")
del board238663772
board238663772 = None
assert gamma_move(board, 1, 1, 0) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_free_fields(board, 2) == 8 
assert gamma_move(board, 1, 2, 0) == 1 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_busy_fields(board, 1) == 6 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 2, 1, 1) == 0 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_free_fields(board, 1) == 7 
assert gamma_move(board, 2, 2, 1) == 0 
assert gamma_busy_fields(board, 1) == 6 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_move(board, 2, 0, 0) == 0 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 1, 3, 2) == 0 
assert gamma_move(board, 2, 1, 0) == 0 
assert gamma_move(board, 2, 1, 3) == 1 
assert gamma_free_fields(board, 2) == 5 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 1, 1, 2) == 1 
assert gamma_free_fields(board, 1) == 5 
assert gamma_move(board, 2, 2, 0) == 0 
assert gamma_move(board, 2, 0, 1) == 0 
assert gamma_move(board, 1, 3, 3) == 1 
assert gamma_move(board, 1, 3, 1) == 0 
assert gamma_busy_fields(board, 1) == 8 
assert gamma_move(board, 2, 3, 0) == 0 
assert gamma_move(board, 2, 2, 0) == 0 


board693508817 = gamma_board(board)
assert board693508817 is not None
assert board693508817 == (".2.1\n"
".1.2\n"
"1211\n"
"1112\n")
del board693508817
board693508817 = None
assert gamma_move(board, 1, 2, 2) == 1 
assert gamma_move(board, 2, 3, 2) == 0 
assert gamma_move(board, 1, 2, 1) == 0 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 0, 3) == 1 
assert gamma_move(board, 1, 2, 0) == 0 
assert gamma_move(board, 1, 2, 3) == 1 
assert gamma_golden_move(board, 1, 1, 1) == 1 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_golden_possible(board, 2) == 1 


gamma_delete(board)
