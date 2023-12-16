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

    # XXX FIXME TODO  Do a much better job with the moon phases!!!
    for month in range(1, 13):
        print(f'{new_moon(date(year, month, 16)).date()} New Moon')
        print(f'{first_moon(date(year, month, 16)).date()} First Moon')
        print(f'{full_moon(date(year, month, 16)).date()} Full Moon')
        print(f'{last_moon(date(year, month, 16)).date()} Last Moon')

    #// XXX FIXME TODO  St. Francis Day
    #// XXX FIXME TODO  St. Nicholas Day
    #// XXX FIXME TODO  Our Lady of Guadalupe
    #// XXX FIXME TODO  Posadas Navidenas
    #// XXX FIXME TODO  Holy Innocents
    #// XXX FIXME TODO  Nativity Fast begins
    #// XXX FIXME TODO  Feast of the Nativity
    #// XXX FIXME TODO  Nativity of Virgin Mary
    #// XXX FIXME TODO  Ecclesiastical year begins

    #   https://en.wikipedia.org/wiki/Nowruz
    #   https://fr.wikipedia.org/wiki/Norouz
    # Persian/Zoroastrian/Baha'i
    print(f'{spring(year).date()} Nowruz')  # Norouz

    #   https://en.wikipedia.org/wiki/South_and_Southeast_Asian_solar_New_Year
    #   https://en.wikipedia.org/wiki/New_Year%27s_Day#New_Year's_Days_in_other_calendars
    #   https://en.wikipedia.org/wiki/Pahela_Baishakh
    # print(f'{date(year, APRIL, 13)}')

    # 10th day of the 7th month (Ashvin) on the Hindu calendar
    #   https://en.wikipedia.org/wiki/Dasara
    #   https://en.wikipedia.org/wiki/Vijayadashami
    #   https://fr.wikipedia.org/wiki/Dussehra
    # in 7th month (Ashvin) on the Hindu calendar
    #   https://en.wikipedia.org/wiki/Navaratri
    #   https://fr.wikipedia.org/wiki/Navratri
    # 20 days after Vijayadashami/Dussehra/Dasara/Dasain
    #   https://en.wikipedia.org/wiki/Diwali
    #   https://fr.wikipedia.org/wiki/Divali
    print(f'{new_moon(date(year, OCTOBER, 16)).date() - timedelta(days=4)} Diwali')

    #   https://en.wikipedia.org/wiki/Lunar_New_Year#Middle_East
    #   https://fr.wikipedia.org/wiki/Nouvel_An_lunaire#Calendrier_h%C3%A9bra%C3%AFque
    #   https://en.wikipedia.org/wiki/Nisan
    #   https://fr.wikipedia.org/wiki/Nissan_(mois)
    print(f'{heb_date(NISAN, 1, year)} Aviv')

    #   https://en.wikipedia.org/wiki/Passover
    #   https://fr.wikipedia.org/wiki/Pessa%27h
    #   https://en.wikipedia.org/wiki/Pascha
    #   https://en.wikipedia.org/wiki/Passover_(Christian_holiday)
    #   https://en.wikipedia.org/wiki/Passover_Seder
    #   https://fr.wikipedia.org/wiki/S%C3%A9der_de_Pessa%27h
    #   https://en.wikipedia.org/wiki/Nisan
    #   https://fr.wikipedia.org/wiki/Nissan_(mois)
    # Passover begins on 14 or 15 Nisan and goes until 21 or 22 Nisan
    print(f'{heb_date(NISAN, 14, year)} Passover Begins')  # Pessa'h
    print(f'{heb_date(NISAN, 22, year)} Passover Ends')
    # Début de Pâque des Juifs
    # Fin de Pâque des Juifs
    # Passover = Pesach = Pascha = Jewish Easter

    #   https://en.wikipedia.org/wiki/Shavuot
    #   https://fr.wikipedia.org/wiki/Chavouot
    #   XXX FIXME TODO  Add more links!!!
    # Shauvot or Pentecost is 6 and 7 Sivan or the Sunday following
    print(f'{heb_date(SIVAN, 6, year)} Shauvot')  # Chavouot
    # print(f'{heb_date(SIVAN, 6, year)} Shauvot Begins')  # Début de Chavouot
    # print(f'{heb_date(SIVAN, 7, year)} Shauvot Ends')  # Fin de Chavouot

    #   https://en.wikipedia.org/wiki/Rosh_Hashanah
    #   https://fr.wikipedia.org/wiki/Roch_Hachana
    #   https://en.wikipedia.org/wiki/Tishrei
    #   https://fr.wikipedia.org/wiki/Tishri
    print(f'{heb_date(TISHREI, 1, year)} Rosh Hashanah')
    # print(f'{heb_date(TISHREI, 1, year)} Rosh Hashanah Begins')  # Début de Roch Hachana
    # print(f'{heb_date(TISHREI, 2, year)} Rosh Hashanah Ends')  # Fin de Roch Hachana
    # Jewish New Year

    #   https://en.wikipedia.org/wiki/Yom_Kippur
    #   https://fr.wikipedia.org/wiki/Yom_Kippour
    #   https://en.wikipedia.org/wiki/Tishrei
    #   https://fr.wikipedia.org/wiki/Tishri
    print(f'{heb_date(TISHREI, 10, year)} Yom Kippur')  # Yom Kippour

    #   https://en.wikipedia.org/wiki/Sukkot
    #   https://fr.wikipedia.org/wiki/Souccot
    #   https://en.wikipedia.org/wiki/Tishrei
    #   https://fr.wikipedia.org/wiki/Tishri
    print(f'{heb_date(TISHREI, 15, year)} Sukkot Begins')  # Début de Souccot
    print(f'{heb_date(TISHREI, 21, year)} Sukkot Ends')  # Fin de Souccot
    # a.k.a. Tabernacles

    #   https://en.wikipedia.org/wiki/Hanukkah
    #   https://fr.wikipedia.org/wiki/Hanoucca
    #   XXX FIXME TODO  Add more links!!!
    print(f'{heb_date(KISLEV, 25, year)} Hanukkah Begins')  # Début de Hanoucca
    print(f'{heb_date(TEVET, 2, year)} Hanukkah Ends')  # Fin de Hanoucca

    #   https://en.wikipedia.org/wiki/Purim
    #   https://fr.wikipedia.org/wiki/Pourim
    #   XXX FIXME TODO  Add more links!!!
    #   XXX FIXME TODO  What happens when the year is "short"???
    # print(f'{heb_date(ADAR, 14, year)} Purim')  # Pourim

    #   https://en.wikipedia.org/wiki/Ramadan
    #   https://fr.wikipedia.org/wiki/Ramadan
    #   https://en.wikipedia.org/wiki/Eid_al-Fitr
    #   https://fr.wikipedia.org/wiki/A%C3%AFd_el-Fitr
    #   https://en.wikipedia.org/wiki/Ramadan_(calendar_month)
    #   https://en.wikipedia.org/wiki/Shawwal
    #   https://fr.wikipedia.org/wiki/Chawwal
    print(f'{isl_date(RAMADAN, 1, year)} Month of Ramadan Begins')
    print(f'{isl_date(SHAWWAL, 1, year)} Eid al-Fitr Begins')

    #   https://en.wikipedia.org/wiki/Eid_al-Adha
    #   https://fr.wikipedia.org/wiki/A%C3%AFd_al-Adha
    #   https://en.wikipedia.org/wiki/Dhu_al-Hijjah
    #   https://fr.wikipedia.org/wiki/Dhou_al-hijja
    print(f'{isl_date(DHU_AL_HIJJAH, 10, year)} Eid al-Adha Begins')


if __name__ == '__main__':
    main()
