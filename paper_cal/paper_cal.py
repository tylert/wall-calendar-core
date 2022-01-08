from datetime import date, timedelta
from math import ceil, floor, pi, sin


(JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC) = range(1, 13, 1)
(
    JANUARY,
    FEBRUARY,
    MARCH,
    APRIL,
    MAY,
    JUNE,
    JULY,
    AUGUST,
    SEPTEMBER,
    OCTOBER,
    NOVEMBER,
    DECEMBER,
) = range(1, 13, 1)

_DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
_FEBRUARY_LEAP_YEAR = 29
_LENGTH_OF_WEEK = 7  # days

(MON, TUE, WED, THU, FRI, SAT, SUN) = range(_LENGTH_OF_WEEK)
(MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY, SUNDAY) = range(
    _LENGTH_OF_WEEK
)
(WEEK1, WEEK2, WEEK3, WEEK4) = (4, 11, 18, 25)

_LENGTH_OF_LUNAR_MONTH = 30
(NEW_MOON, FIRST_QUARTER_MOON, FULL_MOON, LAST_QUARTER_MOON) = (0, 8, 15, 22)

_MOON_GLYPHS = [
    '🌑',  #  0 new moon
    '🌒',  #  1
    '🌒',  #  2
    '🌒',  #  3
    '🌒',  #  4 waxing crescent moon
    '🌒',  #  5
    '🌒',  #  6
    '🌒',  #  7
    '🌓',  #  8 first quarter moon
    '🌔',  #  9
    '🌔',  # 10
    '🌔',  # 11 waxing gibbous moon
    '🌔',  # 12
    '🌔',  # 13
    '🌔',  # 14
    '🌕',  # 15 full moon
    '🌖',  # 16
    '🌖',  # 17
    '🌖',  # 18
    '🌖',  # 19 waning gibbous moon
    '🌖',  # 20
    '🌖',  # 21
    '🌗',  # 22 last quarter moon
    '🌘',  # 23
    '🌘',  # 24
    '🌘',  # 25
    '🌘',  # 26 waning crescent moon
    '🌘',  # 27
    '🌘',  # 28
    '🌘',  # 29
]


def is_leap_year(year=date.today().year):
    ''' '''

    # XXX FIXME TODO Add some better range checking!!!

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year=date.today().year, month=date.today().month):
    ''' '''

    # XXX FIXME TODO Add some better range checking!!!

    if month == FEBRUARY and is_leap_year(year=year):
        return _FEBRUARY_LEAP_YEAR
    else:
        return _DAYS_IN_MONTH[month]


def closest_date(desired_weekday, nearby_date=date.today(), last=False):
    ''' '''

    # Move the nearby_date to the end of the month
    if last:
        nearby_date = date(
            year=nearby_date.year,
            month=nearby_date.month,
            day=days_in_month(year=nearby_date.year, month=nearby_date.month),
        )

    offset = nearby_date.weekday() - (desired_weekday % _LENGTH_OF_WEEK)

    if offset < -3:
        offset += _LENGTH_OF_WEEK
    if offset > 3:
        offset -= _LENGTH_OF_WEEK

    found_date = nearby_date - timedelta(days=offset)

    # Jump back into the correct month if we managed to leave it
    if last and found_date.month != nearby_date.month:
        return found_date - timedelta(days=_LENGTH_OF_WEEK)
    else:
        return found_date


def moon_phase(moon_date=date.today()):
    ''' '''

    # http://www.ben-daglish.net/moon.shtml

    n = floor(12.37 * (moon_date.year - 1900 + ((1.0 * moon_date.month - 0.5) / 12.0)))
    rad = pi / 180.0
    t = n / 1236.85
    t2 = t * t
    ass = 359.2242 + 29.105356 * n
    am = 306.0253 + 385.816918 * n + 0.010730 * t2
    xtra = 0.75933 + 1.53058868 * n + ((1.178e-4) - (1.55e-7) * t) * t2
    xtra += (0.1734 - 3.93e-4 * t) * sin(rad * ass) - 0.4068 * sin(rad * am)
    i = floor(xtra) if xtra > 0.0 else ceil(xtra - 1.0)
    jy = moon_date.year
    if moon_date.year < 0:
        jy += 1
    jm = moon_date.month + 1
    if moon_date.month <= 2:
        jy -= 1
        jm += 12
    jul = floor(365.25 * jy) + floor(30.6001 * jm) + moon_date.day + 1720995
    if moon_date.day + 31 * (moon_date.month + 12 * moon_date.year) >= (
        15 + 31 * (10 + 12 * 1582)
    ):
        ja = floor(0.01 * jy)
        jul = jul + 2 - ja + floor(0.25 * ja)
    jd = (2415020 + 28 * n) + i
    return (jul - jd + 30) % 30


def moon_glyph(moon_date=date.today()):
    ''' '''

    return _MOON_GLYPHS[moon_phase(moon_date=moon_date)]


