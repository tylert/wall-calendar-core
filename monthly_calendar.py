#!/usr/bin/env python


from datetime import date
from calendar import LocaleTextCalendar

import click


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year,
    help='Year to show',
)
def main(year):
    ''' '''

    # print(LocaleTextCalendar(locale='fr_CA.UTF-8').formatmonth(year, 1, w=10, l=2))
    # print(LocaleTextCalendar(locale='fr_CA.UTF-8').formatmonth(year, 1))
    print(
        LocaleTextCalendar(firstweekday=6, locale='en_CA.UTF-8').formatyear(
            year, w=10, l=2, c=6, m=1
        )
    )

    #   m controls columns (# of months) printed horizontally
    #   c controls space between columns (# of characters)
    #   l controls line spacing (# of lines between)
    #   w controls width of each day column (# characters)


if __name__ == '__main__':
    main()
