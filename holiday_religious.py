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

    # Epiphany is January 6th
    #   https://en.wikipedia.org/wiki/Epiphany_(holiday)
    #   https://fr.wikipedia.org/wiki/%C3%89piphanie
    print(f'{date(year, JANUARY, 6)} Epiphany')  # Epiphanie

    # St. Valentine's Day is February 14th
    #   https://en.wikipedia.org/wiki/Valentine%27s_Day
    #   https://fr.wikipedia.org/wiki/Saint-Valentin
    print(f'{date(year, FEBRUARY, 14)} St. Valentine\'s Day')  # Saint-Valentin

    # Annunciation is March 25th
    #   https://en.wikipedia.org/wiki/Annunciation
    #   https://fr.wikipedia.org/wiki/Annonciation
    print(f'{date(year, MARCH, 25)} Annunciation')  # Annonciation

    print(f'{spring(year).date()} First day of Spring')
    print(f'{summer(year).date()} First day of Summer')
    print(f'{autumn(year).date()} First day of Fall')
    print(f'{winter(year).date()} First day of Winter')

    # Easter is the 1st Sunday after the 1st full moon after the Spring
    # equinox (min:  March 22nd, max:  April 25th)
    #   https://en.wikipedia.org/wiki/Ecclesiastical_full_moon#Paschal_full_moon
    #   https://en.wikipedia.org/wiki/Computus
    #   https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques
    #   https://en.wikipedia.org/wiki/Shrove_Tuesday
    #   https://fr.wikipedia.org/wiki/Mardi_gras
    #   https://en.wikipedia.org/wiki/Ash_Wednesday
    #   https://fr.wikipedia.org/wiki/Mercredi_des_Cendres
    #   https://en.wikipedia.org/wiki/Palm_Sunday
    #   https://fr.wikipedia.org/wiki/Dimanche_des_Rameaux
    #   https://en.wikipedia.org/wiki/Maundy_Thursday
    #   https://fr.wikipedia.org/wiki/Jeudi_saint
    #   https://en.wikipedia.org/wiki/Good_Friday
    #   https://fr.wikipedia.org/wiki/Vendredi_saint
    #   https://en.wikipedia.org/wiki/Easter
    #   https://fr.wikipedia.org/wiki/P%C3%A2ques
    #   https://en.wikipedia.org/wiki/Feast_of_the_Ascension
    #   https://fr.wikipedia.org/wiki/Ascension_(f%C3%AAte)
    #   https://en.wikipedia.org/wiki/Pentecost
    #   https://fr.wikipedia.org/wiki/Pentec%C3%B4te
    #   https://www.timeanddate.com/holidays/common/carnival-wednesday
    #   https://www.timeanddate.com/holidays/common/palm-sunday
    #   https://www.timeanddate.com/holidays/common/maundy-thursday
    #   https://www.timeanddate.com/holidays/common/good-friday
    #   https://www.timeanddate.com/holidays/common/holy-saturday
    #   https://www.timeanddate.com/holidays/common/easter-monday
    #   https://www.timeanddate.com/holidays/common/ascension-day
    #   https://www.timeanddate.com/holidays/common/whit-sunday
    #   https://www.timeanddate.com/holidays/common/whit-monday
    #   https://www.timeanddate.com/holidays/common/trinity
    #   https://www.timeanddate.com/holidays/common/corpus-christi
    print(f'{easter(year) - timedelta(days=47)} Shrove/Pancake Tuesday')  # Mardi Gras
    print(f'{easter(year) - timedelta(days=46)} Ash Wednesday')  # Mercredi des Cendres
    print(f'{easter(year) - timedelta(days=7)} Palm Sunday')  # Dimanche des Rameaux
    print(f'{easter(year) - timedelta(days=3)} Maundy Thursday')  # Jeudi saint
    print(f'{easter(year) - timedelta(days=2)} Good Friday')  # Vendredi saint
    print(f'{easter(year) - timedelta(days=1)} Easter Saturday')
    print(f'{easter(year)} Easter Sunday')  # Le dimanche de Pâques
    print(f'{easter(year) + timedelta(days=1)} Easter Monday')  # Le lundi de Pâques
    print(f'{easter(year) + timedelta(days=39)} Ascension Day')  # Ascension
    print(f'{easter(year) + timedelta(days=49)} Whit Sunday/Pentecost')  # Pentecôte
    print(f'{easter(year) + timedelta(days=50)} Whit Monday')
    print(f'{easter(year) + timedelta(days=56)} Trinity Sunday')
    print(f'{easter(year) + timedelta(days=60)} Corpus Christi')

    # All Saints' Day is November 1st
    #   https://en.wikipedia.org/wiki/All_Saints%27_Day
    #   https://fr.wikipedia.org/wiki/Toussaint
    print(f'{date(year, NOVEMBER, 1)} All Saints\' Day')  # Toussaint

    # All Souls' Day is November 2nd
    #   https://en.wikipedia.org/wiki/All_Souls%27_Day
    #   https://fr.wikipedia.org/wiki/Comm%C3%A9moration_des_fid%C3%A8les_d%C3%A9funts
    print(f'{date(year, NOVEMBER, 2)} All Souls\' Day')  # Fête des Morts

    # Christmas Day is December 25th
    # Boxing Day is December 26th
    #   https://en.wikipedia.org/wiki/Christmas
    #   https://fr.wikipedia.org/wiki/No%C3%ABl
    #   https://en.wikipedia.org/wiki/Boxing_Day
    #   https://fr.wikipedia.org/wiki/Boxing_Day
    print(f'{date(year, DECEMBER, 24)} Christmas Eve')  # Veille de Noël
    print(f'{date(year, DECEMBER, 25)} Christmas Day')  # Noël
    print(f'{date(year, DECEMBER, 26)} Boxing Day')
    # Lendemain de Noël
    # Le jour des boîtes
    # Après-Noël
    if date.weekday(date(year, DECEMBER, 25)) == SATURDAY:
        print(
            f'{closest_date(MONDAY, date(year, DECEMBER, 25))} Christmas Day (observed)'
        )
        print(
            f'{closest_date(TUESDAY, date(year, DECEMBER, 26))} Boxing Day (observed)'
        )
    if date.weekday(date(year, DECEMBER, 25)) == SUNDAY:
        print(
            f'{closest_date(TUESDAY, date(year, DECEMBER, 25))} Christmas Day (observed)'
        )


if __name__ == '__main__':
    main()
