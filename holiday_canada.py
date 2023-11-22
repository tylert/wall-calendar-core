#!/usr/bin/env python


from datetime import date, timedelta

import click

from paper_cal import *


@click.command()
@click.option(
    '--year',
    '-y',
    default=date.today().year+1,
    help='Year to show',
)
def main(year):
    ''' '''

    #   https://en.wikipedia.org/wiki/Spring_break
    #   https://fr.wikipedia.org/wiki/Semaine_de_rel%C3%A2che
    # March Break
    # Spring Break
    # Congé de mars
    # Congé de printemps
    # Semaine de relâche

    #   https://en.wikipedia.org/wiki/March_equinox
    #   https://fr.wikipedia.org/wiki/%C3%89quinoxe_de_mars
    #   https://en.wikipedia.org/wiki/June_solstice
    #   https://en.wikipedia.org/wiki/September_equinox
    #   https://en.wikipedia.org/wiki/December_solstice
    print(
        f'{spring(year).date()} {spring(year).time().strftime("%H:%M")} First day of Spring'
    )  # Premier jour de printemps
    print(
        f'{summer(year).date()} {summer(year).time().strftime("%H:%M")} First day of Summer'
    )  # Premier jour d'été
    print(
        f'{autumn(year).date()} {autumn(year).time().strftime("%H:%M")} First day of Fall'
    )  # Premier jour d'automne
    print(
        f'{winter(year).date()} {winter(year).time().strftime("%H:%M")} First day of Winter'
    )  # Premier jour d'hiver

    print(
        f'{perihelion(year).date()} {perihelion(year).time().strftime("%H:%M")} Perihelion'
    )  # Périhélie
    print(f'{aphelion(year).date()} {aphelion(year).time().strftime("%H:%M")} Aphelion')
    # Aphélie

    print(
        f'{closest_date(FRIDAY, date(year, AUGUST, WEEK3))} Gold Cup Parade Day (CA-PE)'
    )  # Défilé de la Coupe d'or (CA-PE)


if __name__ == '__main__':
    main()
