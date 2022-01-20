#!/usr/bin/env python


from datetime import date

import click

from paper_cal import *


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year,
    help='Year to show',
)
def main(year):
    ''' '''

    # Ottawa Amateur Radio Club regular meetings are the 2nd Wednesday of
    # each month except July and August
    #   https://www.oarc.net/
    for month in range(1, 13):
        if month != JULY and month != AUGUST:
            print(
                f'{closest_date(WEDNESDAY, date(year, month, WEEK2))} 1930-2200h OARC Meeting'
            )

    # Rideau Lakes Amateur Radio Club meetings are the 3rd Thursday of each
    # month
    #   https://www.ve3rlr.ca/p/about.html
    for month in range(1, 13):
        print(
            f'{closest_date(THURSDAY, date(year, month, WEEK3))} 1930-2200h RLARC Meeting'
        )
    print(
        f'{closest_date(SATURDAY, date(year, MAY, WEEK2))} 0700-1200h RLARC Fleamarket'
    )

    # West-Carleton Amateur Radio Club meetings are the 3rd Monday of each
    # month
    #   https://wcarc.on.ca
    for month in range(1, 13):
        print(
            f'{closest_date(MONDAY, date(year, month, WEEK3))} 1900-2100h WCARC Meeting'
        )

    # Daylight Savings Time starts on the 2nd Sunday in March
    # Before 2007, old DST started on the 1st Sunday in April
    # "Spring forward" at 0200h local time (except CA-SK)
    #   EST -> UTC-04:00 -> Quebec (EST5EDT)
    #   BST -> UTC+01:00 -> Alpha
    print(f'{date(year, MARCH, WEEK2)} Daylight Savings Time Begins (except CA-SK)')
    # Heure d'éte commence (sauf CA-SK)

    # Daylight Savings Time ends on the 1st Sunday in November
    # Before 2007, old DST ended on the last Sunday in October
    # "Fall back" at 0200h local time (except CA-SK)
    #   EDT -> UTC-05:00 -> Romeo (EST5EDT)
    #   GMT -> UTC+00:00 -> Zulu
    print(f'{date(year, NOVEMBER, WEEK1)} Daylight Savings Time Ends (except CA-SK)')
    # Heure d'éte termine (sauf CA-SK)

    #   https://en.wikipedia.org/wiki/Pi_Day
    #   http://www.piday.org/
    print(f'{date(year, MARCH, 14)} Pi Day 3.14')  # Jour de pi 3.14

    #   https://en.wikipedia.org/wiki/Tau_Day
    #   https://tauday.com/
    print(f'{date(year, JUNE, 28)} Tau Day 6.28')  # Jour de tau 6.28

    #   https://en.wikipedia.org/wiki/Pi_Day
    #   http://piapproximationday.com/
    print(f'{date(year, JULY, 22)} Pi Approximation Day 22/7')
    # Jour d'approximation pi 22/7

    # The Day of the Programmer is the 256th day of the year
    #   https://en.wikipedia.org/wiki/Day_of_the_Programmer
    if is_leap(year):
        print(f'{date(year, SEPTEMBER, 12)} Day of the Programmer 256th day')
        # Jour du programmeur 256e jour
    else:
        print(f'{date(year, SEPTEMBER, 13)} Day of the Programmer 256th day')
        # Jour du programmeur 256e jour


if __name__ == '__main__':
    main()
