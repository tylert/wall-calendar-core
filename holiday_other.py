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

    #   https://en.wikipedia.org/wiki/(137108)_1999_AN10
    #   https://fr.wikipedia.org/wiki/(137108)_1999_AN10
    #   https://en.wikipedia.org/wiki/(35396)_1997_XF11
    #   https://fr.wikipedia.org/wiki/(35396)_1997_XF11
    if 2027 == year:
        print(f'{date(year, AUGUST, 7)} 06:48 1999 AN10 Asteroid Pass')
    if 2028 == year:
        print(f'{date(year, OCTOBER, 26)} 06:44 1997 XF11 Asteroid Pass')

    #   https://en.wikipedia.org/wiki/Daylight_saving_time_by_country
    #   https://en.wikipedia.org/wiki/Daylight_saving_time_in_Canada
    #   https://www.timeanddate.com/time/zones/y
    #   https://www.timeanddate.com/time/zones/r
    #   https://www.timeanddate.com/time/zones/q
    #   https://www.timeanddate.com/time/zones/z
    #   https://www.timeanddate.com/time/zones/a
    #   https://www.timeanddate.com/time/zones/b
    #   https://www.timeanddate.com/time/zones/m
    # DST Begins = "Spring forward"
    # DST Ends = "Fall back"
    #     UTC-12:00 -> Yankee
    #     UTC-05:00 -> Romeo
    #     UTC-04:00 -> Quebec
    #     UTC+00:00 -> Zulu
    #     UTC+01:00 -> Alpha
    #     UTC+02:00 -> Bravo
    #     UTC+12:00 -> Mike
    print(
        f'{closest_date(SUNDAY, date(year, MARCH, WEEK2))} 02:00 Daylight Savings Time Begins (CA, US)'
    )  # Heure d'éte commence (CA, US)
    print(
        f'{closest_date(SUNDAY, date(year, MARCH, WEEK4), last=True)} 01:00Z Daylight Savings Time Begins (EU, UK)'
    )  # Heure d'éte commence (EU, UK)
    print(
        f'{closest_date(SUNDAY, date(year, NOVEMBER, WEEK1))} 02:00 Daylight Savings Time Ends (CA, US)'
    )  # Heure d'éte termine (CA, US)
    print(
        f'{closest_date(SUNDAY, date(year, OCTOBER, WEEK4), last=True)} 01:00Z Daylight Savings Time Ends (EU, UK)'
    )  # Heure d'éte termine (EU, UK)

    #   https://en.wikipedia.org/wiki/Friday_The_13th
    #   https://fr.wikipedia.org/wiki/Vendredi_treize
    friday = repeat_date(closest_date(FRIDAY, date(year, JANUARY, 4)))
    for week in range(1, 55):
        found = next(friday)
        if year == found.year and 13 == found.day:
            print(f'{found} Friday the 13th')  # Vendredi treize

    #   https://www.canada.ca/en/canadian-heritage/services/important-commemorative-days.html
    #   https://www.canada.ca/fr/patrimoine-canadien/services/journees-importantes-commemoratives.html
    #   https://www.canada.ca/en/canadian-heritage/news/2022/01/statement-by-minister-hussen-on-raoul-wallenberg-day.html
    #   https://www.canada.ca/fr/patrimoine-canadien/nouvelles/2022/01/declaration-du-ministrehussen-a-loccasion-de-la-journee-raoulwallenberg.html
    #   https://en.wikipedia.org/wiki/Raoul_Wallenberg
    #   https://fr.wikipedia.org/wiki/Raoul_Wallenberg
    print(f'{date(year, JANUARY, 17)} Raoul Wallenburg Day')
    # Journée Raoul Wallenberg

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
    print(f'{date(year, APRIL, 22)} Earth Day')  # Jour de la Terre

    #   https://en.wikipedia.org/wiki/Anzac_Day
    print(f'{date(year, APRIL, 25)} ANZAC Day (AU, NZ)')
    # Jour d'ANZAC (AU, NZ)

    #   https://en.wikipedia.org/wiki/Mother's_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_des_M%C3%A8res
    #   https://en.wikipedia.org/wiki/Mothering_Sunday
    # Mothering Sunday (UK) is 4th Sunday of Lent / exactly 3 weeks before Easter Sunday
    print(f'{closest_date(SUNDAY, date(year, MAY, WEEK2))} Mother\'s Day')
    print(f'{easter(year) - timedelta(days=21)} Mothering Sunday (UK)')
    # Fête des mères

    #   https://en.wikipedia.org/wiki/Armed_Forces_Day
    #   https://fr.wikipedia.org/wiki/Jour_des_forces_arm%C3%A9es
    #   https://en.wikipedia.org/wiki/Memorial_Day
    #   https://fr.wikipedia.org/wiki/Memorial_Day
    print(f'{closest_date(SATURDAY, date(year, MAY, WEEK2))} Armed Forces Week (US)')
    print(f'{closest_date(SATURDAY, date(year, MAY, WEEK3))} Armed Forces Day (US)')
    # Journée des forces armées (US)
    print(
        f'{closest_date(MONDAY, date(year, MAY, WEEK4), last=True)} Memorial Day (US)'
    )

    #   https://en.wikipedia.org/wiki/Flag_Day_(United_States)
    print(f'{date(year, JUNE, 14)} Flag Day (US)')  # Jour du drapeau (US)

    #   https://en.wikipedia.org/wiki/Father's_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_des_P%C3%A8res
    print(f'{closest_date(SUNDAY, date(year, JUNE, WEEK3))} Father\'s Day')
    # Fête des pères

    #   https://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
    print(f'{date(year, JULY, 4)} Independence Day (US)')
    # Jour de l'indépendance (US)

    #   https://en.wikipedia.org/wiki/Columbus_Day
    print(f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2))} Columbus Day (US)')
    # Jour de Columbus (US)

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
        print(f'{date(year, JUNE, 2)} Spring Bank Holiday (UK)')
        print(f'{date(year, JUNE, 3)} Platinum Jubilee Bank Holiday (UK)')
    else:
        print(
            f'{closest_date(MONDAY, date(year, MAY, WEEK4), last=True)} Spring Bank Holiday (UK)'
        )
    print(
        f'{closest_date(MONDAY, date(year, AUGUST, WEEK4), last=True)} Summer Bank Holiday (UK)'
    )

    #   https://en.wikipedia.org/wiki/Guy_Fawkes_Night
    print(f'{date(year, NOVEMBER, 5)} Guy Fawkes Day (UK)')
    # Journée de Guy Fawkes (UK)

    #   https://en.wikipedia.org/wiki/Veterans_Day
    #   https://fr.wikipedia.org/wiki/Veterans_Day
    #   https://en.wikipedia.org/wiki/Armistice_Day
    #   https://fr.wikipedia.org/wiki/Jour_de_l%27Armistice
    print(f'{date(year, NOVEMBER, 11)} Veterans Day (US)')
    # Journée des anciens combattants (US)
    print(f'{date(year, NOVEMBER, 11)} Armistice Day (UK)')
    # Jour de l'Armistice (UK)

    #   https://en.wikipedia.org/wiki/Hogmanay
    #   https://fr.wikipedia.org/wiki/Hogmanay
    print(f'{date(year, DECEMBER, 31)} Hogmanay (UK)')

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

    #   https://en.wikipedia.org/wiki/List_of_minor_secular_observances

    #   https://en.wikipedia.org/wiki/Employee_Appreciation_Day
    print(
        f'{closest_date(FRIDAY, date(year, MARCH, WEEK1))} Employee Appreciation Day (CA, US)'
    )

    #   https://en.wikipedia.org/wiki/International_Cat_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_du_chat
    #   https://en.wikipedia.org/wiki/National_Cat_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_du_chat
    # Caturday!!!
    print(f'{date(year, FEBRUARY, 17)} National Cat Day (BR, IT)')
    print(f'{date(year, FEBRUARY, 22)} National Cat Day (JP)')
    print(f'{date(year, MARCH, 1)} National Cat Day (RU)')
    print(f'{date(year, AUGUST, 8)} National Cat Day (CA)')
    print(f'{date(year, AUGUST, 8)} International Cat Day')
    print(f'{date(year, OCTOBER, 29)} National Cat Day (US)')

    #   https://en.wikipedia.org/wiki/Caps_lock#International_Caps_Lock_Day
    print(f'{date(year, JUNE, 28)} INTERNATIONAL CAPS LOCK DAY')
    print(f'{date(year, OCTOBER, 22)} INTERNATIONAL CAPS LOCK DAY')
    # JOURNÉE INTERNATIONALE DU VERROUILLAGE DES MAJUSCULES

    #   https://en.wikipedia.org/wiki/Day_of_the_Programmer
    if is_leap(year):
        print(f'{date(year, SEPTEMBER, 12)} Day of the Programmer 256th day')
        # Jour du programmeur 256e jour
    else:
        print(f'{date(year, SEPTEMBER, 13)} Day of the Programmer 256th day')
        # Jour du programmeur 256e jour

    #   https://en.wikipedia.org/wiki/Software_Freedom_Day
    print(
        f'{closest_date(SATURDAY, date(year, SEPTEMBER, WEEK3))} Software Freedom Day'
    )  # Journée de la liberté des logiciels

    #   http://worldradioday.org
    print(f'{date(year,FEBRUARY, 13)} World Radio Day')
    # Journée mondiale de la radio

    #   http://iaru.org/world-amateur-radio-day.html
    print(f'{date(year, APRIL, 18)} World Amateur Radio Day')
    # Journée de la radio amateur

    #   https://en.wikipedia.org/wiki/Pi_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_de_pi
    #   https://piday.org/
    #   https://tauday.com/
    #   https://piapproximationday.com/
    print(f'{date(year, MARCH, 14)} Pi Day 3.14')  # Journée de pi 3.14
    print(f'{date(year, JUNE, 28)} Tau Day 6.28')  # Journée de tau 6.28
    print(f'{date(year, JULY, 22)} Pi Approximation Day 22/7')
    if is_leap(year):
        print(f'{date(year, NOVEMBER, 9)} Pi Approximation Day 314th day')
    else:
        print(f'{date(year, NOVEMBER, 10)} Pi Approximation Day 314th day')
    # Journée d'approximation pi 22/7
    # Journée d'approximation pi 314e jour

    #   https://en.wikipedia.org/wiki/Nikola_Tesla
    #   https://fr.wikipedia.org/wiki/Nikola_Tesla
    #   https://nikolatesladay.com/
    print(f'{date(year, JULY, 10)} Nikola Tesla Day')

    #   https://en.wikipedia.org/wiki/Ada_Lovelace_Day
    #   http://findingada.com/about/when-is-ald/
    print(f'{closest_date(TUESDAY, date(year, OCTOBER, WEEK2))} Ada Lovelace Day')
    # Journée de Ada Lovelace

    #   https://en.wikipedia.org/wiki/Darwin_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_Darwin
    print(f'{date(year, FEBRUARY, 12)} Darwin Day')
    # Journée de Darwin

    #   https://en.wikipedia.org/wiki/International_Lefthanders_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_des_gauchers
    print(f'{date(year, AUGUST, 13)} Left-Handers\' Day')
    # Journée internationale des gauchers

    print(f'{date(year, FEBRUARY, 20)} {ordinal(year - 1991)} Birthday of Python')
    if is_leap(year):
        print(
            f'{date(year, FEBRUARY, 29)} {ordinal(year - 2012)} Birthday of Raspberry Pi'
        )
    else:
        print(
            f'{date(year, FEBRUARY, 28)} {ordinal(year - 2012)} Birthday of Raspberry Pi'
        )
    print(f'{date(year, MARCH, 11)} {ordinal(year - 2002)} Birthday of Arch')
    print(f'{date(year, MARCH, 15)} {ordinal(year - 2013)} Birthday of Docker')
    print(f'{date(year, MARCH, 18)} {ordinal(year - 1985)} Birthday of GNU Manifesto')
    print(f'{date(year, MARCH, 21)} {ordinal(year - 1993)} Birthday of NetBSD')
    print(f'{date(year, APRIL, 16)} {ordinal(year - 1971)} Birthday of FTP')
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
