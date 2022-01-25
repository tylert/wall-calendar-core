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
    #   https://fr.wikipedia.org/wiki/Martin_Luther_King_Day
    print(
        f'{closest_date(MONDAY, date(year, JANUARY, WEEK3))} Martin Luther King Jr. Day (US)'
    )  # Journée de Martin Luther King Jr. (US)

    # Inauguration Day (US) is January 20th or the 21st if the 20th is a Sunday
    # every 4th year where "year mod 4 == 1" (2001, ..., 2013, 2017, 2021,
    # 2025, 2029, etc.)
    #   https://en.wikipedia.org/wiki/United_States_presidential_inauguration
    if 1 == year % 4:
        if SUNDAY == date.weekday(date(year, JANUARY, 20)):
            print(f'{date(year, JANUARY, 21)} Inauguration Day (US)')
        else:
            print(f'{date(year, JANUARY, 20)} Inauguration Day (US)')
    # Jour d'inauguration (US)

    #   https://en.wikipedia.org/wiki/Groundhog_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
    print(f'{date(year, FEBRUARY, 2)} Groundhog Day')  # Jour de la marmotte

    #   https://en.wikipedia.org/wiki/Washington's_Birthday
    #   https://en.wikipedia.org/wiki/Presidents%27_Day
    #   https://fr.wikipedia.org/wiki/Presidents_Day
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} President\'s Day (US)')
    # Journée de la Présidence (US)

    #   https://en.wikipedia.org/wiki/April_Fools'_Day
    #   https://fr.wikipedia.org/wiki/Poisson_d%27avril
    print(f'{date(year, APRIL, 1)} April Fool\'s Day')  # Poisson d'avril

    #   https://en.wikipedia.org/wiki/Tartan_Day
    #   https://fr.wikipedia.org/wiki/Tartan_Day
    print(f'{date(year, APRIL, 6)} Tartan Day')  # Journée du Tartan

    #   https://en.wikipedia.org/wiki/Earth_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_la_Terre
    print(f'{date(year, APRIL, 23)} Earth Day')  # Jour de la Terre

    #   https://en.wikipedia.org/wiki/Anzac_Day
    print(f'{date(year, APRIL, 25)} ANZAC Day (AU, NZ)')
    # Jour d'ANZAC (AU, NZ)

    #   https://en.wikipedia.org/wiki/Mother's_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_des_M%C3%A8res
    print(f'{closest_date(SUNDAY, date(year, MAY, WEEK2))} Mother\'s Day')
    # Fête des mères
    # in UK, "Mothering Sunday" is 4th Sunday of Lent / exactly 3 weeks before Easter Sunday

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
    print(f'{date(year, OCTOBER, 31)} Hallowe\'en')  # Halloween

    #   https://en.wikipedia.org/wiki/Thanksgiving
    #   https://en.wikipedia.org/wiki/Black_Friday_(shopping)
    #   https://en.wikipedia.org/wiki/Cyber_Monday
    print(
        f'{closest_date(THURSDAY, date(year, NOVEMBER, WEEK4))} Thanksgiving Day (US)'
    )  # Action de Grâce (US)
    print(
        f'{closest_date(THURSDAY, date(year, NOVEMBER, WEEK4)) + timedelta(days=1)} Black Friday (US)'
    )  # Vendredi Noir (US)
    print(
        f'{closest_date(THURSDAY, date(year, NOVEMBER, WEEK4)) + timedelta(days=3)} Cyber Monday (US)'
    )  # Cyber Lundi (US)

    #   https://uk-public-holidays.com/early-may-bank-holiday/
    #   https://uk-public-holidays.com/spring-bank-holiday/
    #   https://uk-public-holidays.com/summer-bank-holiday/
    print(
        f'{closest_date(MONDAY, date(year, MAY, WEEK1))} Early May Bank Holiday (UK)'
    )  # May Day
    if 2022 == year:
        print(f'{date(2022, JUNE, 2)} Spring Bank Holiday (UK)')
        print(f'{date(2022, JUNE, 3)} Platinum Jubilee Bank Holiday (UK)')
    else:
        print(
            f'{closest_date(MONDAY, date(year, MAY, WEEK4), last=True)} Spring Bank Holiday (UK)'
        )
    print(
        f'{closest_date(MONDAY, date(year, AUGUST, WEEK4), last=True)} Summer Bank Holiday (UK)'
    )

    # Second Easter (ES)
    # Feast of San Juan (ES)
    # Assumption of Mary (ES)
    # Virgin of Mecy (ES)  is there a typo here???
    # Diada (ES)
    # National Day (ES)
    # Constitution Day (ES)
    # Immaculate Conception (ES) = Immaculate Conception of Mary???
    # Day of Madrid (ES)
    # Feast Day of St. Isodore (ES)
    # Feast of St. James the Apostle (ES)
    # La Almudena (ES)


if __name__ == '__main__':
    main()
