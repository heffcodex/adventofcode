from solution_02 import *
from utils import cmls

_INPUT = cmls("""
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
""")


def test_possible_12r_13g_14b_idsum():
    games = parse_games(_INPUT)
    idsum = possible_12r_13g_14b_idsum(games)

    assert idsum == 1+2+5

def test_calc_power():
    games = parse_games(_INPUT)

    assert calc_power(games[1]) == 48
    assert calc_power(games[2]) == 12
    assert calc_power(games[3]) == 1560
    assert calc_power(games[4]) == 630
    assert calc_power(games[5]) == 36

def test_calc_power_sum():
    games = parse_games(_INPUT)

    assert calc_power_sum(games) == 2286