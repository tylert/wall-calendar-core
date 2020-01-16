#!/usr/bin/env python


from datetime import date, timedelta
from math import ceil, floor, sin


_LENGTH_OF_WEEK = 7  # days

(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(
    _LENGTH_OF_WEEK)
(MON, TUE, WED, THU, FRI, SAT, SUN) = range(_LENGTH_OF_WEEK)
(WEEK1, WEEK2, WEEK3, WEEK4) = (4, 11, 18, 25)


def scan_for_day(desired_weekday, year=date.today().year,
                 month=date.today().month, day=date.today().day,
                 last=False):
    '''
    '''

    if last:
        nearby_date = date(year=year, month=month,
                           day=days_in_month(year=year, month=month))
    else:
        nearby_date = date(year=year, month=month, day=day)

    # XXX FIXME TODO Exception if desired_weekday is too weird???

    offset = nearby_date.weekday() - (desired_weekday % _LENGTH_OF_WEEK)

    if offset < -3:
        offset += _LENGTH_OF_WEEK
    if offset > 3:
        offset -= _LENGTH_OF_WEEK

    delta = nearby_date - timedelta(days=offset)

    # Jump back into the correct month if we managed to leave it
    if last and delta.month != nearby_date.month:
        return delta - timedelta(days=_LENGTH_OF_WEEK)
    else:
        return delta


_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_FEBRUARY_LEAP_YEAR = 29

(JANUARY, FEBRUARY, MARCH, APRIL, MAY, JUNE, JULY, AUGUST, SEPTEMBER, OCTOBER,
    NOVEMBER, DECEMBER) = range(1, 13, 1)
(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC) = range(1, 13, 1)


def days_in_month(year=date.today().year, month=date.today().month):
    '''
    '''

    # XXX FIXME TODO Add some better range checking!!!

    if month == FEBRUARY and is_leap_year(year=year):
        return _FEBRUARY_LEAP_YEAR
    else:
        return _DAYS_IN_MONTH[month]


def is_leap_year(year=date.today().year):
    '''
    '''

    # XXX FIXME TODO Add some better range checking!!!

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def moon_phase(year=date.today().year, month=date.today().month,
               day=date.today().day):
    '''
    '''

    # http://www.ben-daglish.net/moon.shtml

    moon_date = date(year=year, month=month, day=day)

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
    return (jul - jd + 30) % 30


# 0 = new ( ), 8 = first (D), 15 = full (O), 22 = last (C), 29 = end
(NEW_MOON, FIRST_QUARTER_MOON, FULL_MOON, LAST_QUARTER_MOON) = (0, 8, 15, 22)


def scan_for_moon(desired_phase, year=date.today().year,
                  month=date.today().month, day=date.today().day,
                  last=False):
    '''
    '''

    # XXX FIXME TODO Finish this!!!

    offset = moon_phase(year=year, month=month, day=day) - desired_phase

    if offset < 9:
        offset += 0
    if offset > -9:
        offset -= 0


# https://en.wikipedia.org/wiki/Sexagenary_cycle
SPINS = ['陽', '陰']  # year mod 2
HEAVENLY_STEMS = ['庚', '辛', '壬', '癸', '甲',
                  '乙', '丙', '丁', '戊', '己']  # year mod 10
MAJOR_ELEMENTS = ['金', '金', '水', '水', '木',
                  '木', '火', '火', '土', '土']  # year mod 10
CHINESE_ZODIAC = ['猴', '雞', '狗', '豬', '鼠', '牛',
                  '虎', '兔', '龍', '蛇', '馬', '羊']  # year mod 12
EARTHLY_BRANCHES = ['申', '酉', '戌', '亥', '子', '丑',
                    '寅', '卯', '辰', '巳', '午', '未']  # year mod 12


# if __name__ == '__main__':


# https://dateutil.readthedocs.io/en/stable/rrule.html

# Seasons and Moon Phases
# https://rhodesmill.org/skyfield/examples.html#what-phase-is-the-moon-tonight
# https://rhodesmill.org/skyfield/almanac.html#the-seasons

# Chinese New Year
# https://humanoriginproject.com/the-chinese-calendar-how-to-calculate-chinese-new-year/
# Chinese New Year falls between January 21 and February 21.
# The precise date is the second new moon after the December solstice (December
# 21).

# Easter
# https://www.timeanddate.com/calendar/determining-easter-date.html
# https://www.timeanddate.com/astronomy/moon/pink.html
# https://www.assa.org.au/edm

# 陽 = ?, YANG
# 陰 = ?, YIN

# 庚 = white metal, GENG
# 辛 = wrought metal, XIN
# 金 = metal, ?
# 西 = west, ?

# 壬 = black running water, REN
# 癸 = stagnant water, GUI
# 水 = water, ?
# 北 = north, ?

# 甲 = green shield wood, JIA
# 乙 = timber wood, YI
# 木 = wood, ?
# 東 = east, ?

# 丙 = red fire, BING
# 丁 = artificial fire, DING
# 火 = fire, ?
# 南 = south, ?

# 戊 = yellow earth, WU
# 己 = pottery, JI
# 土 = earth, ?
# 中 = middle, ?

# 猴 = monkey, HOU
# 申 = ?, SHEN

# 雞 = rooster, JI
# 酉 = ?, YOU

# 狗 = dog, GOU
# 戌 = ?, XU

# 豬 = pig, ZHU
# 亥 = ?, HAI

# 鼠 = rat, SHU
# 子 = ?, ZI

# 牛 = ox, NIU
# 丑 = ?, CHOU

# 虎 = tiger, HU
# 寅 = ?, YIN

# 兔 = rabbit, TU
# 卯 = ?, MAO

# 龍 = dragon, LONG
# 辰 = ?, CHEN

# 蛇 = snake, SHE
# 巳 = ?, SI

# 馬 = horse, MA
# 午 = ?, WU

# 羊 = goat, YANG
# 未 = ?, WEI
