#!/usr/bin/env python


from datetime import date

from paper_cal import (closest_day, THURSDAY, WEEK1, WEEK2, WEEK3, WEEK4)


def main():
    '''
    '''

    for year in (2020, 2021, 2022, 2023):
        # Rideau Lakes Amateur Radio Club nets are every Thursday of each month
        # https://www.ve3rlr.ca/p/about.html
        for month in range(1, 13):
            print(closest_day(THURSDAY, date(year, month, WEEK1)), end='')
            print(' 1930h RLARC Net')
            print(closest_day(THURSDAY, date(year, month, WEEK2)), end='')
            print(' 1930h RLARC Net')
            print(closest_day(THURSDAY, date(year, month, WEEK3)), end='')
            print(' 1930h RLARC Net')
            print(closest_day(THURSDAY, date(year, month, WEEK4)), end='')
            print(' 1930h RLARC Net')
            if closest_day(THURSDAY, date(year, month, WEEK4)) \
                    != closest_day(THURSDAY, date(year, month, WEEK4), last=True):
                print(closest_day(THURSDAY, date(year, month, WEEK4), last=True), end='')
                print(' 1930h RLARC Net')


if __name__ == '__main__':
    main()
