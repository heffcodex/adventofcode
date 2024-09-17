from solution_14 import *
from utils import cmls


_MAT_INPUT = cmls("""
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
""")

_MAT_TILTED_W = cmls("""
O....#....
OOO.#....#
.....##...
OO.#OO....
OO......#.
O.#O...#.#
O....#OO..
O.........
#....###..
#OO..#....
""")

_MAT_TILTED_N = cmls("""
OOOO.#.O..
OO..#....#
OO..O##..O
O..#.OO...
........#.
..#....#.#
..O..#.O.O
..O.......
#....###..
#....#....
""")

_MAT_CYCLED_3 = cmls("""
.....#....
....#...O#
.....##...
..O#......
.....OOO#.
.O#...O#.#
....O#...O
.......OOO
#...O###.O
#.OOO#...O
""")

def test_read_dump_mat():
    assert dump_mat(read_mat(_MAT_INPUT)) == _MAT_INPUT

def test_tilt_vertical():
    mat = read_mat(_MAT_INPUT)

    tilt(mat, "N")
    tilt(mat, "S")
    tilt(mat, "N")

    assert dump_mat(mat) == _MAT_TILTED_N

def test_tilt_horizontal():
    mat = read_mat(_MAT_INPUT)

    tilt(mat, "W")
    tilt(mat, "E")
    tilt(mat, "W")

    assert dump_mat(mat) == _MAT_TILTED_W

def test_cycle_3():
    mat = read_mat(_MAT_INPUT)

    for _ in range(3):
        cycle(mat)

    assert dump_mat(mat) == _MAT_CYCLED_3

def test_calc_load():
    mat = read_mat(_MAT_INPUT)

    tilt(mat, "N")

    assert calc_load(mat) == 136

def test_load_cycles():
    mat = read_mat(_MAT_INPUT)

    assert load_cycles(mat, 1000000000) == 64