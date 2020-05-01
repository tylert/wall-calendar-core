#!/usr/bin/env python


from datetime import date

from pymeeus.Sun import Sun

from paper_cal import (closest_day, SUNDAY, MONDAY, WEDNESDAY,
                       THURSDAY, SATURDAY, WEEK1, WEEK2, WEEK3, JANUARY,
                       FEBRUARY, MAY, JULY, AUGUST, SEPTEMBER, OCTOBER,
                       NOVEMBER, DECEMBER)


def main():
    '''
    '''

    # https://en.wikipedia.org/wiki/Public_holidays_in_Canada
    # https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada

    for year in (2020, 2021, 2022):
        # New Year's Day is January 1st
        # https://en.wikipedia.org/wiki/New_Year's_Day
        # https://fr.wikipedia.org/wiki/Jour_de_l%27an
        print('{}'.format(date(year, JANUARY, 1)), end='')
        print(' New Year\'s Day')
        # Jour de l'an
        if date.weekday(date(year, JANUARY, 1)) == SATURDAY \
                or date.weekday(date(year, JANUARY, 1)) == SUNDAY:
            print(closest_day(MONDAY, year, JANUARY, 1), end='')
            print(' New Year\'s Day (observed)')
            # Jour de l'an (observé)

        # Groundhog Day is February 2nd
        # https://en.wikipedia.org/wiki/Groundhog_Day
        # https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
        print('{}'.format(date(year, FEBRUARY, 2)), end='')
        print(' Groundhog Day')
        # Jour de la marmotte

        # The 3rd Monday in February is observed in 6 provinces and 0
        # territories...
        #   CA-AB:  Family Day;  statutory
        #   CA-BC:  Family Day;  statutory
        #   CA-MB:  Louis Riel Day;  statutory
        #   CA-NB:  Family Day;  statutory
        #   CA-ON:  Family Day;  statutory
        #   CA-NS:  Heritage Day;  ?
        #   CA-PE:  Islander Day;  statutory
        #   CA-SK:  Family Day;  statutory
        # https://en.wikipedia.org/wiki/Family_Day
        # https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
        print(closest_day(MONDAY, year, FEBRUARY, WEEK3), end='')
        print(' Family Day')
        # Fête de la famille
        # Journée Louis Riel (CA-MB)
        # Fête des Insulaires (CA-PE)
        # Fête du Patrimoine (CA-NS)

        # March break
        # Congé de mars

        # https://en.wikipedia.org/wiki/Spring_break
        # Spring break
        # Congé de printemps

        spring_equinox = Sun.get_equinox_solstice(year, target='spring')
        summer_solstice = Sun.get_equinox_solstice(year, target='summer')
        autumn_equinox = Sun.get_equinox_solstice(year, target='autumn')
        winter_solstice = Sun.get_equinox_solstice(year, target='winter')

        _, temp_month, temp_day, _, _, _ = spring_equinox.get_full_date()
        print(date(year, temp_month, temp_day), end='')
        print(' First day of Spring')

        _, temp_month, temp_day, _, _, _ = summer_solstice.get_full_date()
        print(date(year, temp_month, temp_day), end='')
        print(' First day of Summer')

        _, temp_month, temp_day, _, _, _ = autumn_equinox.get_full_date()
        print(date(year, temp_month, temp_day), end='')
        print(' First day of Fall')

        _, temp_month, temp_day, _, _, _ = winter_solstice.get_full_date()
        print(date(year, temp_month, temp_day), end='')
        print(' First day of Winter')

        # Easter is the 1st Sunday after the 1st full moon after the Spring
        # equinox
        # https://en.wikipedia.org/wiki/Shrove_Tuesday
        # https://fr.wikipedia.org/wiki/Mardi_gras
        # https://en.wikipedia.org/wiki/Ash_Wednesday
        # https://fr.wikipedia.org/wiki/Mercredi_des_Cendres
        # https://en.wikipedia.org/wiki/Palm_Sunday
        # https://fr.wikipedia.org/wiki/Dimanche_des_Rameaux
        # https://en.wikipedia.org/wiki/Maundy_Thursday
        # https://fr.wikipedia.org/wiki/Jeudi_saint
        # https://en.wikipedia.org/wiki/Good_Friday
        # https://fr.wikipedia.org/wiki/Vendredi_saint
        # https://en.wikipedia.org/wiki/Easter
        # https://fr.wikipedia.org/wiki/P%C3%A2ques
        # https://en.wikipedia.org/wiki/Feast_of_the_Ascension
        # https://fr.wikipedia.org/wiki/Ascension_(f%C3%AAte)
        # https://en.wikipedia.org/wiki/Pentecost
        # https://fr.wikipedia.org/wiki/Pentec%C3%B4te
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

        # Victoria Day is the Monday on or before May 24th
        # (or the last Monday preceeding May 25th)
        # https://en.wikipedia.org/wiki/Victoria_Day
        # https://en.wikipedia.org/wiki/National_Patriots%27_Day
        # https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Reine_(Canada)
        print(closest_day(MONDAY, year, MAY, 21), end='')
        print(' Victoria Day')
        # Fête de la Reine
        # Fête de Victoria
        # Journée nationale des patriotes (CA-QC)

        # Canada Day is July 1st
        # https://en.wikipedia.org/wiki/Canada_Day
        # https://fr.wikipedia.org/wiki/F%C3%AAte_du_Canada
        print('{}'.format(date(year, JULY, 1)), end='')
        print(' Canada Day')
        # Fête du Canada
        if date.weekday(date(year, JULY, 1)) == SATURDAY \
                or date.weekday(date(year, JULY, 1)) == SUNDAY:
            print(closest_day(MONDAY, year, JULY, 1), end='')
            print(' Canada Day (observed)')
            # Fête du Canada (observé)

        # The 1st Monday in August is a quasi-semi-poly-un-statutory holiday,
        # kinda...
        #   CA-AB:  Heritage Day;  optional, formerly statutory
        #   CA-BC:  British Columbia Day;  statutory
        #   CA-MB:  Civic Holiday;  non-statutory
        #   CA-NB:  New Brunswick Day;  statutory
        #   CA-NL:  not observed
        #   CA-NS:  Natal Day;  non-statutory
        #   CA-NT:  Civic Holiday;  statutory
        #   CA-NU:  Civic Holiday;  statutory
        #   CA-ON:  Civic Holiday and Simcoe Day;  non-statutory
        #   CA-PE:  Civic Holiday;  statutory or non-statutory
        #   CA-QC:  not observed
        #   CA-SK:  Saskatchewan Day;  statutory
        #   CA-YT:  not observed
        # https://en.wikipedia.org/wiki/Civic_Holiday
        # https://en.wikipedia.org/wiki/Public_holidays_in_Canada
        # https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
        print(closest_day(MONDAY, year, AUGUST, WEEK1), end='')
        print(' August Civic Holiday')
        # Premier lundi d'août
        # Longue fin de semaine d'aôut

        # Labour Day is the 1st Monday in September
        # https://en.wikipedia.org/wiki/Labour_Day
        # https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
        print(closest_day(MONDAY, year, SEPTEMBER, WEEK1), end='')
        print(' Labour Day')
        # Fête du Travail

        # Canadian Thanksgiving is the 2nd Monday in October
        # https://en.wikipedia.org/wiki/Thanksgiving#Canada
        # https://fr.wikipedia.org/wiki/Action_de_gr%C3%A2ce_(Canada)
        print(closest_day(MONDAY, year, OCTOBER, WEEK2), end='')
        print(' Thanksgiving Day')
        # Action de Grâce

        # Rememberance Day is November 11th
        # https://en.wikipedia.org/wiki/Remembrance_Day
        # https://fr.wikipedia.org/wiki/Jour_du_Souvenir
        print('{}'.format(date(year, NOVEMBER, 11)), end='')
        print(' Rememberance Day')
        # Jour du Souvenir

        # Christmas Day is December 25th
        # https://en.wikipedia.org/wiki/Christmas
        # https://fr.wikipedia.org/wiki/No%C3%ABl
        print('{}'.format(date(year, DECEMBER, 25)), end='')
        print(' Christmas Day')
        # Noël
        # XXX FIXME TODO Xmas and Boxing Day too close together
        # if date.weekday(date(year, DECEMBER, 25)) == SATURDAY \
        #         or date.weekday(date(year, DECEMBER, 25)) == SUNDAY:
        #     print(closest_day(MONDAY, year, DECEMBER, 25), end='')
        #     print(' Christmas Day (observed)')

        # Boxing Day is December 26th
        # https://en.wikipedia.org/wiki/Boxing_Day
        # https://fr.wikipedia.org/wiki/Boxing_Day
        print('{}'.format(date(year, DECEMBER, 26)), end='')
        print(' Boxing Day')
        # Lendemain de Noël
        # Le jour des boîtes
        # Après-Noël
        # XXX FIXME TODO Xmas and Boxing Day too close together
        # if date.weekday(date(year, DECEMBER, 26)) == SATURDAY \
        #         or date.weekday(date(year, DECEMBER, 26)) == SUNDAY:
        #     print(closest_day(MONDAY, year, DECEMBER, 26), end='')
        #     print(' Boxing Day (observed)')


if __name__ == '__main__':
    main()
