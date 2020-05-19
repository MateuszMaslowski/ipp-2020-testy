#include <stdint.h>

#include <stdlib.h>

#include <assert.h>

#include <stdio.h>

#include "gamma.h"

#include <stdbool.h>





int main() {



/*

scenario: test_strip

uuid: 928321062

*/

/*

board is either vertical or horizontal strip

*/

gamma_t* board = gamma_new(1, 62, 8, 4);

assert( board != NULL );





assert( gamma_move(board, 1, 1, 50) == 0 );

assert( gamma_move(board, 2, 0, 4) == 1 );

assert( gamma_move(board, 3, 1, 60) == 0 );

assert( gamma_move(board, 4, 0, 44) == 1 );

assert( gamma_move(board, 5, 0, 12) == 1 );

assert( gamma_move(board, 6, 0, 55) == 1 );

assert( gamma_move(board, 7, 1, 61) == 0 );

assert( gamma_move(board, 8, 1, 48) == 0 );

assert( gamma_move(board, 1, 1, 0) == 0 );

assert( gamma_move(board, 2, 1, 61) == 0 );

assert( gamma_move(board, 3, 1, 18) == 0 );

assert( gamma_move(board, 4, 0, 3) == 1 );

assert( gamma_move(board, 5, 0, 41) == 1 );

assert( gamma_move(board, 6, 1, 16) == 0 );

assert( gamma_move(board, 7, 0, 51) == 1 );

assert( gamma_move(board, 8, 1, 59) == 0 );

assert( gamma_move(board, 1, 1, 47) == 0 );

assert( gamma_move(board, 2, 0, 13) == 1 );

assert( gamma_move(board, 3, 1, 4) == 0 );

assert( gamma_move(board, 4, 0, 48) == 1 );

assert( gamma_move(board, 5, 0, 24) == 1 );

assert( gamma_move(board, 6, 0, 43) == 1 );

assert( gamma_move(board, 7, 1, 11) == 0 );

assert( gamma_move(board, 8, 1, 36) == 0 );

assert( gamma_move(board, 1, 1, 21) == 0 );

assert( gamma_move(board, 2, 0, 58) == 1 );

assert( gamma_move(board, 3, 0, 50) == 1 );

assert( gamma_move(board, 4, 0, 10) == 1 );

assert( gamma_move(board, 5, 0, 46) == 1 );

assert( gamma_move(board, 6, 1, 8) == 0 );

assert( gamma_move(board, 7, 1, 35) == 0 );

assert( gamma_move(board, 8, 1, 38) == 0 );

assert( gamma_move(board, 1, 0, 0) == 1 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 1 );

assert( gamma_free_fields(board, 1) == 46 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 3 );

assert( gamma_free_fields(board, 2) == 46 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 1 );

assert( gamma_free_fields(board, 3) == 46 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 6 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 4 );

assert( gamma_free_fields(board, 5) == 7 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 2 );

assert( gamma_free_fields(board, 6) == 46 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 1 );

assert( gamma_free_fields(board, 7) == 46 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 0 );

assert( gamma_free_fields(board, 8) == 46 );

assert( gamma_move(board, 2, 0, 14) == 1 );

assert( gamma_move(board, 3, 1, 49) == 0 );

assert( gamma_move(board, 4, 1, 18) == 0 );

assert( gamma_move(board, 5, 1, 31) == 0 );

assert( gamma_move(board, 6, 0, 58) == 0 );

assert( gamma_move(board, 7, 0, 35) == 1 );

assert( gamma_move(board, 8, 1, 27) == 0 );

assert( gamma_move(board, 1, 1, 57) == 0 );

assert( gamma_move(board, 2, 1, 51) == 0 );

assert( gamma_move(board, 3, 0, 41) == 0 );

assert( gamma_move(board, 4, 1, 56) == 0 );

assert( gamma_move(board, 5, 1, 16) == 0 );

assert( gamma_move(board, 6, 1, 55) == 0 );

assert( gamma_move(board, 7, 1, 31) == 0 );

assert( gamma_move(board, 8, 0, 25) == 1 );

assert( gamma_move(board, 1, 1, 7) == 0 );

assert( gamma_move(board, 2, 1, 3) == 0 );

assert( gamma_move(board, 3, 0, 36) == 1 );

assert( gamma_move(board, 4, 0, 41) == 0 );

assert( gamma_move(board, 5, 0, 31) == 0 );

assert( gamma_move(board, 6, 1, 42) == 0 );

assert( gamma_move(board, 7, 1, 7) == 0 );

assert( gamma_move(board, 8, 1, 25) == 0 );

assert( gamma_move(board, 1, 0, 40) == 1 );

assert( gamma_move(board, 2, 1, 1) == 0 );

assert( gamma_move(board, 3, 0, 26) == 1 );

assert( gamma_move(board, 4, 1, 54) == 0 );

assert( gamma_move(board, 5, 1, 43) == 0 );

assert( gamma_move(board, 6, 1, 6) == 0 );

assert( gamma_move(board, 7, 1, 34) == 0 );

assert( gamma_move(board, 8, 0, 43) == 0 );

assert( gamma_move(board, 1, 0, 21) == 1 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 3 );

assert( gamma_free_fields(board, 1) == 39 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 4 );

assert( gamma_free_fields(board, 2) == 39 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 3 );

assert( gamma_free_fields(board, 3) == 39 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 6 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 4 );

assert( gamma_free_fields(board, 5) == 5 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 2 );

assert( gamma_free_fields(board, 6) == 39 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 2 );

assert( gamma_free_fields(board, 7) == 39 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 1 );

assert( gamma_free_fields(board, 8) == 39 );

assert( gamma_move(board, 2, 0, 56) == 1 );

assert( gamma_move(board, 3, 1, 25) == 0 );

assert( gamma_move(board, 4, 1, 23) == 0 );

assert( gamma_move(board, 5, 1, 43) == 0 );

assert( gamma_move(board, 6, 1, 58) == 0 );

assert( gamma_move(board, 7, 0, 44) == 0 );

assert( gamma_move(board, 8, 0, 15) == 1 );

assert( gamma_move(board, 1, 1, 14) == 0 );

assert( gamma_move(board, 2, 1, 31) == 0 );

assert( gamma_move(board, 3, 0, 42) == 1 );

assert( gamma_move(board, 4, 0, 48) == 0 );

assert( gamma_move(board, 5, 0, 9) == 0 );

assert( gamma_move(board, 6, 0, 26) == 0 );

assert( gamma_move(board, 7, 1, 23) == 0 );

assert( gamma_move(board, 8, 1, 35) == 0 );

assert( gamma_move(board, 1, 0, 48) == 0 );

assert( gamma_move(board, 2, 0, 34) == 0 );

assert( gamma_move(board, 3, 1, 21) == 0 );

assert( gamma_move(board, 4, 0, 60) == 0 );

assert( gamma_move(board, 5, 0, 21) == 0 );

assert( gamma_move(board, 6, 0, 5) == 1 );

assert( gamma_move(board, 7, 1, 20) == 0 );

assert( gamma_move(board, 8, 0, 8) == 1 );

assert( gamma_move(board, 1, 1, 41) == 0 );

assert( gamma_move(board, 2, 0, 2) == 0 );

assert( gamma_move(board, 3, 1, 20) == 0 );

assert( gamma_move(board, 4, 1, 47) == 0 );

assert( gamma_move(board, 5, 0, 12) == 0 );

assert( gamma_move(board, 6, 1, 24) == 0 );

assert( gamma_move(board, 7, 1, 47) == 0 );

assert( gamma_move(board, 8, 1, 16) == 0 );

assert( gamma_move(board, 1, 0, 59) == 1 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 4 );

assert( gamma_free_fields(board, 1) == 5 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 5 );

assert( gamma_free_fields(board, 2) == 1 );

assert( gamma_golden_move(board, 1, 1, 48) == 0 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 4 );

assert( gamma_free_fields(board, 3) == 3 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 6 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 4 );

assert( gamma_free_fields(board, 5) == 4 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 3 );

assert( gamma_free_fields(board, 6) == 33 );

assert( gamma_golden_move(board, 1, 0, 53) == 0 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 2 );

assert( gamma_free_fields(board, 7) == 33 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 3 );

assert( gamma_free_fields(board, 8) == 33 );

assert( gamma_move(board, 2, 1, 31) == 0 );

assert( gamma_move(board, 3, 0, 56) == 0 );

assert( gamma_move(board, 4, 1, 47) == 0 );

assert( gamma_move(board, 5, 1, 6) == 0 );

assert( gamma_move(board, 6, 0, 51) == 0 );

assert( gamma_move(board, 7, 1, 10) == 0 );

assert( gamma_move(board, 8, 0, 15) == 0 );

assert( gamma_move(board, 1, 0, 59) == 0 );

assert( gamma_move(board, 2, 0, 15) == 0 );

assert( gamma_move(board, 3, 0, 50) == 0 );

assert( gamma_move(board, 4, 0, 40) == 0 );

assert( gamma_move(board, 5, 0, 26) == 0 );

assert( gamma_move(board, 6, 1, 34) == 0 );

assert( gamma_move(board, 7, 1, 32) == 0 );

assert( gamma_move(board, 8, 1, 62) == 0 );

assert( gamma_move(board, 1, 1, 34) == 0 );

assert( gamma_move(board, 2, 0, 41) == 0 );

assert( gamma_move(board, 3, 1, 40) == 0 );

assert( gamma_move(board, 4, 1, 28) == 0 );

assert( gamma_move(board, 5, 1, 2) == 0 );

assert( gamma_move(board, 6, 1, 41) == 0 );

assert( gamma_move(board, 7, 1, 58) == 0 );

assert( gamma_move(board, 8, 0, 9) == 1 );

assert( gamma_move(board, 1, 1, 6) == 0 );

assert( gamma_move(board, 2, 1, 49) == 0 );

assert( gamma_move(board, 3, 1, 40) == 0 );

assert( gamma_move(board, 4, 1, 0) == 0 );

assert( gamma_move(board, 5, 0, 42) == 0 );

assert( gamma_move(board, 6, 0, 35) == 0 );

assert( gamma_move(board, 7, 0, 29) == 1 );

assert( gamma_move(board, 8, 1, 20) == 0 );

assert( gamma_move(board, 1, 0, 11) == 0 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 4 );

assert( gamma_free_fields(board, 1) == 5 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 5 );

assert( gamma_free_fields(board, 2) == 1 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 4 );

assert( gamma_free_fields(board, 3) == 3 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 5 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 4 );

assert( gamma_free_fields(board, 5) == 4 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 3 );

assert( gamma_free_fields(board, 6) == 31 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 3 );

assert( gamma_free_fields(board, 7) == 31 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 4 );

assert( gamma_free_fields(board, 8) == 31 );

assert( gamma_golden_move(board, 1, 1, 49) == 0 );

assert( gamma_move(board, 2, 0, 5) == 0 );

assert( gamma_move(board, 3, 1, 59) == 0 );

assert( gamma_move(board, 4, 0, 33) == 0 );

assert( gamma_move(board, 5, 1, 24) == 0 );

assert( gamma_move(board, 6, 0, 45) == 1 );

assert( gamma_move(board, 7, 1, 46) == 0 );

assert( gamma_move(board, 8, 0, 53) == 1 );

assert( gamma_move(board, 1, 0, 24) == 0 );

assert( gamma_move(board, 2, 1, 60) == 0 );

assert( gamma_move(board, 3, 1, 3) == 0 );

assert( gamma_move(board, 4, 0, 42) == 0 );

assert( gamma_move(board, 5, 0, 17) == 0 );

assert( gamma_move(board, 6, 0, 6) == 1 );

assert( gamma_move(board, 7, 0, 2) == 1 );

assert( gamma_move(board, 8, 1, 28) == 0 );

assert( gamma_move(board, 1, 0, 32) == 0 );

assert( gamma_move(board, 2, 0, 51) == 0 );

assert( gamma_move(board, 3, 1, 50) == 0 );

assert( gamma_move(board, 4, 1, 5) == 0 );

assert( gamma_move(board, 5, 1, 44) == 0 );

assert( gamma_move(board, 6, 0, 56) == 0 );

assert( gamma_move(board, 7, 1, 28) == 0 );

assert( gamma_move(board, 8, 1, 55) == 0 );

assert( gamma_move(board, 1, 1, 37) == 0 );

assert( gamma_move(board, 2, 0, 52) == 0 );

assert( gamma_move(board, 3, 1, 12) == 0 );

assert( gamma_move(board, 4, 1, 32) == 0 );

assert( gamma_move(board, 5, 1, 18) == 0 );

assert( gamma_move(board, 6, 0, 55) == 0 );

assert( gamma_move(board, 7, 0, 22) == 0 );

assert( gamma_move(board, 8, 1, 34) == 0 );

assert( gamma_move(board, 1, 1, 19) == 0 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 4 );

assert( gamma_free_fields(board, 1) == 5 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 5 );

assert( gamma_free_fields(board, 2) == 1 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 4 );

assert( gamma_free_fields(board, 3) == 3 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 3 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 4 );

assert( gamma_free_fields(board, 5) == 3 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 5 );

assert( gamma_free_fields(board, 6) == 2 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 4 );

assert( gamma_free_fields(board, 7) == 5 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 5 );

assert( gamma_free_fields(board, 8) == 4 );

assert( gamma_move(board, 2, 0, 15) == 0 );

assert( gamma_move(board, 3, 0, 27) == 1 );

assert( gamma_move(board, 4, 1, 5) == 0 );

assert( gamma_move(board, 5, 1, 10) == 0 );

assert( gamma_move(board, 6, 0, 39) == 0 );

assert( gamma_move(board, 7, 1, 6) == 0 );

assert( gamma_move(board, 8, 1, 32) == 0 );

assert( gamma_move(board, 1, 1, 27) == 0 );

assert( gamma_move(board, 2, 1, 13) == 0 );

assert( gamma_move(board, 3, 1, 37) == 0 );

assert( gamma_move(board, 4, 1, 62) == 0 );

assert( gamma_move(board, 5, 0, 47) == 1 );

assert( gamma_move(board, 6, 1, 1) == 0 );

assert( gamma_move(board, 7, 1, 11) == 0 );

assert( gamma_move(board, 8, 0, 7) == 1 );

assert( gamma_move(board, 1, 0, 32) == 0 );

assert( gamma_move(board, 2, 0, 34) == 0 );

assert( gamma_move(board, 3, 1, 29) == 0 );

assert( gamma_move(board, 4, 0, 17) == 0 );

assert( gamma_move(board, 5, 1, 24) == 0 );

assert( gamma_move(board, 6, 1, 19) == 0 );

assert( gamma_move(board, 7, 0, 60) == 0 );

assert( gamma_move(board, 8, 0, 38) == 0 );

assert( gamma_move(board, 1, 1, 45) == 0 );

assert( gamma_move(board, 2, 1, 56) == 0 );

assert( gamma_move(board, 3, 0, 11) == 0 );

assert( gamma_move(board, 4, 0, 45) == 0 );

assert( gamma_move(board, 5, 0, 51) == 0 );

assert( gamma_move(board, 6, 0, 37) == 0 );

assert( gamma_move(board, 7, 1, 61) == 0 );

assert( gamma_move(board, 8, 0, 24) == 0 );

assert( gamma_move(board, 1, 1, 39) == 0 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 4 );

assert( gamma_free_fields(board, 1) == 5 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 5 );

assert( gamma_free_fields(board, 2) == 1 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 5 );

assert( gamma_free_fields(board, 3) == 3 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 2 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 5 );

assert( gamma_free_fields(board, 5) == 2 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 5 );

assert( gamma_free_fields(board, 6) == 1 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 4 );

assert( gamma_free_fields(board, 7) == 5 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 6 );

assert( gamma_free_fields(board, 8) == 3 );

assert( gamma_move(board, 2, 0, 30) == 0 );

assert( gamma_move(board, 3, 0, 28) == 1 );

assert( gamma_move(board, 4, 0, 59) == 0 );

assert( gamma_move(board, 5, 0, 52) == 0 );

assert( gamma_move(board, 6, 1, 4) == 0 );

assert( gamma_move(board, 7, 0, 39) == 0 );

assert( gamma_move(board, 8, 0, 28) == 0 );

assert( gamma_move(board, 1, 0, 17) == 0 );

assert( gamma_move(board, 2, 0, 0) == 0 );

assert( gamma_move(board, 3, 0, 25) == 0 );

assert( gamma_move(board, 4, 0, 35) == 0 );

assert( gamma_move(board, 5, 0, 36) == 0 );

assert( gamma_move(board, 6, 1, 18) == 0 );

assert( gamma_move(board, 7, 1, 35) == 0 );

assert( gamma_move(board, 8, 1, 47) == 0 );

assert( gamma_move(board, 1, 0, 9) == 0 );

assert( gamma_move(board, 2, 0, 4) == 0 );

assert( gamma_move(board, 3, 0, 32) == 0 );

assert( gamma_move(board, 4, 0, 47) == 0 );

assert( gamma_move(board, 5, 0, 24) == 0 );

assert( gamma_move(board, 6, 1, 54) == 0 );

assert( gamma_move(board, 7, 1, 26) == 0 );

assert( gamma_move(board, 8, 1, 17) == 0 );

assert( gamma_move(board, 1, 0, 39) == 1 );

assert( gamma_move(board, 2, 0, 31) == 0 );

assert( gamma_move(board, 3, 1, 60) == 0 );

assert( gamma_move(board, 4, 1, 5) == 0 );

assert( gamma_move(board, 5, 0, 27) == 0 );

assert( gamma_move(board, 6, 1, 19) == 0 );

assert( gamma_move(board, 7, 1, 35) == 0 );

assert( gamma_move(board, 8, 0, 49) == 0 );

assert( gamma_move(board, 1, 1, 61) == 0 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 5 );

assert( gamma_free_fields(board, 1) == 5 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 5 );

assert( gamma_free_fields(board, 2) == 1 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 6 );

assert( gamma_free_fields(board, 3) == 2 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 2 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 5 );

assert( gamma_free_fields(board, 5) == 2 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 5 );

assert( gamma_free_fields(board, 6) == 1 );

assert( gamma_golden_move(board, 1, 0, 51) == 0 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 4 );

assert( gamma_free_fields(board, 7) == 4 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 6 );

assert( gamma_free_fields(board, 8) == 3 );

assert( gamma_move(board, 2, 0, 62) == 0 );

assert( gamma_move(board, 3, 1, 48) == 0 );

assert( gamma_move(board, 4, 0, 59) == 0 );

assert( gamma_move(board, 5, 0, 60) == 0 );

assert( gamma_move(board, 6, 1, 10) == 0 );

assert( gamma_move(board, 7, 1, 20) == 0 );

assert( gamma_move(board, 8, 1, 37) == 0 );

assert( gamma_move(board, 1, 1, 41) == 0 );

assert( gamma_move(board, 2, 0, 5) == 0 );

assert( gamma_move(board, 3, 0, 36) == 0 );

assert( gamma_move(board, 4, 1, 34) == 0 );

assert( gamma_move(board, 5, 0, 29) == 0 );

assert( gamma_move(board, 6, 0, 2) == 0 );

assert( gamma_move(board, 7, 0, 51) == 0 );

assert( gamma_move(board, 8, 0, 59) == 0 );

assert( gamma_move(board, 1, 1, 1) == 0 );

assert( gamma_move(board, 2, 0, 16) == 0 );

assert( gamma_move(board, 3, 0, 15) == 0 );

assert( gamma_move(board, 4, 1, 41) == 0 );

assert( gamma_move(board, 5, 0, 54) == 0 );

assert( gamma_move(board, 6, 1, 16) == 0 );

assert( gamma_move(board, 7, 1, 56) == 0 );

assert( gamma_move(board, 8, 0, 1) == 0 );

assert( gamma_move(board, 1, 0, 2) == 0 );

assert( gamma_move(board, 2, 0, 49) == 0 );

assert( gamma_move(board, 3, 1, 20) == 0 );

assert( gamma_move(board, 4, 1, 22) == 0 );

assert( gamma_move(board, 5, 1, 49) == 0 );

assert( gamma_move(board, 6, 0, 11) == 0 );

assert( gamma_move(board, 7, 1, 33) == 0 );

assert( gamma_move(board, 8, 0, 33) == 0 );

assert(gamma_golden_possible(board, 1) == 1);
assert( gamma_busy_fields(board, 1) == 5 );

assert( gamma_free_fields(board, 1) == 5 );

assert(gamma_golden_possible(board, 2) == 1);
assert( gamma_busy_fields(board, 2) == 5 );

assert( gamma_free_fields(board, 2) == 1 );

assert(gamma_golden_possible(board, 3) == 1);
assert( gamma_busy_fields(board, 3) == 6 );

assert( gamma_free_fields(board, 3) == 2 );

assert( gamma_golden_move(board, 8, 1, 19) == 0 );

assert(gamma_golden_possible(board, 4) == 1);
assert( gamma_busy_fields(board, 4) == 4 );

assert( gamma_free_fields(board, 4) == 2 );

assert(gamma_golden_possible(board, 5) == 1);
assert( gamma_busy_fields(board, 5) == 5 );

assert( gamma_free_fields(board, 5) == 2 );

assert( gamma_golden_move(board, 8, 1, 40) == 0 );

assert(gamma_golden_possible(board, 6) == 1);
assert( gamma_busy_fields(board, 6) == 5 );

assert( gamma_free_fields(board, 6) == 1 );

assert(gamma_golden_possible(board, 7) == 1);
assert( gamma_busy_fields(board, 7) == 4 );

assert( gamma_free_fields(board, 7) == 4 );

assert( gamma_golden_move(board, 8, 1, 20) == 0 );

assert(gamma_golden_possible(board, 8) == 1);
assert( gamma_busy_fields(board, 8) == 6 );

assert( gamma_free_fields(board, 8) == 3 );

assert( gamma_golden_move(board, 8, 1, 31) == 0 );





gamma_delete(board);



    return 0;

}
