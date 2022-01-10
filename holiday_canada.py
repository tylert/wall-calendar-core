#!/usr/bin/env python


from datetime import date

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

    # https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    # https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada

    # New Year's Eve is December 31st
    # New Year's Day is January 1st
    #   https://en.wikipedia.org/wiki/New_Year's_Eve
    #   https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_la_Saint-Sylvestre
    #   https://en.wikipedia.org/wiki/New_Year's_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_l%27an
    print(f'{date(year, DECEMBER, 31)} New Year\'s Eve')  # Veille du Nouvel An
    print(f'{date(year, JANUARY, 1)} New Year\'s Day')  # Jour de l'an
    if (
        date.weekday(date(year, JANUARY, 1)) == SATURDAY
        or date.weekday(date(year, JANUARY, 1)) == SUNDAY
    ):
        print(
            f'{closest_date(MONDAY, date(year, JANUARY, 1))} New Year\'s Day (observed)'
        )  # Jour de l'an (observé)

    # Groundhog Day is February 2nd
    #   https://en.wikipedia.org/wiki/Groundhog_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
    print(f'{date(year, FEBRUARY, 2)} Groundhog Day')  # Jour de la marmotte

    # National Flag of Canada Day is February 15th
    #   https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_drapeau_national_du_Canada
    print(f'{date(year, FEBRUARY, 15)} National Flag of Canada Day')
    # Jour du drapeau national du Canada

    # The 3rd Monday in February is observed in 8 provinces and 0
    # territories...
    #     CA-AB:  Family Day;  statutory
    #     CA-BC:  Family Day;  statutory
    #     CA-MB:  Louis Riel Day;  statutory
    #     CA-NB:  Family Day;  statutory
    #     CA-ON:  Family Day;  statutory
    #     CA-NS:  Heritage Day;  ?
    #     CA-PE:  Islander Day;  statutory
    #     CA-SK:  Family Day;  statutory
    #   https://en.wikipedia.org/wiki/Family_Day
    #   https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} Family Day')
    # Fête de la famille
    # Journée Louis Riel (CA-MB)
    # Fête des Insulaires (CA-PE)
    # Fête du Patrimoine (CA-NS)

    # March break
    # Congé de mars

    #   https://en.wikipedia.org/wiki/Spring_break
    # Spring break
    # Congé de printemps

    # Victoria Day is the Monday on or before May 24th
    # (or the last Monday preceeding May 25th)
    #   https://en.wikipedia.org/wiki/Victoria_Day
    #   https://en.wikipedia.org/wiki/National_Patriots%27_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Reine_(Canada)
    print(f'{closest_date(MONDAY, date(year, MAY, 21))} Victoria Day')
    # Fête de la Reine
    # Fête de Victoria
    # Journée nationale des patriotes (CA-QC)

    # Canada Day is July 1st
    #   https://en.wikipedia.org/wiki/Canada_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Canada
    print(f'{date(year, JULY, 1)} Canada Day')  # Fête du Canada
    if (
        date.weekday(date(year, JULY, 1)) == SATURDAY
        or date.weekday(date(year, JULY, 1)) == SUNDAY
    ):
        print(f'{closest_date(MONDAY, date(year, JULY, 1))} Canada Day (observed)')
        # Fête du Canada (observé)

    # The 1st Monday in August is a quasi-semi-poly-un-statutory holiday,
    # kinda...
    #     CA-AB:  Heritage Day;  optional, formerly statutory
    #     CA-BC:  British Columbia Day;  statutory
    #     CA-MB:  Civic Holiday;  non-statutory
    #     CA-NB:  New Brunswick Day;  statutory
    #     CA-NL:  not observed
    #     CA-NS:  Natal Day;  non-statutory
    #     CA-NT:  Civic Holiday;  statutory
    #     CA-NU:  Civic Holiday;  statutory
    #     CA-ON:  Civic Holiday and Simcoe Day;  non-statutory
    #     CA-PE:  Civic Holiday;  statutory or non-statutory
    #     CA-QC:  not observed
    #     CA-SK:  Saskatchewan Day;  statutory
    #     CA-YT:  not observed
    #   https://en.wikipedia.org/wiki/Civic_Holiday
    #   https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    #   https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
    print(f'{closest_date(MONDAY, date(year, AUGUST, WEEK1))} August Civic Holiday')
    # Longue fin de semaine d'aôut (sauf CA-NL, CA-QC, CA-YT)
    # Premier lundi d'août

    # Labour Day is the 1st Monday in September
    #   https://en.wikipedia.org/wiki/Labour_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
    print(f'{closest_date(MONDAY, date(year, SEPTEMBER, WEEK1))} Labour Day')
    # Fête du Travail

    # Canadian Thanksgiving is the 2nd Monday in October
    #   https://en.wikipedia.org/wiki/Thanksgiving#Canada
    #   https://fr.wikipedia.org/wiki/Action_de_gr%C3%A2ce_(Canada)
    print(f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2))} Thanksgiving Day')
    # Action de Grâce

    # Rememberance Day is November 11th
    #   https://en.wikipedia.org/wiki/Remembrance_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_Souvenir
    print(f'{date(year, NOVEMBER, 11)} Rememberance Day')  # Jour du Souvenir

    # The Statute of Westminster was enacted on December 11th, 1931
    #   https://en.wikipedia.org/wiki/Statute_of_Westminster_1931
    #   https://fr.wikipedia.org/wiki/Statut_de_Westminster_de_1931
    # Anniversary of the Statute of Westminster
    # Anniversaire du Statut de Westminster


if __name__ == '__main__':
    main()
