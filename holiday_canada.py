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
            f'{closest_date(MONDAY, date(year, JANUARY, 1))} New Year\'s Day Observed'
        )  # Jour de l'an Observé

    #   https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_drapeau_national_du_Canada
    print(f'{date(year, FEBRUARY, 15)} Flag Day (CA)')
    # Jour du drapeau national du Canada

    # The 3rd Monday in February is observed in 8 provinces and 0
    # territories...
    #     CA-AB:  Family Day;  statutory
    #     CA-BC:  Family Day;  statutory
    #     CA-MB:  Louis Riel Day;  statutory
    #     CA-NB:  Family Day;  statutory
    #     CA-NL:  not observed
    #     CA-NS:  Heritage Day;  statutory
    #     CA-NT:  not observed
    #     CA-NU:  not observed
    #     CA-ON:  Family Day;  statutory
    #     CA-PE:  Islander Day;  statutory
    #     CA-QC:  not observed
    #     CA-SK:  Family Day;  statutory
    #     CA-YT:  not observed
    #   https://en.wikipedia.org/wiki/Family_Day
    #   https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
    print(
        f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} Family Day (CA-AB, CA-BC, CA-NB, CA-ON, CA-SK)'
    )  # Fête de la famille (CA-AB, CA-BC, CA-NB, CA-ON, CA-SK)
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} Louis Riel Day (CA-MB)')
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} Islander Day (CA-PE)')
    print(f'{closest_date(MONDAY, date(year, FEBRUARY, WEEK3))} Heritage Day (CA-NS)')
    # Journée Louis Riel (CA-MB)
    # Fête des insulaires (CA-PE)
    # Jour de patrimoine / Fête du patrimoine (CA-NS)

    # Heritage Day (CA-YT) is the Friday before the last Sunday in February
    #   https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
    print(
        f'{closest_date(SUNDAY, date(year, FEBRUARY, WEEK4), last=True) - timedelta(days=2)} Heritage Day (CA-YT))'
    )  # Jour de patrimoine / Fête du patrimoine (CA-YT)

    #   https://en.wikipedia.org/wiki/Commonwealth_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_Commonwealth
    print(f'{closest_date(MONDAY, date(year, MARCH, WEEK2))} Commonwealth Day')
    # Journée du Commonwealth

    # March Break
    # Congé de mars

    #   https://en.wikipedia.org/wiki/Spring_break
    # Spring Break
    # Congé de printemps

    print(f'{spring(year).date()} {spring(year).time().strftime("%H%Mh")} First day of Spring')
    print(f'{summer(year).date()} {summer(year).time().strftime("%H%Mh")} First day of Summer')
    print(f'{autumn(year).date()} {autumn(year).time().strftime("%H%Mh")} First day of Fall')
    print(f'{winter(year).date()} {winter(year).time().strftime("%H%Mh")} First day of Winter')

    print(f'{perihelion(year).date()} {perihelion(year).time().strftime("%H%Mh")} Perihelion')
    print(f'{aphelion(year).date()} {aphelion(year).time().strftime("%H%Mh")} Aphelion')

    # Victoria Day is the Monday before May 25th
    #   https://en.wikipedia.org/wiki/Victoria_Day
    #   https://en.wikipedia.org/wiki/National_Patriots%27_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Reine_(Canada)
    print(f'{closest_date(MONDAY, date(year, MAY, 21))} Victoria Day (CA)')
    # Fête de la Reine
    # Fête de Victoria
    # Journée nationale des patriotes (CA-QC)

    #   https://en.wikipedia.org/wiki/National_Aboriginal_Day
    #   https://en.wikipedia.org/wiki/National_Indigenous_Peoples_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_des_peuples_autochtones
    #   https://www.canada.ca/en/canadian-heritage/campaigns/indigenous-peoples-day.html
    #   https://www.canada.ca/fr/patrimoine-canadien/campagnes/journee-peuples-autochtones.html
    print(f'{date(year, JUNE, 21)} National Indigenous Peoples Day (CA)')
    # Journée nationale des peuples autochtones (CA)

    #   https://en.wikipedia.org/wiki/Discovery_Day
    print(f'{closest_date(MONDAY, date(year, JUNE, 24))} June Day (CA-NL)')

    #   https://en.wikipedia.org/wiki/Multiculturalism_in_Canada
    #   https://www.canada.ca/en/canadian-heritage/campaigns/multiculturalism-day.html
    #   https://www.canada.ca/fr/patrimoine-canadien/campagnes/journee-multiculturalisme.html
    print(f'{date(year, JUNE, 27)} Canadian Multiculturalism Day')
    # Journée canadienne du multiculturalisme

    #   https://en.wikipedia.org/wiki/Canada_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Canada
    print(f'{date(year, JULY, 1)} Canada Day')  # Fête du Canada
    if (
        date.weekday(date(year, JULY, 1)) == SATURDAY
        or date.weekday(date(year, JULY, 1)) == SUNDAY
    ):
        print(f'{closest_date(MONDAY, date(year, JULY, 1))} Canada Day Observed')
        # Fête du Canada Observé

    #   https://en.wikipedia.org/wiki/Nunavut_Day
    print(f'{date(year, JULY, 9)} Nunavut Day ᓄᓇᕗᑦ ᐅᓪᓗᖓ  (CA-NU)')
    # Fête du Nunavut (CA-NU)

    # The Quebec Construction Holiday begins on the 2nd last Sunday of July and
    # lasts for 2 weeks
    #   https://en.wikipedia.org/wiki/Construction_Holiday_%28Quebec%29
    #   https://fr.wikipedia.org/wiki/Vacances_de_la_construction
    #   https://www.ccq.org/en/avantages-sociaux/dates-conges-vacances
    #   https://www.ccq.org/fr-CA/avantages-sociaux/dates-conges-vacances
    print(
        f'{closest_date(SUNDAY, date(year, JULY, WEEK4), last=True) - timedelta(days=7)} Construction Holiday Begins (CA-QC)'
    )  # Début des vacances de la construction (CA-QC)
    print(
        f'{closest_date(SUNDAY, date(year, JULY, WEEK4), last=True) + timedelta(days=6)} Construction Holiday Ends (CA-QC)'
    )  # Fin des vacances de la construction (CA-QC)

    # The 1st Monday in August is a quasi-semi-poly-un-statutory holiday,
    # kinda...
    #     CA-AB:  Heritage Day;  optional, formerly statutory
    #     CA-BC:  British Columbia Day;  statutory
    #     CA-MB:  Terry Fox Day;  non-statutory
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
    print(
        f'{closest_date(MONDAY, date(year, AUGUST, WEEK1))} Civic Holiday (except CA-NL, CA-QC, CA-YT)'
    )  # Congé civique (sauf CA-NL, CA-QC, CA-YT)
    # Premier lundi d'août

    #   https://en.wikipedia.org/wiki/International_Day_of_the_World's_Indigenous_Peoples
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_des_populations_autochtones
    print(
        f'{date(year, AUGUST, 9)} International Day of the World\'s Indigenous Peoples'
    )  # Journée internationale des populations autochtones du monde

    #   https://en.wikipedia.org/wiki/Discovery_Day
    print(f'{closest_date(MONDAY, date(year, AUGUST, WEEK3))} Discovery Day (CA-YT)')
    # Journée découverte (CA-YT)

    # Merchant Navy Rememberance Day (CA) is September 3rd
    #   https://en.wikipedia.org/wiki/Remembrance_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_Souvenir
    #   https://en.wikipedia.org/wiki/Merchant_Navy_(United_Kingdom)
    print(f'{date(year, SEPTEMBER, 3)} Merchant Navy Day')
    # Jour de la marine marchande

    #   https://en.wikipedia.org/wiki/Labour_Day
    #   https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
    print(f'{closest_date(MONDAY, date(year, SEPTEMBER, WEEK1))} Labour Day')
    # Fête du Travail

    #   https://en.wikipedia.org/wiki/Orange_Shirt_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_de_la_v%C3%A9rit%C3%A9_et_de_la_r%C3%A9conciliation
    #   https://www.orangeshirtday.org/
    print(f'{date(year, SEPTEMBER, 30)} Orange Shirt Day (CA)')
    # Jour du chandail orange (CA)
    # National Day for Truth and Reconciliation (CA)
    # Journée nationale de la vérité et de la réconciliation (CA)

    #   https://en.wikipedia.org/wiki/Thanksgiving#Canada
    #   https://fr.wikipedia.org/wiki/Action_de_gr%C3%A2ce_(Canada)
    #   https://en.wikipedia.org/wiki/Oktoberfest
    #   https://fr.wikipedia.org/wiki/Oktoberfest
    # Oktoberfest (CA-ON) starts the Friday before Thanksgiving and ends the
    # Saturday after
    print(
        f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2))} Thanksgiving Day (CA)'
    )  # Action de Grâce (CA)
    print(
        f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2)) - timedelta(days=3)} Oktoberfest Begins (CA-ON)'
    )  # Début de l'Oktoberfest (CA-ON)
    print(
        f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2)) + timedelta(days=8)} Oktoberfest Ends (CA-ON)'
    )  # Fin de l'Oktoberfest (CA-ON)

    #   https://en.wikipedia.org/wiki/Remembrance_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_Souvenir
    #   https://en.wikipedia.org/wiki/Armistice_Day
    print(f'{date(year, NOVEMBER, 11)} Rememberance Day')  # Jour du Souvenir
    print(f'{date(year, NOVEMBER, 11)} Armistice Day (CA-NL)')
    # Jour de l'Armistice (CA-NL)

    #   https://en.wikipedia.org/wiki/Statute_of_Westminster_1931
    #   https://fr.wikipedia.org/wiki/Statut_de_Westminster_de_1931
    # The Statute of Westminster was enacted on December 11th, 1931
    # Anniversary of the Statute of Westminster
    # Anniversaire du Statut de Westminster


if __name__ == '__main__':
    main()
