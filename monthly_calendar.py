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

    # sudo dpkg-reconfigure locales
    # locale -a

    # cal = LocaleTextCalendar(firstweekday=6, locale='en_CA.UTF-8')
    cal = LocaleTextCalendar(firstweekday=6, locale='fr_CA.UTF-8')

    for month in range(1, 13):
        # print(cal.formatmonth(year, month))
        print(cal.monthdayscalendar(year, month))

    # print(cal.formatmonth(year, 1, w=10, l=2))
    # print(cal.formatyear(year, w=10, l=2, c=6, m=1))

    #   m controls columns (# of months) printed horizontally
    #   c controls space between columns (# of characters)
    #   l controls line spacing (# of lines between)
    #   w controls width of each day column (# characters)

    # dimanche lundi mardi mercredi jeudi vendredi samedi
    # janvier février mars avril mai juin juillet août septembre octobre novembre décembre


if __name__ == '__main__':
    main()
