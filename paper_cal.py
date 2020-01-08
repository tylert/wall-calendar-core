#!/usr/bin/env python


from datetime import date, timedelta
from math import ceil, floor, sin


def moon_phase(year=date.today().year, month=date.today().month,
               day=date.today().day):
    '''
    '''

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

# https://en.wikipedia.org/wiki/Sexagenary_cycle
SPINS = ['陽', '陰']  # year mod 2
HEAVENLY_STEMS = ['庚', '辛', '壬', '癸', '甲', '乙', '丙', '丁', '戊', '己']  # year mod 10
MAJOR_ELEMENTS = ['金', '金', '水', '水', '木', '木', '火', '火', '土', '土']  # year mod 10
CHINESE_ZODIAC = ['猴', '雞', '狗', '豬', '鼠', '牛', '虎', '兔', '龍', '蛇', '馬', '羊']  # year mod 12
EARTHLY_BRANCHES = ['申', '酉', '戌', '亥', '子', '丑', '寅', '卯', '辰', '巳', '午', '未']  # year mod 12


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


# Seasons and Moon Phases
# https://rhodesmill.org/skyfield/examples.html#what-phase-is-the-moon-tonight
# https://rhodesmill.org/skyfield/almanac.html#the-seasons

# Chinese New Year
# https://humanoriginproject.com/the-chinese-calendar-how-to-calculate-chinese-new-year/
# Chinese New Year falls between January 21 and February 21.
# The precise date is the second new moon after the December solstice (December 21).

# Easter
# https://www.timeanddate.com/calendar/determining-easter-date.html
# https://www.timeanddate.com/astronomy/moon/pink.html
# https://www.assa.org.au/edm

# 陽 = yang
# 陰 = yin

# 庚 = white metal, geng
# 辛 = wrought metal, xin
# 金 = metal
# 西 = west

# 壬 = black running water, ren
# 癸 = stagnant water, gui
# 水 = water
# 北 = north

# 甲 = green shield wood, jia
# 乙 = timber wood, yi
# 木 = wood
# 東 = east

# 丙 = red fire, bing
# 丁 = artificial fire, ding
# 火 = fire
# 南 = south

# 戊 = yellow earth, wu
# 己 = pottery, ji
# 土 = earth
# 中 = middle

# 猴 = monkey, hou
# 申 = shen

# 雞 = rooster, ji
# 酉 = you

# 狗 = dog, gou
# 戌 = xu

# 豬 = pig, zhu
# 亥 = hai

# 鼠 = rat, shu
# 子 = zi

# 牛 = ox, niu
# 丑 = chou

# 虎 = tiger, hu
# 寅 = yin

# 兔 = rabbit, tu
# 卯 = mao

# 龍 = dragon, long
# 辰 = chen

# 蛇 = snake, she
# 巳 = si

# 馬 = horse, ma
# 午 = wu

# 羊 = goat, yang
# 未 = wei
