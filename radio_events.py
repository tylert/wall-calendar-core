#!/usr/bin/env python


from datetime import date, timedelta

import click

from paper_cal import *


def get_assignment():
    ''' '''

    names = [
        'Name1',
        'Name2',
        'Name3',
        'Name4',
        'Name5',
        'Name6',
        'Name7',
        'Name8',
        'Name9',
    ]

    # Try to distribute the assignements "fairly"
    # (Run through all the choices uniquely before doing so again)
    while True:
        for name in names:
            yield f'{name}'


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year,
    help='Year to show',
)
def main(year):
    ''' '''

    assignment = get_assignment()
    # Lanark North Leeds ARES nets are every Wednesday of each month at
    # 2000H.
    for month in range(1, 13):
        print(
            f'{closest_date(WEDNESDAY, date(year, month, WEEK1))} 20:00 {next(assignment)}'
        )
        print(
            f'{closest_date(WEDNESDAY, date(year, month, WEEK2))} 20:00 {next(assignment)}'
        )
        print(
            f'{closest_date(WEDNESDAY, date(year, month, WEEK3))} 20:00 {next(assignment)}'
        )
        print(
            f'{closest_date(WEDNESDAY, date(year, month, WEEK4))} 20:00 {next(assignment)}'
        )
        # Wednesdays sometimes happen in the 5th week of the month
        if closest_date(WEDNESDAY, date(year, month, WEEK4)) != closest_date(
            WEDNESDAY, date(year, month, WEEK4), last=True
        ):
            print(
                f'{closest_date(WEDNESDAY, date(year, month, WEEK4), last=True)} 20:00 {next(assignment)}'
            )


if __name__ == '__main__':
    main()
