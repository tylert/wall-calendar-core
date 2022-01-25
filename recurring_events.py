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

    #   https://en.wikipedia.org/wiki/Friday_The_13th
    friday = date_generator(closest_date(FRIDAY, date(year, JANUARY, 4)))
    for week in range(1, 55):
        found = next(friday)
        if year == found.year and 13 == found.day:
            print(f'{found} Friday the 13th')  # Le vendredi treize


if __name__ == '__main__':
    main()
