#!/usr/bin/env python


from datetime import date

from paper_cal import (closest_day, MONDAY, WEDNESDAY, THURSDAY, SATURDAY,
                       WEEK1, WEEK2, WEEK3, MAY, JUNE, JULY, SEPTEMBER)


def main():
    '''
    '''

    for year in (2022, 2023):
        # Ottawa Amateur Radio Club executive meetings are the 1st Wednesday of
        # each month except July and August
        # Ottawa Amateur Radio Club regular meetings are the 2nd Wednesday of
        # each month except July and August
        # https://www.oarc.net/
        for month in range(1, 13, 1):
            # XXX FIXME TODO Make summer break work properly
            if month != JUNE or month != JULY:
                print(closest_day(WEDNESDAY, date(year, month, WEEK1)), end='')
                print(' 1900-2100h OARC Exec')
                # exécutif
                print(closest_day(WEDNESDAY, date(year, month, WEEK2)), end='')
                print(' 1930-2200h OARC')
        print(closest_day(SATURDAY, date(year, SEPTEMBER, WEEK2)), end='')
        print(' 0700-1200h OARC Hamfest')
        print(closest_day(SATURDAY, date(year, SEPTEMBER, WEEK3)), end='')
        print(' 0800-1300h OARC Demo')

        # Rideau Lakes Amateur Radio Club meetings are the 3rd Thursday of each
        # month
        # https://www.ve3rlr.ca/p/about.html
        for month in range(1, 13):
            print(closest_day(THURSDAY, date(year, month, WEEK3)), end='')
            print(' 1930-2200h RLARC')
        print(closest_day(SATURDAY, date(year, MAY, WEEK2)), end='')
        print(' 0700-1200h RLARC Fleamarket')

        # West-Carleton Amateur Radio Club meetings are the 3rd Monday of each
        # month
        # https://wcarc.on.ca
        for month in range(1, 13):
            print(closest_day(MONDAY, date(year, month, WEEK3)), end='')
            print(' 1900-2100h WCARC')

    # Daylight Savings Time starts on the 2nd Sunday in March
    # Before 2007, old DST started on the 1st Sunday in April
    # "Spring forward" at 0200h local time (except CA-SK)
    #   EST -> UTC-04:00 -> Quebec (EST5EDT)
    #   BST -> UTC+01:00 -> Alpha

    # Daylight Savings Time ends on the 1st Sunday in November
    # Before 2007, old DST ended on the last Sunday in October
    # "Fall back" at 0200h local time (except CA-SK)
    #   EDT -> UTC-05:00 -> Romeo (EST5EDT)
    #   GMT -> UTC+00:00 -> Zulu


if __name__ == '__main__':
    main()
