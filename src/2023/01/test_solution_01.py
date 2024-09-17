from solution_01 import *
from utils import cmls


_INPUT_REAL = cmls("""
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
""")

_INPUT_ANY = cmls("""
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
""")

def test_sum_real_digits():
    assert sum_real_digits(_INPUT_REAL) == 142

def test_sum_any_digits():
    assert sum_any_digits(_INPUT_ANY) == 281