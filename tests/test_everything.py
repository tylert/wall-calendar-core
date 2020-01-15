from paper_cal import *

import pytest


class TestMoons:
    def test_some_moon_phases(self):
        assert moon_phase(2020, JANUARY, 2) == FIRST_QUARTER_MOON
        assert moon_phase(2020, JANUARY, 9) == FULL_MOON
        assert moon_phase(2020, JANUARY, 16) == LAST_QUARTER_MOON
        assert moon_phase(2020, JANUARY, 23) == 29  # end of phase
        assert moon_phase(2020, JANUARY, 24) == NEW_MOON
        assert moon_phase(2020, OCTOBER, 1) == FULL_MOON
        assert moon_phase(2020, OCTOBER, 31) == FULL_MOON  # blue moon

    def test_weird_date_exception_handling(self):
        with pytest.raises(ValueError):
            assert moon_phase(2020, 13, 32)
