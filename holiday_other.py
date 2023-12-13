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

    #   https://en.wikipedia.org/wiki/Friday_The_13th
    #   https://fr.wikipedia.org/wiki/Vendredi_treize
    friday = repeat_date(closest_date(FRIDAY, date(year, JANUARY, 4)))
    for week in range(1, 55):
        found = next(friday)
        if year == found.year and 13 == found.day:
            print(f'{found} Friday the 13th')  # Vendredi treize

    #   https://en.wikipedia.org/wiki/Grandparents'_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_des_grands-parents
    # XXX FIXME TODO  2nd Sunday in September or 1st Sunday after Labour Day
    # print(f'{closest_date(SUNDAY, date(year, SEPTEMBER, WEEK2))} Grandparents\' Day (US)')
    # print(f'{closest_date(MONDAY, date(year, SEPTEMBER, WEEK1)) + timedelta(days=6)} Grandparents\' Day (US)')
    # Fête des grands-parents (US)
    # Journée nationale des grands-parents (US)

    #   https://es.wikipedia.org/wiki/D%C3%ADa_Internacional_de_los_Trabajadores
    #   https://es.wikipedia.org/wiki/Fiesta_de_San_Juan
    #   https://es.wikipedia.org/wiki/Asunci%C3%B3n_de_Mar%C3%ADa
    #   https://es.wikipedia.org/wiki/D%C3%ADa_de_Catalu%C3%B1a
    #   https://es.wikipedia.org/wiki/Fiesta_Nacional_de_Espa%C3%B1a
    #   https://es.wikipedia.org/wiki/D%C3%ADa_de_Todos_los_Santos
    #   https://es.wikipedia.org/wiki/D%C3%ADa_de_la_Constituci%C3%B3n_(Espa%C3%B1a)
    print(f'{date(year, MAY, 1)} Fiesta del Trabajo (ES)')
    print(f'{date(year, JUNE, 24)} San Juan (ES-CT)')
    print(f'{date(year, AUGUST, 15)} La Asunción (ES)')
    print(f'{date(year, SEPTEMBER, 11)} Diada Nacional de Catalunya (ES)')
    print(f'{date(year, OCTOBER, 12)} Fiesta Nacional de España (ES)')
    print(f'{date(year, NOVEMBER, 1)} Todos los Santos (ES)')
    print(f'{date(year, DECEMBER, 6)} Dia de la Constitución (ES)')

    print(f'{date(year, FEBRUARY, 20)} {ordinal(year - 1991)} Birthday of Python')
    print(f'{date(year, MARCH, 11)} {ordinal(year - 2002)} Birthday of Arch')
    print(f'{date(year, MARCH, 15)} {ordinal(year - 2013)} Birthday of Docker')
    print(f'{date(year, MARCH, 18)} {ordinal(year - 1985)} Birthday of GNU Manifesto')
    print(f'{date(year, MARCH, 21)} {ordinal(year - 1993)} Birthday of NetBSD')
    print(f'{date(year, APRIL, 3)} {ordinal(year - 2005)} Birthday of Git')
    print(f'{date(year, APRIL, 16)} {ordinal(year - 1971)} Birthday of FTP')
    print(f'{date(year, MAY, 22)} {ordinal(year - 1973)} Birthday of Ethernet')
    print(f'{date(year, JUNE, 1)} {ordinal(year - 1969)} Birthday of Unix')
    print(f'{date(year, JUNE, 19)} {ordinal(year - 1984)} Birthday of X-Windows')
    print(f'{date(year, JUNE, 19)} {ordinal(year - 1993)} Birthday of FreeBSD')
    print(f'{date(year, JUNE, 7)} {ordinal(year - 2014)} Birthday of Kubernetes')
    print(f'{date(year, JULY, 16)} {ordinal(year - 1993)} Birthday of Slackware')
    print(f'{date(year, AUGUST, 1)} {ordinal(year - 1998)} Birthday of IRC')
    print(f'{date(year, AUGUST, 15)} {ordinal(year - 1997)} Birthday of GNOME')
    print(f'{date(year, AUGUST, 16)} {ordinal(year - 1993)} Birthday of Debian')
    print(f'{date(year, AUGUST, 25)} {ordinal(year - 1991)} Birthday of Linux')
    print(f'{date(year, SEPTEMBER, 27)} {ordinal(year - 1983)} Birthday of GNU')
    print(f'{date(year, SEPTEMBER, 28)} {ordinal(year - 2010)} Birthday of LibreOffice')
    print(f'{date(year, OCTOBER, 18)} {ordinal(year - 1995)} Birthday of OpenBSD')
    print(f'{date(year, OCTOBER, 19)} {ordinal(year - 2009)} Birthday of Alpine')
    print(f'{date(year, OCTOBER, 20)} {ordinal(year - 2004)} Birthday of Ubuntu')
    print(f'{date(year, NOVEMBER, 6)} {ordinal(year - 2003)} Birthday of Inkscape')
    print(f'{date(year, NOVEMBER, 21)} {ordinal(year - 1995)} Birthday of GIMP')

    print(f'{date(year, MARCH, 21)} Aries Rises')  # Ascension du bélier
    print(f'{date(year, APRIL, 19)} Aries Sets')  # Descension du bélier
    print(f'{date(year, APRIL, 20)} Taurus Rises')  # Ascension du taureau
    print(f'{date(year, MAY, 20)} Taurus Sets')  # Descension du taureau
    print(f'{date(year, MAY, 21)} Gemini Rises')  # Ascension des gémeaux
    print(f'{date(year, JUNE, 20)} Gemini Sets')  # Descension des gémeaux
    print(f'{date(year, JUNE, 21)} Cancer Rises')  # Ascension du cancer
    print(f'{date(year, JULY, 22)} Cancer Sets')  # Descension du cancer
    print(f'{date(year, JULY, 23)} Leo Rises')  # Ascension du lion
    print(f'{date(year, AUGUST, 22)} Leo Sets')  # Descension du lion
    print(f'{date(year, AUGUST, 23)} Virgo Rises')  # Ascension de la vierge
    print(f'{date(year, SEPTEMBER, 22)} Virgo Sets')  # Descension de la vierge
    print(f'{date(year, SEPTEMBER, 23)} Libra Rises')  # Ascension de la balance
    print(f'{date(year, OCTOBER, 22)} Libra Sets')  # Descension de la balance
    print(f'{date(year, OCTOBER, 23)} Scorpio Rises')  # Ascension du scorpion
    print(f'{date(year, NOVEMBER, 21)} Scorpio Sets')  # Descension du scorpion
    print(f'{date(year, NOVEMBER, 22)} Sagittarius Rises')  # Ascension du sagittaire
    print(f'{date(year, DECEMBER, 21)} Sagittarius Sets')  # Descension du sagittaire
    print(f'{date(year, DECEMBER, 22)} Capricorn Rises')  # Ascension du capricorne
    print(f'{date(year, JANUARY, 19)} Capricorn Sets')  # Descension du capricorne
    print(f'{date(year, JANUARY, 20)} Aquarius Rises')  # Ascension du verseau
    print(f'{date(year, FEBRUARY, 18)} Aquarius Sets')  # Descension du verseau
    print(f'{date(year, FEBRUARY, 19)} Pisces Rises')  # Ascension des poissons
    print(f'{date(year, MARCH, 20)} Pisces Sets')  # Descension des poissons


if __name__ == '__main__':
    main()
