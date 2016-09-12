#!/usr/bin/env python


from datetime import datetime, timedelta
import math


#http://rhodesmill.org/pyephem/quick.html#phases-of-the-moon
#http://stackoverflow.com/questions/2526815/moon-lunar-phase-algorithm


(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(0, 7)


def next_weekday(date=datetime.today()):
    '''Moo'''
    while True:
        if date.weekday() >= MONDAY and date.weekday() <= FRIDAY:
            yield a_date
        date += timedelta(days=1)


# http://www.ben-daglish.net/moon.shtml
# 0 = new, 8 = first (D), 15 = full (O), 22 = last (C)
def moon_phase(
        year=datetime.today().year,
        month=datetime.today().month,
        day=datetime.today().day):
    '''Foo'''
    n = math.floor(12.37 * (year - 1900 + ((1.0 * month - 0.5) / 12.0)))
    rad = 3.14159265 / 180.0
    t = n / 1236.85
    t2 = t * t
    ass = 359.2242 + 29.105356 * n
    am = 306.0253 + 385.816918 * n + 0.010730 * t2
    xtra = 0.75933 + 1.53058868 * n + ((1.178e-4) - (1.55e-7) * t) * t2
    xtra += (0.1734 - 3.93e-4 * t) * math.sin(rad * ass) - 0.4068 * \
        math.sin(rad * am)
    i = math.floor(xtra) if xtra > 0.0 else math.ceil(xtra - 1.0)
    j1 = julian_day(year, month, day)
    jd = (2415020 + 28 * n) + i
    return (j1 - jd + 30) % 30


def julian_day(
        year=datetime.today().year,
        month=datetime.today().month,
        day=datetime.today().day):
    '''Foo'''
    jy = year
    if year < 0:
        jy += 1
    jm = month + 1
    if month <= 2:
        jy -= 1
        jm += 12
    jul = math.floor(365.25 * jy) + math.floor(30.6001 * jm) + day + 1720995
    if day + 31 * (month + 12 * year) >= (15 + 31 * (10 + 12 * 1582)):
        ja = math.floor(0.01 * jy)
        jul = jul + 2 - ja + math.floor(0.25 * ja)
    return jul


if __name__ == '__main__':
    print(moon_phase())


#import code
#code.interact(local=locals())
