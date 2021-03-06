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
uuid: 114711915
"""
"""
random actions, total chaos
"""
board = gamma_new(5, 3, 3, 7)
assert board is not None


assert gamma_move(board, 1, 0, 2) == 1 
assert gamma_move(board, 2, 1, 1) == 1 
assert gamma_move(board, 2, 3, 0) == 1 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 1, 2, 3) == 0 
assert gamma_move(board, 1, 3, 1) == 1 
assert gamma_golden_possible(board, 1) == 1 
assert gamma_move(board, 2, 1, 2) == 1 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 0, 0) == 1 
assert gamma_move(board, 1, 1, 1) == 0 
assert gamma_move(board, 2, 1, 4) == 0 
assert gamma_move(board, 2, 4, 2) == 1 
assert gamma_busy_fields(board, 2) == 4 
assert gamma_move(board, 3, 0, 1) == 1 
assert gamma_move(board, 3, 2, 2) == 1 
assert gamma_move(board, 1, 0, 1) == 0 
assert gamma_move(board, 1, 3, 2) == 1 
assert gamma_move(board, 2, 0, 4) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 3, 3, 2) == 0 
assert gamma_move(board, 1, 1, 2) == 0 
assert gamma_move(board, 2, 0, 2) == 0 
assert gamma_move(board, 1, 1, 2) == 0 
assert gamma_move(board, 1, 2, 2) == 0 
assert gamma_move(board, 2, 3, 1) == 0 
assert gamma_move(board, 3, 1, 4) == 0 
assert gamma_move(board, 3, 4, 1) == 1 
assert gamma_move(board, 1, 0, 2) == 0 
assert gamma_free_fields(board, 1) == 4 


board982159503 = gamma_board(board)
assert board982159503 is not None
assert board982159503 == ("12312\n"
"32.13\n"
"3..2.\n")
del board982159503
board982159503 = None
assert gamma_move(board, 2, 4, 2) == 0 
assert gamma_move(board, 3, 0, 2) == 0 
assert gamma_move(board, 1, 2, 0) == 1 
assert gamma_move(board, 1, 1, 0) == 1 


board773256134 = gamma_board(board)
assert board773256134 is not None
assert board773256134 == ("12312\n"
"32.13\n"
"3112.\n")
del board773256134
board773256134 = None
assert gamma_free_fields(board, 2) == 2 
assert gamma_move(board, 3, 1, 2) == 0 
assert gamma_move(board, 3, 1, 1) == 0 
assert gamma_golden_possible(board, 3) == 1 
assert gamma_move(board, 1, 1, 2) == 0 
assert gamma_move(board, 1, 2, 2) == 0 
assert gamma_move(board, 2, 1, 2) == 0 
assert gamma_move(board, 3, 1, 0) == 0 
assert gamma_move(board, 3, 4, 1) == 0 
assert gamma_golden_move(board, 3, 1, 2) == 1 
assert gamma_move(board, 1, 3, 0) == 0 
assert gamma_move(board, 3, 0, 4) == 0 
assert gamma_move(board, 3, 2, 2) == 0 


gamma_delete(board)
