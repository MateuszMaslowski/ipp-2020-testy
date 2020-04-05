#include <stdint.h>
#include <stdlib.h>
#include <assert.h>
#include <stdio.h>
#include "gamma.h"
#include <stdbool.h>


int main() {

/*
scenario: fill_board_without_collisions
uuid: 429995405
*/
/*
gamma_move, fill board no collisions, many players, unlimited areas
*/
gamma_t* board = gamma_new(10, 10, 30, 100);
assert( board != NULL );


assert( gamma_move(board, 19, 9, 5) == 1 );
assert( gamma_move(board, 26, 4, 7) == 1 );
assert( gamma_move(board, 21, 8, 4) == 1 );
assert( gamma_move(board, 17, 3, 2) == 1 );
assert( gamma_move(board, 4, 9, 1) == 1 );
assert( gamma_move(board, 17, 7, 0) == 1 );
assert( gamma_move(board, 2, 9, 9) == 1 );
assert( gamma_move(board, 15, 8, 2) == 1 );
assert( gamma_move(board, 5, 5, 8) == 1 );
assert( gamma_move(board, 14, 0, 4) == 1 );
assert( gamma_move(board, 9, 1, 4) == 1 );
assert( gamma_move(board, 11, 0, 3) == 1 );
assert( gamma_move(board, 19, 4, 3) == 1 );
assert( gamma_move(board, 3, 6, 6) == 1 );
assert( gamma_move(board, 21, 0, 5) == 1 );
assert( gamma_move(board, 28, 9, 0) == 1 );
assert( gamma_move(board, 1, 8, 3) == 1 );
assert( gamma_move(board, 4, 3, 7) == 1 );
assert( gamma_move(board, 4, 2, 0) == 1 );
assert( gamma_move(board, 9, 5, 0) == 1 );
assert( gamma_move(board, 23, 8, 5) == 1 );
assert( gamma_move(board, 2, 3, 4) == 1 );
assert( gamma_move(board, 27, 7, 3) == 1 );
assert( gamma_move(board, 22, 0, 1) == 1 );
assert( gamma_move(board, 16, 3, 3) == 1 );
assert( gamma_move(board, 11, 6, 1) == 1 );
assert( gamma_move(board, 30, 1, 8) == 1 );
assert( gamma_move(board, 18, 0, 6) == 1 );
assert( gamma_move(board, 15, 3, 8) == 1 );
assert( gamma_move(board, 22, 5, 7) == 1 );
assert( gamma_move(board, 5, 9, 7) == 1 );
assert( gamma_move(board, 13, 3, 5) == 1 );
assert( gamma_move(board, 10, 7, 2) == 1 );
assert( gamma_move(board, 3, 4, 8) == 1 );
assert( gamma_move(board, 16, 2, 1) == 1 );
assert( gamma_move(board, 23, 7, 7) == 1 );
assert( gamma_move(board, 11, 6, 8) == 1 );
assert( gamma_move(board, 4, 4, 6) == 1 );
assert( gamma_move(board, 29, 1, 3) == 1 );
assert( gamma_move(board, 7, 6, 9) == 1 );
assert( gamma_move(board, 30, 4, 4) == 1 );
assert( gamma_move(board, 3, 6, 4) == 1 );
assert( gamma_move(board, 19, 0, 9) == 1 );
assert( gamma_move(board, 6, 1, 9) == 1 );
assert( gamma_move(board, 8, 1, 6) == 1 );
assert( gamma_move(board, 19, 0, 7) == 1 );
assert( gamma_move(board, 29, 5, 9) == 1 );
assert( gamma_move(board, 8, 3, 0) == 1 );
assert( gamma_move(board, 20, 2, 8) == 1 );
assert( gamma_move(board, 24, 1, 2) == 1 );
assert( gamma_move(board, 9, 7, 9) == 1 );
assert( gamma_move(board, 1, 6, 0) == 1 );
assert( gamma_move(board, 6, 9, 3) == 1 );
assert( gamma_move(board, 17, 2, 4) == 1 );
assert( gamma_move(board, 11, 8, 9) == 1 );
assert( gamma_move(board, 10, 9, 8) == 1 );
assert( gamma_move(board, 6, 9, 4) == 1 );
assert( gamma_move(board, 21, 0, 2) == 1 );
assert( gamma_move(board, 6, 1, 0) == 1 );
assert( gamma_move(board, 30, 7, 1) == 1 );
assert( gamma_move(board, 6, 5, 6) == 1 );
assert( gamma_move(board, 4, 6, 3) == 1 );
assert( gamma_move(board, 13, 3, 1) == 1 );
assert( gamma_move(board, 25, 1, 5) == 1 );
assert( gamma_move(board, 17, 9, 6) == 1 );
assert( gamma_move(board, 17, 5, 2) == 1 );
assert( gamma_move(board, 21, 3, 9) == 1 );
assert( gamma_move(board, 10, 6, 5) == 1 );
assert( gamma_move(board, 11, 2, 9) == 1 );
assert( gamma_move(board, 12, 3, 6) == 1 );
assert( gamma_move(board, 26, 4, 9) == 1 );
assert( gamma_move(board, 22, 4, 0) == 1 );
assert( gamma_move(board, 21, 8, 8) == 1 );
assert( gamma_move(board, 21, 7, 8) == 1 );
assert( gamma_move(board, 19, 5, 5) == 1 );
assert( gamma_move(board, 6, 2, 7) == 1 );
assert( gamma_move(board, 22, 8, 1) == 1 );
assert( gamma_move(board, 13, 1, 7) == 1 );
assert( gamma_move(board, 27, 0, 8) == 1 );
assert( gamma_move(board, 8, 7, 4) == 1 );
assert( gamma_move(board, 10, 7, 5) == 1 );
assert( gamma_move(board, 9, 9, 2) == 1 );
assert( gamma_move(board, 4, 0, 0) == 1 );
assert( gamma_move(board, 18, 4, 2) == 1 );
assert( gamma_move(board, 3, 5, 1) == 1 );
assert( gamma_move(board, 2, 5, 3) == 1 );
assert( gamma_move(board, 12, 2, 2) == 1 );
assert( gamma_move(board, 20, 2, 3) == 1 );
assert( gamma_move(board, 17, 7, 6) == 1 );
assert( gamma_move(board, 2, 2, 6) == 1 );
assert( gamma_move(board, 7, 6, 2) == 1 );
assert( gamma_move(board, 3, 8, 6) == 1 );
assert( gamma_move(board, 29, 4, 5) == 1 );
assert( gamma_move(board, 22, 4, 1) == 1 );
assert( gamma_move(board, 12, 2, 5) == 1 );
assert( gamma_move(board, 7, 8, 7) == 1 );
assert( gamma_move(board, 12, 8, 0) == 1 );
assert( gamma_move(board, 29, 5, 4) == 1 );
assert( gamma_move(board, 25, 6, 7) == 1 );
assert( gamma_move(board, 25, 1, 1) == 1 );


gamma_delete(board);

    return 0;
}
