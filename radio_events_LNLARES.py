#!/usr/bin/env python


from datetime import date

from paper_cal import (closest_day, WEDNESDAY, WEEK1, WEEK2, WEEK3, WEEK4)


def main():
    '''
    '''

    for year in (2020, 2021, 2022, 2023):
        # Rideau Lakes Amateur Radio Club nets are every Thursday of each month
        # at 2000H
        # https://www.ve3rlr.ca/p/about.html
        for month in range(1, 13):
            print(closest_day(WEDNESDAY, date(year, month, WEEK1)))
            print(closest_day(WEDNESDAY, date(year, month, WEEK2)))
            print(closest_day(WEDNESDAY, date(year, month, WEEK3)))
            print(closest_day(WEDNESDAY, date(year, month, WEEK4)))
            if closest_day(WEDNESDAY, date(year, month, WEEK4)) \
                    != closest_day(WEDNESDAY, date(year, month, WEEK4), last=True):
                print(closest_day(WEDNESDAY, date(year, month, WEEK4), last=True))


if __name__ == '__main__':
    main()
