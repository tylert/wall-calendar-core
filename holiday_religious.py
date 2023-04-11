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
    ''' '''

    # XXX FIXME TODO  Do a much better job with the moon phases!!!
    for month in range(1, 13):
        print(f'{new_moon(date(year, month, 16)).date()} New Moon')
        print(f'{first_moon(date(year, month, 16)).date()} First Moon')
        print(f'{full_moon(date(year, month, 16)).date()} Full Moon')
        print(f'{last_moon(date(year, month, 16)).date()} Last Moon')

    #   https://en.wikipedia.org/wiki/Epiphany_(holiday)
    #   https://fr.wikipedia.org/wiki/%C3%89piphanie
    #   https://en.wikipedia.org/wiki/Baptism_of_the_Lord
    # Baptism of the Lord is the 1st Sunday after January 6th
    # Jesus
    print(f'{date(year, JANUARY, 6)} Epiphany')  # Epiphanie
    print(f'{closest_date(SUNDAY, date(year, JANUARY, 10))} Baptism of the Lord')

    #   https://en.wikipedia.org/wiki/Conversion_of_Paul_the_Apostle
    #   https://fr.wikipedia.org/wiki/Conversion_de_Paul
    print(f'{date(year, JANUARY, 25)} Conversion of St. Paul')
    # Conversion de Paul

    #   https://en.wikipedia.org/wiki/Valentine%27s_Day
    #   https://fr.wikipedia.org/wiki/Saint-Valentin
    print(f'{date(year, FEBRUARY, 14)} St. Valentine\'s Day')  # Saint-Valentin

    #   https://en.wikipedia.org/wiki/Saint_David%27s_Day
    #   https://fr.wikipedia.org/wiki/Saint_David%27s_Day
    #   https://en.wikipedia.org/wiki/Saint_Patrick%27s_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Saint-Patrick
    #   https://en.wikipedia.org/wiki/Saint_George%27s_Day
    #   https://fr.wikipedia.org/wiki/Sant_Jordi
    #   https://en.wikipedia.org/wiki/Saint_Andrew%27s_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Saint-Andr%C3%A9
    # St. Patrick's Day (CA-NL) is the Monday nearest March 17th
    # St. George's Day (CA-NL) is the Monday nearest April 23rd
    print(f'{date(year, MARCH, 1)} St. David\'s Day')
    print(f'{date(year, MARCH, 17)} St. Patrick\'s Day')
    print(f'{closest_date(MONDAY, date(year, MARCH, 17))} St. Patrick\'s Day (CA-NL)')
    print(f'{closest_date(MONDAY, date(year, APRIL, 23))} St. George\'s Day (CA-NL)')
    print(f'{date(year, APRIL, 23)} St. George\'s Day')
    print(f'{date(year, NOVEMBER, 30)} St. Andrew\'s Day')
    # Fête de la Saint-David (UK)
    # Fête de la Saint-Patrick
    # Fête de la Saint-Patrick (CA-NL)
    # Fête de la Saint-Georges (CA-NL) (UK)
    # Fête de la Saint-André (UK)

    #   https://en.wikipedia.org/wiki/Annunciation
    #   https://fr.wikipedia.org/wiki/Annonciation
    print(f'{date(year, MARCH, 25)} Annunciation')  # Annonciation

    #   https://en.wikipedia.org/wiki/Ecclesiastical_full_moon
    #   https://en.wikipedia.org/wiki/Computus
    #   https://en.wikipedia.org/wiki/Date_of_Easter
    #   https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques
    #   https://en.wikipedia.org/wiki/Shrove_Tuesday
    #   https://fr.wikipedia.org/wiki/Mardi_gras
    #   https://en.wikipedia.org/wiki/Ash_Wednesday
    #   https://fr.wikipedia.org/wiki/Mercredi_des_Cendres
    #   https://en.wikipedia.org/wiki/Lent
    #   https://fr.wikipedia.org/wiki/Car%C3%AAme
    #   https://en.wikipedia.org/wiki/Palm_Sunday
    #   https://fr.wikipedia.org/wiki/Dimanche_des_Rameaux
    #   https://en.wikipedia.org/wiki/Holy_Wednesday
    #   https://fr.wikipedia.org/wiki/Mercredi_saint
    #   https://en.wikipedia.org/wiki/Maundy_Thursday
    #   https://fr.wikipedia.org/wiki/Jeudi_saint
    #   https://en.wikipedia.org/wiki/Good_Friday
    #   https://fr.wikipedia.org/wiki/Vendredi_saint
    #   https://en.wikipedia.org/wiki/Holy_Saturday
    #   https://fr.wikipedia.org/wiki/Samedi_saint
    #   https://en.wikipedia.org/wiki/Easter
    #   https://fr.wikipedia.org/wiki/P%C3%A2ques
    #   https://en.wikipedia.org/wiki/Easter_Saturday
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
    print(
        f'{easter(year) - timedelta(days=46)} Carnival/Ash Wednesday'
    )  # Mercredi des Cendres
    # Lent / Carême
    print(f'{easter(year) - timedelta(days=7)} Palm Sunday')  # Dimanche des Rameaux
    print(f'{easter(year) - timedelta(days=4)} Holy Wednesday')  # Mercredi saint
    print(f'{easter(year) - timedelta(days=3)} Maundy Thursday')  # Jeudi saint
    print(f'{easter(year) - timedelta(days=2)} Good Friday')  # Vendredi saint
    print(f'{easter(year) - timedelta(days=1)} Holy Saturday')  # Samedi saint
    print(f'{easter(year)} Easter Sunday')  # Dimanche de Pâques
    print(f'{easter(year) + timedelta(days=1)} Easter Monday')  # Lundi de Pâques
    print(f'{easter(year) + timedelta(days=6)} Easter Saturday')
    print(f'{easter(year) + timedelta(days=39)} Ascension Day')  # Ascension
    print(
        f'{easter(year) + timedelta(days=49)} Whit Sunday/Pentecost Sunday'
    )  # Pentecôte
    print(f'{easter(year) + timedelta(days=50)} Whit Monday/Pentecost Monday')
    print(f'{easter(year) + timedelta(days=56)} Trinity Sunday')
    print(f'{easter(year) + timedelta(days=60)} Corpus Christi')
    # XXX FIXME TODO  Palm Sunday Orthodox???

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
    print(f'{heb_date(SIVAN, 6, year)} Shauvot Begins')  # Début de Chavouot
    print(f'{heb_date(SIVAN, 7, year)} Shauvot Ends')  # Fin de Chavouot

    #   https://en.wikipedia.org/wiki/Rosh_Hashanah
    #   https://fr.wikipedia.org/wiki/Roch_Hachana
    #   https://en.wikipedia.org/wiki/Tishrei
    #   https://fr.wikipedia.org/wiki/Tishri
    print(f'{heb_date(TISHREI, 1, year)} Rosh Hashanah')
    # print(f'{heb_date(TISHREI, 1, year)} Rosh Hashanah Begins')
    # print(f'{heb_date(TISHREI, 2, year)} Rosh Hashanah Ends')
    # Jewish New Year
    # Début de Roch Hachana
    # Fin de Roch Hachana

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
    print(f'{heb_date(KISLEV, 25, year)} Hanukkah Begins')
    print(f'{heb_date(TEVET, 2, year)} Hanukkah Ends')
    # Début de Hanoucca
    # Fin de Hanoucca

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

    #   https://en.wikipedia.org/wiki/Saint-Jean-Baptiste_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_nationale_du_Qu%C3%A9bec
    #   https://en.wikipedia.org/wiki/John_the_Baptist
    #   https://fr.wikipedia.org/wiki/Jean_le_Baptiste
    #   https://en.wikipedia.org/wiki/Nativity_of_St_John_the_Baptist
    print(f'{date(year, JUNE, 24)} Saint-Jean-Baptiste Day')
    # Fête nationale du Québec
    # St. John the Baptist's Day
    # Fête de la Saint-Jean-Baptiste
    # Nativity of St. John the Baptist
    # Nativité de saint Jean-Baptiste

    #   https://en.wikipedia.org/wiki/Orangemen%27s_Day
    #   https://fr.wikipedia.org/wiki/Orange_Day
    #   https://en.wikipedia.org/wiki/The_Twelfth#The_Twelfth_outside_Northern_Ireland
    print(f'{closest_date(MONDAY, date(year, JULY, 12))} Orangemen\'s Day (CA-NL)')
    # Battle of the Boyne???
    # Fête des Orangistes (CA-NL)

    #   https://en.wikipedia.org/wiki/All_Saints%27_Day
    #   https://fr.wikipedia.org/wiki/Toussaint
    #   https://en.wikipedia.org/wiki/All_Souls%27_Day
    #   https://fr.wikipedia.org/wiki/Comm%C3%A9moration_des_fid%C3%A8les_d%C3%A9funts
    print(f'{date(year, NOVEMBER, 1)} All Saints\' Day')  # Toussaint
    print(f'{date(year, NOVEMBER, 2)} All Souls\' Day')  # Fête des Morts

    #   https://en.wikipedia.org/wiki/Christmas_Eve
    #   https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_No%C3%ABl
    #   https://en.wikipedia.org/wiki/Christmas
    #   https://fr.wikipedia.org/wiki/No%C3%ABl
    #   https://en.wikipedia.org/wiki/Boxing_Day
    #   https://fr.wikipedia.org/wiki/Boxing_Day
    print(f'{date(year, DECEMBER, 24)} Christmas Eve')  # Veille de Noël
    print(f'{date(year, DECEMBER, 25)} Christmas Day')  # Noël
    print(f'{date(year, DECEMBER, 26)} Boxing Day')  # Le jour des boîtes
    # Lendemain de Noël
    # Après-Noël
    if SATURDAY == date.weekday(date(year, DECEMBER, 25)):
        print(
            f'{closest_date(MONDAY, date(year, DECEMBER, 25))} Christmas Day Observed'
        )  # Noël observé
        print(f'{closest_date(TUESDAY, date(year, DECEMBER, 26))} Boxing Day Observed')
        # Le jour des boîtes observé
    if SUNDAY == date.weekday(date(year, DECEMBER, 25)):
        print(
            f'{closest_date(TUESDAY, date(year, DECEMBER, 25))} Christmas Day Observed'
        )  # Noël observé


if __name__ == '__main__':
    main()
