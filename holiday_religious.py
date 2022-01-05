#!/usr/bin/env python


from datetime import date

from pymeeus.Sun import Sun

from paper_cal import (closest_day, SUN, MON, TUE, SAT, WEEK1, WEEK2, WEEK3,
                       JAN, FEB, MAY, JUL, AUG, SEP, OCT, NOV, DEC)


def main():

    # https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    # https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada

    for year in (2022, 2023):
        # St. Valentine's Day is February 14th
        #   https://en.wikipedia.org/wiki/Valentine%27s_Day
        #   https://fr.wikipedia.org/wiki/Saint-Valentin
        print(f'{date(year, FEB, 14)} St. Valentine\'s Day')
        # Saint-Valentin

        spring_equinox = Sun.get_equinox_solstice(year, target='spring')
        summer_solstice = Sun.get_equinox_solstice(year, target='summer')
        autumn_equinox = Sun.get_equinox_solstice(year, target='autumn')
        winter_solstice = Sun.get_equinox_solstice(year, target='winter')

        _, temp_month, temp_day, _, _, _ = spring_equinox.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Spring')
        _, temp_month, temp_day, _, _, _ = summer_solstice.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Summer')
        _, temp_month, temp_day, _, _, _ = autumn_equinox.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Fall')
        _, temp_month, temp_day, _, _, _ = winter_solstice.get_full_date()
        print(f'{date(year, temp_month, temp_day)} First day of Winter')

        # Easter is the 1st Sunday after the 1st full moon after the Spring
        # equinox
        # (min:  March 22nd, max:  April 25th)
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
        # REM  [trigger(easter-47)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Shrove/Pancake Tuesday", "Mardi Gras")]%" %b%
        # REM  [trigger(easter-46)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Ash Wednesday", "Mercredi des Cendres")]%" %b%
        # REM  [trigger(easter-7)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Palm Sunday", "Dimanche des Rameaux")]%" %b%
        # REM  [trigger(easter-3)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Maundy Thursday", "Jeudi saint")]%" %b%
        # OMIT [trigger(easter-2)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Good Friday", "Vendredi saint")]%" %b%
        # OMIT [trigger(easter)]    +1 PRIORITY 1000 \
        #   MSG %"[babel("Easter Sunday", "Le dimanche de Pâques")]%" %b%
        # REM  [trigger(easter+1)]  +1 PRIORITY 1000 \
        #   MSG %"[babel("Easter Monday", "Le lundi de Pâques")]%" %b%
        # REM  [trigger(easter+39)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Ascension", "Ascension")]%" %b%
        # REM  [trigger(easter+49)] +1 PRIORITY 1000 \
        #   MSG %"[babel("Pentecost", "Pentecôte")]%" %b%

        # Christmas Eve is December 24th
        print(f'{date(year, DEC, 24)} Christmas Eve')
        # Veille de Noël

        # Christmas Day is December 25th
        #   https://en.wikipedia.org/wiki/Christmas
        #   https://fr.wikipedia.org/wiki/No%C3%ABl
        # Boxing Day is December 26th
        #   https://en.wikipedia.org/wiki/Boxing_Day
        #   https://fr.wikipedia.org/wiki/Boxing_Day
        print(f'{date(year, DEC, 25)} Christmas Day')
        # Noël
        print(f'{date(year, DEC, 26)} Boxing Day')
        # Lendemain de Noël
        # Le jour des boîtes
        # Après-Noël
        if date.weekday(date(year, DEC, 25)) == SAT:
            print(f'{closest_day(MON, date(year, DEC, 25))} Christmas Day (observed)')
            print(f'{closest_day(TUE, date(year, DEC, 26))} Boxing Day (observed)')
        if date.weekday(date(year, DEC, 25)) == SUN:
            print(f'{closest_day(TUE, date(year, DEC, 25))} Christmas Day (observed)')


if __name__ == '__main__':
    main()