def closest_moon(desired_phase, nearby_date=date.today(), last=False):
    ''' '''

    # XXX FIXME TODO Exception if desired_phase is too weird???

    offset = moon_phase(nearby_date) - (desired_phase % _LENGTH_OF_LUNAR_MONTH)

    if offset < -14:
        offset += _LENGTH_OF_LUNAR_MONTH
    if offset > 14:
        offset -= _LENGTH_OF_LUNAR_MONTH

    found_date = nearby_date - timedelta(days=offset)

    # Jump back into the correct month if we managed to leave it
    if last and found_date.month != nearby_date.month:
        return found_date - timedelta(days=_LENGTH_OF_LUNAR_MONTH)
    else:
        return found_date


# https://en.wikipedia.org/wiki/Chinese_zodiac
# https://en.wikipedia.org/wiki/Chinese_astrology
# https://en.wikipedia.org/wiki/Sexagenary_cycle
# https://en.wikipedia.org/wiki/Heavenly_Stems
# https://en.wikipedia.org/wiki/Earthly_Branches

_CHINESE_ZODIAC = [
    '猴',  # hóu (monkey)
    '雞',  # jī (rooster) 鸡
    '狗',  # gǒu (dog)
    '豬',  # zhū (pig/boar) 猪
    '鼠',  # shǔ (rat)
    '牛',  # niú (ox)
    '虎',  # hǔ (tiger)
    '兔',  # tù (rabbit)
    '龍',  # lóng (dragon) 龙
    '蛇',  # shé (snake)
    '馬',  # mǎ (horse) 马
    '羊',  # yáng (goat)
]  # year mod 12
_MAJOR_ELEMENTS = [
    '金',  # jīn (metal)
    '金',  # jīn (metal)
    '水',  # shuǐ (water)
    '水',  # shuǐ (water)
    '木',  # mù (wood)
    '木',  # mù (wood)
    '火',  # huǒ (fire)
    '火',  # huǒ (fire)
    '土',  # tǔ (earth)
    '土',  # tǔ (earth)
]  # year mod 10
_SPINS = [
    '陽',  # yáng (white side) 阳
    '陰',  # yīn (black side) 阴
]  # year mod 2
_HEAVENLY_STEMS = [
    '庚',  # gēng
    '辛',  # xīn
    '壬',  # rén
    '癸',  # guǐ
    '甲',  # jiǎ
    '乙',  # yǐ
    '丙',  # bǐng
    '丁',  # dīng
    '戊',  # wù
    '己',  # jǐ
]  # year mod 10
_EARTHLY_BRANCHES = [
    '申',  # shēn
    '酉',  # yǒu
    '戌',  # xū
    '亥',  # hài
    '子',  # zǐ
    '丑',  # chǒu
    '寅',  # yín
    '卯',  # mǎo
    '辰',  # chén
    '巳',  # sì
    '午',  # wǔ
    '未',  # wèi
]  # year mod 12


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

# 庚 = white metal (GENG)
# 辛 = wrought metal (XIN)
# 金 = metal (?)
# 西 = west (?)

# 壬 = black running water (REN)
# 癸 = stagnant water (GUI)
# 水 = water (?)
# 北 = north (?)

# 甲 = green shield wood (JIA)
# 乙 = timber wood (YI)
# 木 = wood (?)
# 東 = east (?)

# 丙 = red fire (BING)
# 丁 = artificial fire (DING)
# 火 = fire (?)
# 南 = south (?)

# 戊 = yellow earth (WU)
# 己 = pottery (JI)
# 土 = earth (?)
# 中 = middle (?)

# Zodiac
# https://en.wikipedia.org/wiki/Astrological_symbols

# Chinese/Lunar New Year is between Jan 21 and Feb 20 on the day after the
# new moon

# January
#   Wolf Moon
#   Old Moon
#   Spirit Moon
#   Moon After Yule
# February
#   Hunger Moon
#   Snow Moon
#   Bear Moon
# March
#   Worm Moon
#   Crow Moon
#   Crust Moon
#   Sap Moon
#   Lenten Moon
#   Sugar Moon
# April
#   Pink Moon
#   Sprouting Grass Moon
#   Egg Moon
#   Fish Moon
#   Sucker Moon
# May
#   Flower Moon
#   Corn Planting Moon
#   Milk Moon
# June
#   Strawberry Moon
#   Rose Moon
# July
#   Buck Moon
#   Thunder Moon
#   Hay Moon
#   Raspberry Moon
# August
#   Sturgeon Moon
#   Red Moon
#   Green Corn Moon
#   Grain Moon
#   Thimbleberry Moon
# September
#   Harvest Moon
#   Corn Moon
# October
#   Hunter's Moon
#   Falling Leaves Moon
# November
#   Beaver Moon
#   Frosty Moon
#   Freezing Moon
# December
#   Cold Moon
#   Long Nights Moon
#   Little Spirit Moon
#   Moon Before Yule
