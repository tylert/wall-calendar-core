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

    # XXX FIXME TODO  Do a much better job with the moon phases!!!
    for month in range(1, 13):
        print(f'{new_moon(date(year, month, 16)).date()} New Moon')
        print(f'{first_moon(date(year, month, 16)).date()} First Moon')
        print(f'{full_moon(date(year, month, 16)).date()} Full Moon')
        print(f'{last_moon(date(year, month, 16)).date()} Last Moon')

    #   https://en.wikipedia.org/wiki/Epiphany_(holiday)
    #   https://fr.wikipedia.org/wiki/%C3%89piphanie
    #   https://es.wikipedia.org/wiki/Epifan%C3%ADa
    #   https://en.wikipedia.org/wiki/Biblical_Magi
    #   https://fr.wikipedia.org/wiki/Rois_mages
    #   https://es.wikipedia.org/wiki/Reyes_Magos
    #   https://en.wikipedia.org/wiki/Baptism_of_the_Lord
    # Baptism of the Lord is the 1st Sunday after January 6th
    # Jesus
    print(f'{date(year, JANUARY, 6)} Epiphany')  # Épiphanie / Epifanía
    print(
        f'{date(year, JANUARY, 6)} Reyes (ES)'
    )  # La festividad de los Reyes Magos???
    print(f'{closest_date(SUNDAY, date(year, JANUARY, 10))} Baptism of the Lord')

    #   https://en.wikipedia.org/wiki/Annunciation
    #   https://fr.wikipedia.org/wiki/Annonciation
    print(f'{date(year, MARCH, 25)} Annunciation')  # Annonciation

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
