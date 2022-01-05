#!/usr/bin/env python


from datetime import date
import random

from paper_cal import *


def get_assignment():
    '''
    '''

    names = ['Name1', 'Name2', 'Name3', 'Name4', 'Name5', 'Name6', 'Name7',
             'Name8', 'Name9']

    # Try to distribute the assignements "fairly"
    # (Run through all the choices uniquely before doing so again)
    while True:
        for name in names:
            yield f' {name}'


def main():
    '''
    '''

    assignment = get_assignment()
    for year in (2022, 2023, 2024, 2025):
        # Lanark North Leeds ARES nets are every Wednesday of each month at
        # 2000H.
        for month in range(1, 13):
            print(closest_date(WED, date(year, month, WEEK1)), end='')
            print(next(assignment))
            print(closest_date(WED, date(year, month, WEEK2)), end='')
            print(next(assignment))
            print(closest_date(WED, date(year, month, WEEK3)), end='')
            print(next(assignment))
            print(closest_date(WED, date(year, month, WEEK4)), end='')
            print(next(assignment))
            # Wednesdays sometimes happen in the 5th week of the month
            if closest_date(WED, date(year, month, WEEK4)) \
                    != closest_date(WED, date(year, month, WEEK4), last=True):
                print(closest_date(WED, date(year, month, WEEK4), last=True), end='')
                print(next(assignment))


if __name__ == '__main__':
    main()
