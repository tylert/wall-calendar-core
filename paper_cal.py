#!/usr/bin/env python


from datetime import date, timedelta
from math import ceil, floor, sin


def moon_phase(year=date.today().year, month=date.today().month,
               day=date.today().day):
    '''
    '''

    # http://rhodesmill.org/pyephem/quick.html#phases-of-the-moon
    # http://stackoverflow.com/questions/2526815/moon-lunar-phase-algorithm
    # http://www.ben-daglish.net/moon.shtml

    moon_date = date(year, month, day)

    n = floor(12.37 * (moon_date.year - 1900 +
                       ((1.0 * moon_date.month - 0.5) / 12.0)))
    rad = 3.14159265 / 180.0
    t = n / 1236.85
    t2 = t * t
    ass = 359.2242 + 29.105356 * n
    am = 306.0253 + 385.816918 * n + 0.010730 * t2
    xtra = 0.75933 + 1.53058868 * n + ((1.178e-4) - (1.55e-7) * t) * t2
    xtra += (0.1734 - 3.93e-4 * t) * sin(rad * ass) - 0.4068 * \
        sin(rad * am)
    i = floor(xtra) if xtra > 0.0 else ceil(xtra - 1.0)
    jy = moon_date.year
    if moon_date.year < 0:
        jy += 1
    jm = moon_date.month + 1
    if moon_date.month <= 2:
        jy -= 1
        jm += 12
    jul = floor(365.25 * jy) + floor(30.6001 * jm) + moon_date.day + 1720995
    if moon_date.day + 31 * (moon_date.month + 12 * moon_date.year) >= (15 + 31 * (10 + 12 * 1582)):
        ja = floor(0.01 * jy)
        jul = jul + 2 - ja + floor(0.25 * ja)
    jd = (2415020 + 28 * n) + i
    # 0 = new ( ), 8 = first (D), 15 = full (O), 22 = last (C)
    return (jul - jd + 30) % 30


LENGTH_OF_WEEK = 7
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(
    LENGTH_OF_WEEK)

(WEEK1, WEEK2, WEEK3, WEEK4) = (4, 11, 18, 25)
DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def scan_for(desired_weekday, year=date.today().year,
            month=date.today().month, day=date.today().day, last=False):
    '''
    '''

    # https://dateutil.readthedocs.io/en/stable/rrule.html

    if last:
        nearest_date = date(year, month, DAYS_IN_MONTH[month])
    else:
        nearest_date = date(year, month, day)

    offset = nearest_date.weekday() - (desired_weekday % LENGTH_OF_WEEK)

    if offset < -3:
        offset += LENGTH_OF_WEEK
    if offset > 3:
        offset -= LENGTH_OF_WEEK

    delta = nearest_date - timedelta(days=offset)

    # Jump back into the correct month if we managed to leave it
    if last and delta.month != nearest_date.month:
        return delta - timedelta(days=LENGTH_OF_WEEK)
    else:
        return delta


def is_leap(year):
    '''
    '''

    # "year -> 1 if leap year, else 0."
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    print(moon_phase(2020, 1, 7))
