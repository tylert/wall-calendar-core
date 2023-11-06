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

    #   https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_drapeau_national_du_Canada
    print(f'{date(year, FEBRUARY, 15)} Flag Day (CA)')
    # Jour du drapeau national du Canada

    # Heritage Day (CA-YT) is the Friday before the last Sunday in February
    #   https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
    print(
        f'{closest_date(SUNDAY, date(year, FEBRUARY, WEEK4), last=True) - timedelta(days=2)} Heritage Day (CA-YT)'
    )  # Fête du patrimoine (CA-YT)

    #   https://en.wikipedia.org/wiki/Commonwealth_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_Commonwealth
    print(f'{closest_date(MONDAY, date(year, MARCH, WEEK2))} Commonwealth Day')
    # Journée du Commonwealth

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

    #   https://en.wikipedia.org/wiki/Armed_Forces_Day
    #   https://fr.wikipedia.org/wiki/Jour_des_forces_arm%C3%A9es
    print(f'{closest_date(SUNDAY, date(year, JUNE, WEEK1))} Armed Forces Day (CA)')
    # Journée des forces armées (CA)
    # Journée des forces armées canadiennes (CA)
    # Canadian Armed Forces Day

    #   https://en.wikipedia.org/wiki/National_Aboriginal_Day
    #   https://en.wikipedia.org/wiki/National_Indigenous_Peoples_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_des_peuples_autochtones
    #   https://www.canada.ca/en/canadian-heritage/campaigns/indigenous-peoples-day.html
    #   https://www.canada.ca/fr/patrimoine-canadien/campagnes/journee-peuples-autochtones.html
    print(f'{date(year, JUNE, 21)} National Indigenous Peoples Day (CA)')
    # Journée nationale des peuples autochtones (CA)
    # National Aboriginal Day (CA)
    # Journée nationale des Autochthones (CA)

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
    if SATURDAY == date.weekday(date(year, JULY, 1)) or SUNDAY == date.weekday(
        date(year, JULY, 1)
    ):
        print(f'{closest_date(MONDAY, date(year, JULY, 1))} Canada Day Observed')
        # Fête du Canada observé

    #   https://en.wikipedia.org/wiki/Memorial_Day_(Newfoundland_and_Labrador)
    print(f'{date(year, JULY, 1)} Memorial Day (CA-NL)')

    #   https://en.wikipedia.org/wiki/Construction_Holiday_%28Quebec%29
    #   https://fr.wikipedia.org/wiki/Vacances_de_la_construction
    #   https://www.ccq.org/en/avantages-sociaux/dates-conges-vacances
    #   https://www.ccq.org/fr-CA/avantages-sociaux/dates-conges-vacances
    # The Quebec Construction Holiday begins on the 2nd last Sunday of July and
    # lasts for 2 weeks
    print(
        f'{closest_date(SUNDAY, date(year, JULY, WEEK4), last=True) - timedelta(days=7)} Construction Holiday Begins (CA-QC)'
    )  # Début des vacances de la construction (CA-QC)
    print(
        f'{closest_date(SUNDAY, date(year, JULY, WEEK4), last=True) + timedelta(days=6)} Construction Holiday Ends (CA-QC)'
    )  # Fin des vacances de la construction (CA-QC)

    #   https://en.wikipedia.org/wiki/International_Day_of_the_World's_Indigenous_Peoples
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_des_populations_autochtones
    print(
        f'{date(year, AUGUST, 9)} International Day of the World\'s Indigenous Peoples'
    )  # Journée internationale des populations autochtones du monde

    #   https://en.wikipedia.org/wiki/Discovery_Day
    print(f'{closest_date(MONDAY, date(year, AUGUST, WEEK3))} Discovery Day (CA-YT)')
    # Journée de la Découverte (CA-YT)

    print(
        f'{closest_date(FRIDAY, date(year, AUGUST, WEEK3))} Gold Cup Parade Day (CA-PE)'
    )  # Défilé de la Coupe d'or (CA-PE)

    #   https://en.wikipedia.org/wiki/Orange_Shirt_Day
    #   https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_de_la_v%C3%A9rit%C3%A9_et_de_la_r%C3%A9conciliation
    #   https://www.orangeshirtday.org/
    print(f'{date(year, SEPTEMBER, 30)} National Day for Truth and Reconciliation (CA)')
    # Journée nationale de la vérité et de la réconciliation (CA)
    # Orange Shirt Day (CA)
    # Journée du chandail orange (CA)

    #   https://en.wikipedia.org/wiki/Thanksgiving#Canada
    #   https://fr.wikipedia.org/wiki/Action_de_gr%C3%A2ce_(Canada)
    #   https://en.wikipedia.org/wiki/Oktoberfest
    #   https://fr.wikipedia.org/wiki/Oktoberfest
    # Oktoberfest (CA-ON) starts the Friday before Thanksgiving and ends the
    # Saturday after
    print(
        f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2))} Thanksgiving Day (CA)'
    )  # Action de grâce (CA)
    print(
        f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2)) - timedelta(days=3)} Oktoberfest Begins (CA-ON)'
    )  # Début de l'Oktoberfest (CA-ON)
    print(
        f'{closest_date(MONDAY, date(year, OCTOBER, WEEK2)) + timedelta(days=8)} Oktoberfest Ends (CA-ON)'
    )  # Fin de l'Oktoberfest (CA-ON)

    #   https://en.wikipedia.org/wiki/Remembrance_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_Souvenir
    #   https://en.wikipedia.org/wiki/Armistice_Day
    #   https://fr.wikipedia.org/wiki/Jour_du_Souvenir
    #   https://en.wikipedia.org/wiki/Merchant_Navy_(United_Kingdom)
    print(f'{date(year, NOVEMBER, 11)} Rememberance Day')  # Jour du Souvenir
    print(f'{date(year, NOVEMBER, 11)} Armistice Day (CA-NL)')
    # Jour de l'Armistice (CA-NL)
    print(f'{date(year, SEPTEMBER, 3)} Merchant Navy Day')
    # Merchant Navy Rememberance Day
    # Jour de la marine marchande

    #   https://en.wikipedia.org/wiki/Statute_of_Westminster_1931
    #   https://fr.wikipedia.org/wiki/Statut_de_Westminster_de_1931
    #   https://www.canada.ca/en/canadian-heritage/services/important-commemorative-days/anniversary-statute-westminster.html
    #   https://www.canada.ca/fr/patrimoine-canadien/services/journees-importantes-commemoratives/anniversaire-statut-westminster.html
    # The Statute of Westminster was enacted on December 11th, 1931
    print(
        f'{date(year, DECEMBER, 11)} {ordinal(year - 1931)} Anniversary of the Statute of Westminster'
    )  # Anniversaire du Statut de Westminster


if __name__ == '__main__':
    main()
