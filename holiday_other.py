#!/usr/bin/env python


from datetime import date, timedelta

import click

from paper_cal import *


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year,
    help='Year to show',
)
def main(year):

    #   https://en.wikipedia.org/wiki/Martin_Luther_King_Jr._Day
    print(
        f'{closest_date(MONDAY, date(year, JANUARY, WEEK3))} Martin Luther King Jr. Day (US)'
    )
    # Journée de Martin Luther King Jr. (US)

    #   https://en.wikipedia.org/wiki/Washington's_Birthday
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} President\'s Day (US)')
    # Journée de la Présidence (US)

    #   https://en.wikipedia.org/wiki/Memorial_Day
    print(
        f'{closest_date(MONDAY, date(year, MAY, WEEK4), last=True)} Memorial Day (US)'
    )
    # Memorial Day (US)

    #   https://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
    print(f'{date(year, JULY, 4)} Independence Day (US)')
    # Jour de l'indépendance (US)

    #   https://en.wikipedia.org/wiki/Thanksgiving
    #   https://en.wikipedia.org/wiki/Black_Friday_(shopping)
    #   https://en.wikipedia.org/wiki/Cyber_Monday
    buzzard_day = closest_date(THURSDAY, date(year, NOVEMBER, WEEK4))
    print(f'{buzzard_day} Thanksgiving Day (US)')
    print(f'{buzzard_day + timedelta(days=1)} Black Friday (US)')
    print(f'{buzzard_day + timedelta(days=3)} Cyber Monday (US)')
    # Action de Grâce (US)
    # Vendredi Noir (US)
    # Cyber Lundi (US)


if __name__ == '__main__':
    main()
