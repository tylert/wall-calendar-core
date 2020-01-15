from paper_cal import *


def test_moon_phase():
    assert moon_phase(2020, JANUARY, 9) == FULL_MOON
