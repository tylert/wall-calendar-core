#!/usr/bin/env python


from datetime import date, timedelta

import click

from paper_cal import *


def bin_colour_generator():
    ''' '''

    bins = [
        'Blue Bin',  # Bac bleu
        'Yellow Bin',  # Bac jaune
    ]

    while True:
        for bin in bins:
            yield f'{bin}'


def date_generator(start_date=date.today(), skip=LENGTH_OF_WEEK):
    ''' '''

    date_tracker = start_date
    while True:
        yield date_tracker
        date_tracker += timedelta(skip)


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year,
    help='Year to show',
)
def main(year):
    ''' '''

    print(f'{date(2022, JANUARY, 31)} 2000-2030h NC for Capital City Net')
    print(f'{date(2022, FEBRUARY, 28)} 2000-2030h NC for Capital City Net')
    print(f'{date(2022, APRIL, 4)} 2000-2030h NC for Capital City Net')

    # Blue/Yellow Bin
    bin_colour = bin_colour_generator()
    wednesday = date_generator(closest_date(WEDNESDAY, date(year, JANUARY, 4)))
    for week in range(1, 55):
        found = next(wednesday)
        if (
            year == found.year
            and date(year, JANUARY, 1) != found
            and date(year, JULY, 1) != found
            and date(year, DECEMBER, 25) != found
            and date(year, DECEMBER, 26) != found
        ):
            print(f'{found} {next(bin_colour)}')

    #   https://www.oarc.net/
    for month in range(1, 13):
        if JULY != month and AUGUST != month:
            print(
                f'{closest_date(WEDNESDAY, date(year, month, WEEK2))} 1930-2200h OARC Meeting'
            )

    #   https://www.ve3rlr.ca/p/about.html
    for month in range(1, 13):
        print(
            f'{closest_date(THURSDAY, date(year, month, WEEK3))} 1930-2200h RLARC Meeting'
        )
    # print(
    #     f'{closest_date(SATURDAY, date(year, MAY, WEEK2))} 0700-1200h RLARC Fleamarket'
    # )

    #   https://wcarc.on.ca
    for month in range(1, 13):
        print(
            f'{closest_date(MONDAY, date(year, month, WEEK3))} 1900-2100h WCARC Meeting'
        )

    # XXX FIXME TODO  DST start/end times are different for UK, AT, etc.
    # Daylight Savings Time starts on the 2nd Sunday in March
    # Before 2007, old DST started on the 1st Sunday in April
    # "Spring forward" at 0200h local time (except CA-SK)
    #     EST -> UTC-04:00 -> Quebec (EST5EDT)
    #     BST -> UTC+01:00 -> Alpha
    print(
        f'{closest_date(SUNDAY, date(year, MARCH, WEEK2))} Daylight Savings Time Begins (except CA-SK)'
    )  # Heure d'éte commence (sauf CA-SK)

    # Daylight Savings Time ends on the 1st Sunday in November
    # Before 2007, old DST ended on the last Sunday in October
    # "Fall back" at 0200h local time (except CA-SK)
    #     EDT -> UTC-05:00 -> Romeo (EST5EDT)
    #     GMT -> UTC+00:00 -> Zulu
    print(
        f'{closest_date(SUNDAY, date(year, NOVEMBER, WEEK1))} Daylight Savings Time Ends (except CA-SK)'
    )  # Heure d'éte termine (sauf CA-SK)

    #   https://en.wikipedia.org/wiki/Friday_The_13th
    friday = date_generator(closest_date(FRIDAY, date(year, JANUARY, 4)))
    for week in range(1, 55):
        found = next(friday)
        if year == found.year and 13 == found.day:
            print(f'{found} Friday the 13th')  # Le vendredi treize

    print(f'{date(year, FEBRUARY, 20)} {year - 1991} Birthday of Python')
    print(f'{date(year, MARCH, 11)} {year - 2002} Birthday of Arch')
    print(f'{date(year, MARCH, 15)} {year - 2013} Birthday of Docker')
    print(f'{date(year, MARCH, 18)} {year - 1985} Birthday of GNU Manifesto')
    print(f'{date(year, MARCH, 21)} {year - 1993} Birthday of NetBSD')
    print(f'{date(year, APRIL, 16)} {year - 1971} Birthday of FTP')
    print(f'{date(year, JUNE, 1)} {year - 1969} Birthday of Unix')
    print(f'{date(year, JUNE, 19)} {year - 1984} Birthday of X-Windows')
    print(f'{date(year, JUNE, 19)} {year - 1993} Birthday of FreeBSD')
    print(f'{date(year, JUNE, 21)} 1100h {year - 1948} Birthday of Software')
    print(f'{date(year, JUNE, 7)} {year - 2014} Birthday of Kubernetes')
    print(f'{date(year, JULY, 16)} {year - 1993} Birthday of Slackware')
    print(f'{date(year, AUGUST, 1)} {year - 1998} Birthday of IRC')
    print(f'{date(year, AUGUST, 16)} {year - 1993} Birthday of Debian')
    print(f'{date(year, AUGUST, 25)} {year - 1991} Birthday of Linux')
    print(f'{date(year, SEPTEMBER, 27)} {year - 1983} Birthday of GNU')
    print(f'{date(year, SEPTEMBER, 28)} {year - 2010} Birthday of LibreOffice')
    print(f'{date(year, OCTOBER, 18)} {year - 1995} Birthday of OpenBSD')
    print(f'{date(year, OCTOBER, 19)} {year - 2009} Birthday of Alpine')
    print(f'{date(year, OCTOBER, 20)} {year - 2004} Birthday of Ubuntu')
    print(f'{date(year, NOVEMBER, 21)} {year - 1995} Birthday of GIMP')

    #   https://en.wikipedia.org/wiki/Caps_lock#International_Caps_Lock_Day
    print(f'{date(year, JUNE, 28)} INTERNATIONAL CAPS LOCK DAY')
    print(f'{date(year, OCTOBER, 22)} INTERNATIONAL CAPS LOCK DAY')
    # JOURNÉE INTERNATIONALE DU VERROUILLAGE DES MAJUSCULES

    #   https://en.wikipedia.org/wiki/Day_of_the_Programmer
    if is_leap(year):
        print(f'{date(year, SEPTEMBER, 12)} Day of the Programmer 256th day')
        # Jour du programmeur 256e jour
    else:
        print(f'{date(year, SEPTEMBER, 13)} Day of the Programmer 256th day')
        # Jour du programmeur 256e jour

    #   https://en.wikipedia.org/wiki/Software_Freedom_Day
    print(
        f'{closest_date(SATURDAY, date(year, SEPTEMBER, WEEK3))} Software Freedom Day'
    )  # Journée de la liberté des logiciels

    #   http://worldradioday.org
    print(f'{date(year,FEBRUARY, 13)} World Radio Day')
    # Journée mondiale de la radio

    #   http://iaru.org/world-amateur-radio-day.html
    print(f'{date(year, APRIL, 18)} World Amateur Radio Day')
    # Journée de la radio amateur

    #   https://en.wikipedia.org/wiki/Pi_Day
    #   http://www.piday.org/
    #   https://en.wikipedia.org/wiki/Tau_Day
    #   https://tauday.com/
    #   https://en.wikipedia.org/wiki/Pi_Day
    #   http://piapproximationday.com/
    print(f'{date(year, MARCH, 14)} Pi Day 3.14')  # Jour de pi 3.14
    print(f'{date(year, JUNE, 28)} Tau Day 6.28')  # Jour de tau 6.28
    print(f'{date(year, JULY, 22)} Pi Approximation Day 22/7')
    # Jour d'approximation pi 22/7

    #   https://en.wikipedia.org/wiki/Ada_Lovelace_Day
    #   http://findingada.com/about/when-is-ald/
    print(f'{closest_date(TUESDAY, date(year, OCTOBER, WEEK2))} Ada Lovelace Day')
    # Jour de Ada Lovelace

    print(f'{date(year, JULY, 10)} Nikola Tesla Day')


if __name__ == '__main__':
    main()
