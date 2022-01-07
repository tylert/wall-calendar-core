#!/usr/bin/env python


from datetime import date

import click

from paper_cal import *


def get_bin():
    ''' '''

    bins = [
        'Blue Bin',  # Bac bleu
        'Yellow Bin',  # Bac jaune
    ]

    while True:
        for bin in bins:
            yield f'{bin}'


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year,
    help='Year to show',
)
def main(year):
    ''' '''


    bin = get_bin()
    for month in range(1, 13):
        # XXX FIXME TODO  OMIT Jan 01, Jul 01, Dec 25, Dec 26!!!
        print(f'{closest_date(WEDNESDAY, date(year, month, WEEK1))} {next(bin)}')
        print(f'{closest_date(WEDNESDAY, date(year, month, WEEK2))} {next(bin)}')
        print(f'{closest_date(WEDNESDAY, date(year, month, WEEK3))} {next(bin)}')
        print(f'{closest_date(WEDNESDAY, date(year, month, WEEK4))} {next(bin)}')
        # Wednesdays sometimes happen in the 5th week of the month
        if closest_date(WEDNESDAY, date(year, month, WEEK4)) != closest_date(
            WEDNESDAY, date(year, month, WEEK4), last=True
        ):
            print(
                f'{closest_date(WEDNESDAY, date(year, month, WEEK4), last=True)} {next(bin)}'
            )


if __name__ == '__main__':
    main()
