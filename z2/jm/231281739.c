#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include "gamma.h"
#include <stdbool.h>


int main() {

/*
scenario: fill_board_without_collisions
uuid: 231281739
*/
/*
gamma_move, fill board no collisions, many players, unlimited areas
*/
gamma_t* board = gamma_new(10, 10, 30, 100);
assert( board != NULL );


assert( gamma_move(board, 4, 6, 4) == 1 );
assert( gamma_move(board, 3, 1, 3) == 1 );
assert( gamma_move(board, 24, 0, 1) == 1 );
assert( gamma_move(board, 23, 4, 3) == 1 );
assert( gamma_move(board, 2, 1, 6) == 1 );
assert( gamma_move(board, 20, 7, 2) == 1 );
assert( gamma_move(board, 11, 1, 0) == 1 );
assert( gamma_move(board, 15, 6, 1) == 1 );
assert( gamma_move(board, 10, 6, 6) == 1 );
assert( gamma_move(board, 4, 0, 4) == 1 );
assert( gamma_move(board, 16, 6, 2) == 1 );
assert( gamma_move(board, 16, 0, 3) == 1 );
assert( gamma_move(board, 17, 1, 9) == 1 );
assert( gamma_move(board, 3, 6, 9) == 1 );
assert( gamma_move(board, 4, 5, 9) == 1 );
assert( gamma_move(board, 20, 3, 0) == 1 );
assert( gamma_move(board, 15, 3, 7) == 1 );
assert( gamma_move(board, 1, 4, 7) == 1 );
assert( gamma_move(board, 4, 2, 2) == 1 );
assert( gamma_move(board, 16, 2, 3) == 1 );
assert( gamma_move(board, 23, 3, 8) == 1 );
assert( gamma_move(board, 14, 8, 3) == 1 );
assert( gamma_move(board, 17, 7, 0) == 1 );
assert( gamma_move(board, 25, 4, 6) == 1 );
assert( gamma_move(board, 26, 5, 1) == 1 );
assert( gamma_move(board, 18, 0, 9) == 1 );
assert( gamma_move(board, 3, 8, 8) == 1 );
assert( gamma_move(board, 25, 1, 2) == 1 );
assert( gamma_move(board, 5, 5, 8) == 1 );
assert( gamma_move(board, 29, 3, 4) == 1 );
assert( gamma_move(board, 6, 5, 7) == 1 );
assert( gamma_move(board, 22, 2, 8) == 1 );
assert( gamma_move(board, 22, 4, 5) == 1 );
assert( gamma_move(board, 14, 9, 3) == 1 );
assert( gamma_move(board, 5, 7, 5) == 1 );
assert( gamma_move(board, 7, 5, 3) == 1 );
assert( gamma_move(board, 20, 7, 6) == 1 );
assert( gamma_move(board, 9, 2, 6) == 1 );
assert( gamma_move(board, 15, 7, 4) == 1 );
assert( gamma_move(board, 22, 1, 4) == 1 );
assert( gamma_move(board, 21, 4, 0) == 1 );
assert( gamma_move(board, 18, 8, 2) == 1 );
assert( gamma_move(board, 3, 6, 8) == 1 );
assert( gamma_move(board, 22, 8, 4) == 1 );
assert( gamma_move(board, 27, 7, 3) == 1 );
assert( gamma_move(board, 17, 9, 5) == 1 );
assert( gamma_move(board, 1, 2, 5) == 1 );
assert( gamma_move(board, 13, 5, 2) == 1 );
assert( gamma_move(board, 26, 5, 5) == 1 );
assert( gamma_move(board, 24, 0, 2) == 1 );
assert( gamma_move(board, 28, 5, 0) == 1 );
assert( gamma_move(board, 10, 1, 1) == 1 );
assert( gamma_move(board, 15, 1, 8) == 1 );
assert( gamma_move(board, 13, 0, 8) == 1 );
assert( gamma_move(board, 16, 2, 4) == 1 );
assert( gamma_move(board, 1, 0, 6) == 1 );
assert( gamma_move(board, 18, 7, 7) == 1 );
assert( gamma_move(board, 1, 4, 1) == 1 );
assert( gamma_move(board, 30, 3, 9) == 1 );
assert( gamma_move(board, 19, 3, 6) == 1 );
assert( gamma_move(board, 19, 6, 5) == 1 );
assert( gamma_move(board, 5, 0, 0) == 1 );
assert( gamma_move(board, 20, 5, 6) == 1 );
assert( gamma_move(board, 7, 6, 3) == 1 );
assert( gamma_move(board, 21, 9, 4) == 1 );
assert( gamma_move(board, 26, 2, 1) == 1 );
assert( gamma_move(board, 19, 3, 5) == 1 );
assert( gamma_move(board, 6, 5, 4) == 1 );
assert( gamma_move(board, 5, 4, 4) == 1 );
assert( gamma_move(board, 28, 4, 8) == 1 );
assert( gamma_move(board, 10, 9, 1) == 1 );
assert( gamma_move(board, 14, 9, 9) == 1 );
assert( gamma_move(board, 4, 7, 8) == 1 );
assert( gamma_move(board, 24, 8, 5) == 1 );
assert( gamma_move(board, 6, 8, 1) == 1 );
assert( gamma_move(board, 14, 9, 7) == 1 );
assert( gamma_move(board, 5, 2, 7) == 1 );
assert( gamma_move(board, 29, 3, 2) == 1 );
assert( gamma_move(board, 24, 3, 1) == 1 );
assert( gamma_move(board, 26, 1, 5) == 1 );
assert( gamma_move(board, 13, 2, 9) == 1 );
assert( gamma_move(board, 21, 7, 9) == 1 );
assert( gamma_move(board, 21, 4, 2) == 1 );
assert( gamma_move(board, 25, 9, 8) == 1 );
assert( gamma_move(board, 11, 8, 0) == 1 );
assert( gamma_move(board, 25, 3, 3) == 1 );
assert( gamma_move(board, 29, 8, 6) == 1 );
assert( gamma_move(board, 17, 6, 0) == 1 );
assert( gamma_move(board, 14, 8, 9) == 1 );
assert( gamma_move(board, 2, 6, 7) == 1 );
assert( gamma_move(board, 9, 2, 0) == 1 );
assert( gamma_move(board, 22, 9, 2) == 1 );
assert( gamma_move(board, 19, 0, 5) == 1 );
assert( gamma_move(board, 15, 4, 9) == 1 );
assert( gamma_move(board, 24, 0, 7) == 1 );
assert( gamma_move(board, 24, 7, 1) == 1 );
assert( gamma_move(board, 20, 1, 7) == 1 );
assert( gamma_move(board, 3, 9, 6) == 1 );
assert( gamma_move(board, 22, 8, 7) == 1 );
assert( gamma_move(board, 22, 9, 0) == 1 );


gamma_delete(board);

    return 0;
}
