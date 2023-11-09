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

    #   https://en.wikipedia.org/wiki/Commonwealth_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_Commonwealth
    print(f'{closest_date(MONDAY, date(year, MARCH, WEEK2))} Commonwealth Day')
    # Journée du Commonwealth

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

    #   https://en.wikipedia.org/wiki/Canada_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Canada
    print(f'{date(year, JULY, 1)} Canada Day')  # Fête du Canada
    if SATURDAY == date.weekday(date(year, JULY, 1)) or SUNDAY == date.weekday(
        date(year, JULY, 1)
    ):
        print(f'{closest_date(MONDAY, date(year, JULY, 1))} Canada Day Observed')
        # Fête du Canada observé

    #   https://en.wikipedia.org/wiki/Memorial_Day_(Newfoundland_and_Labrador)
    print(f'{date(year, JULY, 1)} Memorial Day (CA-NL)')

    #   https://en.wikipedia.org/wiki/Construction_Holiday_%28Quebec%29
    #   https://fr.wikipedia.org/wiki/Vacances_de_la_construction
    #   https://www.ccq.org/en/avantages-sociaux/dates-conges-vacances
    #   https://www.ccq.org/fr-CA/avantages-sociaux/dates-conges-vacances
    # The Quebec Construction Holiday begins on the 2nd last Sunday of July and
    # lasts for 2 weeks
    print(
        f'{closest_date(SUNDAY, date(year, JULY, WEEK4), last=True) - timedelta(days=7)} Construction Holiday Begins (CA-QC)'
    )  # Début des vacances de la construction (CA-QC)
    print(
        f'{closest_date(SUNDAY, date(year, JULY, WEEK4), last=True) + timedelta(days=6)} Construction Holiday Ends (CA-QC)'
    )  # Fin des vacances de la construction (CA-QC)

    print(
        f'{closest_date(FRIDAY, date(year, AUGUST, WEEK3))} Gold Cup Parade Day (CA-PE)'
    )  # Défilé de la Coupe d'or (CA-PE)

    #   https://en.wikipedia.org/wiki/Statute_of_Westminster_1931
    #   https://fr.wikipedia.org/wiki/Statut_de_Westminster_de_1931
    #   https://www.canada.ca/en/canadian-heritage/services/important-commemorative-days/anniversary-statute-westminster.html
    #   https://www.canada.ca/fr/patrimoine-canadien/services/journees-importantes-commemoratives/anniversaire-statut-westminster.html
    # The Statute of Westminster was enacted on December 11th, 1931
    print(
        f'{date(year, DECEMBER, 11)} {ordinal(year - 1931)} Anniversary of the Statute of Westminster'
    )  # Anniversaire du Statut de Westminster


if __name__ == '__main__':
    main()
