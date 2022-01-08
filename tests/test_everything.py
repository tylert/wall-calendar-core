from datetime import date

import pytest

from paper_cal import *


class TestDays:
    def test_some_leap_years(self):
        assert is_leap(2000) is True
        assert is_leap(2020) is True
        assert is_leap(2021) is False
        assert is_leap(2022) is False
        assert is_leap(2023) is False
        assert is_leap(2024) is True

    def test_some_month_lengths(self):
        assert days_in_month(JANUARY, 2020) == 31
        assert days_in_month(FEBRUARY, 2020) == 29
        assert days_in_month(MARCH, 2020) == 31
        assert days_in_month(APRIL, 2020) == 30
        assert days_in_month(MAY, 2020) == 31
        assert days_in_month(JUNE, 2020) == 30
        assert days_in_month(FEBRUARY, 2021) == 28
        assert days_in_month(FEBRUARY, 2022) == 28
        assert days_in_month(FEBRUARY, 2023) == 28
        assert days_in_month(FEBRUARY, 2024) == 29

    def test_some_nearby_days(self):
        assert closest_date(SATURDAY, date(2020, JANUARY, 30), last=True) == date(
            2020, JANUARY, 25
        )
        assert closest_date(SATURDAY, date(2020, JANUARY, WEEK4)) == date(
            2020, JANUARY, 25
        )
        assert closest_date(FRIDAY, date(2020, JANUARY, 30), last=True) == date(
            2020, JANUARY, 31
        )
        assert closest_date(FRIDAY, date(2020, JANUARY, WEEK4)) == date(
            2020, JANUARY, 24
        )
        assert closest_date(SATURDAY, date(2020, JANUARY, WEEK3)) == date(
            2020, JANUARY, 18
        )
        assert closest_date(SATURDAY, date(2020, JANUARY, WEEK2)) == date(
            2020, JANUARY, 11
        )
        assert closest_date(SATURDAY, date(2020, JANUARY, WEEK1)) == date(
            2020, JANUARY, 4
        )
        assert closest_date(MONDAY, date(2020, JULY, 24)) == date(2020, JULY, 27)

    def test_some_weekday_constants(self):
        assert date.weekday(closest_date(SUNDAY, date(2020, JANUARY, 1))) == 6
        assert date.weekday(closest_date(MONDAY, date(2020, JANUARY, 1))) == 0
        assert date.weekday(closest_date(TUESDAY, date(2020, JANUARY, 1))) == 1
        assert date.weekday(closest_date(WEDNESDAY, date(2020, JANUARY, 1))) == 2
        assert date.weekday(closest_date(THURSDAY, date(2020, JANUARY, 1))) == 3
        assert date.weekday(closest_date(FRIDAY, date(2020, JANUARY, 1))) == 4
        assert date.weekday(closest_date(SATURDAY, date(2020, JANUARY, 1))) == 5

    def test_some_exception_handling(self):
        with pytest.raises(ValueError):
            assert closest_date(MONDAY, date(2020, 13, 32))
        with pytest.raises(TypeError):
            assert closest_date()


class TestMoons:
    def test_some_moon_phases(self):
        assert moon_phase(date(2020, JANUARY, 2)) == FIRST_QUARTER_MOON
        assert moon_phase(date(2020, JANUARY, 9)) == FULL_MOON
        assert moon_phase(date(2020, JANUARY, 16)) == LAST_QUARTER_MOON
        assert moon_phase(date(2020, JANUARY, 23)) == 29  # end of phase
        assert moon_phase(date(2020, JANUARY, 24)) == NEW_MOON
        assert moon_phase(date(2020, OCTOBER, 1)) == FULL_MOON
        assert moon_phase(date(2020, OCTOBER, 31)) == FULL_MOON  # blue moon

    def test_weird_date_exception_handling(self):
        with pytest.raises(ValueError):
            assert moon_phase(date(2020, 13, 32))

    def test_some_nearby_moons(self):
        assert closest_moon(FULL_MOON, date(2020, JANUARY, 7)) == date(2020, JANUARY, 9)
        assert closest_moon(FULL_MOON, date(2020, JANUARY, 15)) == date(
            2020, JANUARY, 9
        )
        assert closest_moon(NEW_MOON, date(2020, JANUARY, 1)) == date(
            2019, DECEMBER, 25
        )
        # assert closest_moon(NEW_MOON, date(2020, JANUARY,
        #                     20)) == date(2019, JANUARY, 24)
