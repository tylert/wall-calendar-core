from datetime import date

from paper_cal import *

import pytest


class TestDays:
    def test_some_leap_years(self):
        assert is_leap_year(2000) is True
        assert is_leap_year(2020) is True
        assert is_leap_year(2021) is False
        assert is_leap_year(2022) is False
        assert is_leap_year(2023) is False
        assert is_leap_year(2024) is True

    def test_some_month_lengths(self):
        assert days_in_month(2020, JANUARY) == 31
        assert days_in_month(2020, FEBRUARY) == 29
        assert days_in_month(2020, MARCH) == 31
        assert days_in_month(2020, APRIL) == 30
        assert days_in_month(2020, MAY) == 31
        assert days_in_month(2020, JUNE) == 30
        assert days_in_month(2021, FEBRUARY) == 28
        assert days_in_month(2022, FEBRUARY) == 28
        assert days_in_month(2023, FEBRUARY) == 28
        assert days_in_month(2024, FEBRUARY) == 29

    def test_some_nearby_days(self):
        assert closest_day(SATURDAY, 2020, JANUARY, 30,
                           last=True) == date(2020, JANUARY, 25)
        assert closest_day(SATURDAY, 2020, JANUARY,
                           WEEK4) == date(2020, JANUARY, 25)
        assert closest_day(FRIDAY, 2020, JANUARY, 30,
                           last=True) == date(2020, JANUARY, 31)
        assert closest_day(FRIDAY, 2020, JANUARY,
                           WEEK4) == date(2020, JANUARY, 24)
        assert closest_day(SATURDAY, 2020, JANUARY,
                           WEEK3) == date(2020, JANUARY, 18)
        assert closest_day(SATURDAY, 2020, JANUARY,
                           WEEK2) == date(2020, JANUARY, 11)
        assert closest_day(SATURDAY, 2020, JANUARY,
                           WEEK1) == date(2020, JANUARY, 4)
        assert closest_day(MONDAY, 2020, JULY, 24) == date(2020, JULY, 27)

    def test_some_exception_handling(self):
        with pytest.raises(ValueError):
            assert closest_day(MONDAY, 2020, 13, 32)
        with pytest.raises(TypeError):
            assert closest_day()


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

    def test_some_nearby_moons(self):
        assert closest_moon(FULL_MOON, 2020, JANUARY,
                            7) == date(2020, JANUARY, 9)
        assert closest_moon(FULL_MOON, 2020, JANUARY,
                            15) == date(2020, JANUARY, 9)
        assert closest_moon(NEW_MOON, 2020, JANUARY,
                            1) == date(2019, DECEMBER, 25)
        # assert closest_moon(NEW_MOON, 2020, JANUARY,
        #                     20) == date(2019, JANUARY, 24)
