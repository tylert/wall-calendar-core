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

    #   https://en.wikipedia.org/wiki/Groundhog_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
    print(f'{date(year, FEBRUARY, 2)} Groundhog Day')  # Jour de la marmotte

    #   https://en.wikipedia.org/wiki/Washington's_Birthday
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} President\'s Day (US)')
    # Journée de la Présidence (US)

    #   https://en.wikipedia.org/wiki/April_Fools'_Day
    #   https://fr.wikipedia.org/wiki/Poisson_d%27avril
    print(f'{date(year, APRIL, 1)} April Fool\'s Day')
    # Poisson d'avril

    #   https://en.wikipedia.org/wiki/Tartan_Day
    #   https://fr.wikipedia.org/wiki/Tartan_Day
    print(f'{date(year, APRIL, 6)} Tartan Day')
    # Journée du Tartan

    #   https://en.wikipedia.org/wiki/Earth_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_la_Terre
    print(f'{date(year, APRIL, 23)} Earth Day')
    # Jour de la Terre

    #   https://en.wikipedia.org/wiki/Mother's_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_des_M%C3%A8res
    print(f'{closest_date(SUNDAY, date(year, MAY, WEEK2))} Mother\'s Day')
    # Fête des mères

    #   https://en.wikipedia.org/wiki/Memorial_Day
    #   https://fr.wikipedia.org/wiki/Memorial_Day
    print(
        f'{closest_date(MONDAY, date(year, MAY, WEEK4), last=True)} Memorial Day (US)'
    )

    #   https://en.wikipedia.org/wiki/Father's_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_des_P%C3%A8res
    print(f'{closest_date(SUNDAY, date(year, JUNE, WEEK3))} Father\'s Day')
    # Fête des pères

    #   https://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
    print(f'{date(year, JULY, 4)} Independence Day (US)')
    # Jour de l'indépendance (US)

    #   https://en.wikipedia.org/wiki/Halloween
    #   https://fr.wikipedia.org/wiki/Halloween
    print(f'{date(year, OCTOBER, 31)} Hallowe\'en')
    # Halloween

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
