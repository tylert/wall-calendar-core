package main

import (
	"fmt"
	"time"
)

func englishCanada(year uint32) {
	var t time.Time

	// https://en.wikipedia.org/wiki/Public_holidays_in_Canada
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
	// https://en.wikipedia.org/wiki/Lists_of_holidays

	// December 31st, January 1st
	// https://en.wikipedia.org/wiki/New_Year's_Eve
	// https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_la_Saint-Sylvestre
	// https://en.wikipedia.org/wiki/New_Year's_Day
	// https://fr.wikipedia.org/wiki/Jour_de_l%27an
	// Veille du Nouvel An, Jour de l'an, Jour de l'an observé
	t = find_date(fmt.Sprintf("%d-12-31", year))
	print_date(t, "New Year's Eve")
	t = find_date(fmt.Sprintf("%d-01-01", year))
	print_date(t, "New Year's Day")
	if t.Weekday() == time.Sunday {
		t = t.AddDate(0, 0, 1)
		print_date(t, "New Year's Day Observed")
	} else if t.Weekday() == time.Saturday {
		t = t.AddDate(0, 0, 2)
		print_date(t, "New Year's Day Observed")
	}

	// January 17th
	// https://www.canada.ca/en/canadian-heritage/services/important-commemorative-days.html
	// https://www.canada.ca/fr/patrimoine-canadien/services/journees-importantes-commemoratives.html
	// https://www.canada.ca/en/canadian-heritage/news/2022/01/statement-by-minister-hussen-on-raoul-wallenberg-day.html
	// https://www.canada.ca/fr/patrimoine-canadien/nouvelles/2022/01/declaration-du-ministrehussen-a-loccasion-de-la-journee-raoulwallenberg.html
	// https://en.wikipedia.org/wiki/Raoul_Wallenberg
	// https://fr.wikipedia.org/wiki/Raoul_Wallenberg
	// Journée Raoul Wallenberg
	t = find_date(fmt.Sprintf("%d-01-17", year))
	print_date(t, "Raoul Wallenburg Day")

	// January 25th
	// https://en.wikipedia.org/wiki/Conversion_of_Paul_the_Apostle
	// https://fr.wikipedia.org/wiki/Conversion_de_Paul
	// Conversion de Paul
	t = find_date(fmt.Sprintf("%d-01-25", year))
	print_date(t, "Conversion of St. Paul")

	// February 2nd
	// https://en.wikipedia.org/wiki/Groundhog_Day
	// https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
	// Jour de la marmotte
	t = find_date(fmt.Sprintf("%d-02-02", year))
	print_date(t, "Groundhog Day")

	// February 14th
	// https://en.wikipedia.org/wiki/Valentine%27s_Day
	// https://fr.wikipedia.org/wiki/Saint-Valentin
	// Saint-Valentin
	t = find_date(fmt.Sprintf("%d-02-14", year))
	print_date(t, "St. Valentine's Day")

	// February 15th
	// https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day
	// https://fr.wikipedia.org/wiki/Jour_du_drapeau_national_du_Canada
	// Jour du drapeau national du Canada
	t = find_date(fmt.Sprintf("%d-02-15", year))
	print_date(t, "Flag Day (CA)")

	// 3rd Monday in February
	// https://en.wikipedia.org/wiki/Family_Day
	// https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
	// https://fr.wikipedia.org/wiki/Jour_de_Louis_Riel
	// Fête de la famille, Journée Louis Riel (CA-MB), Fête des Insulaires (CA-PE), Journée du patrimoine (CA-NS)
	t = find_nearby_date(fmt.Sprintf("%d-02-18", year), uint32(time.Monday))
	print_date(t, "Family Day (CA-AB, CA-BC, CA-NB, CA-ON, CA-SK)")
	print_date(t, "Louis Riel Day (CA-MB)")
	print_date(t, "Heritage Day (CA-NS)")
	print_date(t, "Islander Day (CA-PE)")

	// the Friday before the last Sunday in February
	// https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
	// Fête du patrimoine (CA-YT)
	t = find_nearby_date(fmt.Sprintf("%d-02-28", year), uint32(time.Sunday))
	t = t.AddDate(0, 0, -2)
	print_date(t, "Heritage Day (CA-YT)")

	// the Monday nearest March 17th
	// the Monday nearest April 23rd
	// https://en.wikipedia.org/wiki/Saint_David%27s_Day
	// https://fr.wikipedia.org/wiki/Saint_David%27s_Day
	// https://en.wikipedia.org/wiki/Saint_Patrick%27s_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Saint-Patrick
	// https://en.wikipedia.org/wiki/Saint_George%27s_Day
	// https://fr.wikipedia.org/wiki/Sant_Jordi
	// https://en.wikipedia.org/wiki/Saint_Andrew%27s_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Saint-Andr%C3%A9
	// Fête de la Saint-David
	// Fête de la Saint-Patrick
	// Fête de la Saint-Georges
	// Fête de la Saint-André
	t = find_date(fmt.Sprintf("%d-03-01", year))
	print_date(t, "St. David's Day")
	t = find_date(fmt.Sprintf("%d-03-17", year))
	print_date(t, "St. Patrick's Day")
	t = find_nearby_date(fmt.Sprintf("%d-03-17", year), uint32(time.Monday))
	print_date(t, "St. Patrick's Day (CA-NL)")
	t = find_nearby_date(fmt.Sprintf("%d-04-23", year), uint32(time.Monday))
	print_date(t, "St. George's Day (CA-NL)")
	t = find_date(fmt.Sprintf("%d-04-23", year))
	print_date(t, "St. George's Day")
	t = find_date(fmt.Sprintf("%d-11-30", year))
	print_date(t, "St. Andrew's Day")

	// 2nd Sunday in March, 1st Sunday in November
	// last Sunday in March, last Sunday in October
	// https://en.wikipedia.org/wiki/Daylight_saving_time_in_Canada
	// https://en.wikipedia.org/wiki/Daylight_saving_time_by_country
	// https://en.wikipedia.org/wiki/Military_time_zone
	// https://fr.wikipedia.org/wiki/Liste_des_zones_horaires_militaires
	//   UTC-12:00 Yankee, UTC-11:00 X-ray,   UTC-10:00 Whiskey
	//   UTC-09:00 Victor, UTC-08:00 Uniform, UTC-07:00 Tango
	//   UTC-06:00 Sierra, UTC-05:00 Romeo,   UTC-04:00 Quebec
	//   UTC-03:00 Papa,   UTC-02:00 Oscar,   UTC-01:00 November
	//   UTC+00:00 Zulu
	//   UTC+01:00 Alpha,  UTC+02:00 Bravo,   UTC+03:00 Charlie
	//   UTC+04:00 Delta,  UTC+05:00 Echo,    UTC+06:00 Foxtrot
	//   UTC+07:00 Golf,   UTC+08:00 Hotel,   UTC+09:00 India
	//   UTC+10:00 Kilo,   UTC+11:00 Lima,    UTC+12:00 Mike
	// DST Begins = "Spring forward", DST Ends = "Fall back"
	// Heure d'éte commence, Heure d'éte termine
	t = find_nearby_date(fmt.Sprintf("%d-03-11", year), uint32(time.Sunday))
	print_date(t, "02:00 DST Begins (CA, US)")
	t = find_nearby_date(fmt.Sprintf("%d-11-04", year), uint32(time.Sunday))
	print_date(t, "02:00 DST Ends (CA, US)")
	t = find_nearby_date(fmt.Sprintf("%d-03-31", year), uint32(time.Sunday))
	print_date(t, "01:00Z DST Begins (EU, UK)")
	t = find_nearby_date(fmt.Sprintf("%d-10-31", year), uint32(time.Sunday))
	print_date(t, "01:00Z DST Ends (EU, UK)")

	// 1st Friday in March
	// https://en.wikipedia.org/wiki/Employee_Appreciation_Day
	t = find_nearby_date(fmt.Sprintf("%d-03-04", year), uint32(time.Friday))
	print_date(t, "Employee Appreciation Day (AU, CA, IN, SG, US, UK)")

	// 2nd Monday in March
	// https://en.wikipedia.org/wiki/Commonwealth_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_Commonwealth
	// Journée du Commonwealth
	t = find_nearby_date(fmt.Sprintf("%d-03-11", year), uint32(time.Monday))
	print_date(t, "Commonwealth Day")

	// XXX FIXME TODO  Describe a bit how this date is calculated
	// https://en.wikipedia.org/wiki/Ecclesiastical_full_moon
	// https://en.wikipedia.org/wiki/Computus
	// https://en.wikipedia.org/wiki/Date_of_Easter
	// https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques
	// https://en.wikipedia.org/wiki/Shrove_Tuesday
	// https://fr.wikipedia.org/wiki/Mardi_gras
	// https://en.wikipedia.org/wiki/Ash_Wednesday
	// https://fr.wikipedia.org/wiki/Mercredi_des_Cendres
	// https://en.wikipedia.org/wiki/Lent
	// https://fr.wikipedia.org/wiki/Car%C3%AAme
	// https://en.wikipedia.org/wiki/Palm_Sunday
	// https://fr.wikipedia.org/wiki/Dimanche_des_Rameaux
	// https://en.wikipedia.org/wiki/Holy_Wednesday
	// https://fr.wikipedia.org/wiki/Mercredi_saint
	// https://en.wikipedia.org/wiki/Maundy_Thursday
	// https://fr.wikipedia.org/wiki/Jeudi_saint
	// https://en.wikipedia.org/wiki/Good_Friday
	// https://fr.wikipedia.org/wiki/Vendredi_saint
	// https://es.wikipedia.org/wiki/Viernes_Santo
	// https://en.wikipedia.org/wiki/Holy_Saturday
	// https://fr.wikipedia.org/wiki/Samedi_saint
	// https://en.wikipedia.org/wiki/Easter
	// https://fr.wikipedia.org/wiki/P%C3%A2ques
	// https://es.wikipedia.org/wiki/Pascua
	// https://en.wikipedia.org/wiki/Easter_Saturday
	// https://en.wikipedia.org/wiki/Feast_of_the_Ascension
	// https://fr.wikipedia.org/wiki/Ascension_(f%C3%AAte)
	// https://en.wikipedia.org/wiki/Pentecost
	// https://fr.wikipedia.org/wiki/Pentec%C3%B4te
	// https://www.timeanddate.com/holidays/common/carnival-wednesday
	// https://www.timeanddate.com/holidays/common/palm-sunday
	// https://www.timeanddate.com/holidays/common/maundy-thursday
	// https://www.timeanddate.com/holidays/common/good-friday
	// https://www.timeanddate.com/holidays/common/holy-saturday
	// https://www.timeanddate.com/holidays/common/easter-monday
	// https://www.timeanddate.com/holidays/common/ascension-day
	// https://www.timeanddate.com/holidays/common/whit-sunday
	// https://www.timeanddate.com/holidays/common/whit-monday
	// https://www.timeanddate.com/holidays/common/trinity
	// https://www.timeanddate.com/holidays/common/corpus-christi
	// Pascua (ES) = Easter
	// Mardi Gras
	// Mercredi des Cendres
	// Lent / Carême
	// Dimanche des Rameaux
	// Mercredi saint
	// Jeudi saint
	// Vendredi saint, Viernes Santo (ES)
	// Samedi saint
	// Dimanche de Pâques
	// Lundi de Pâques
	// Ascension
	// Pentecôte
	// XXX FIXME TODO  Palm Sunday Orthodox???
	month, day := Gregorian(int(year))
	easter := find_date(fmt.Sprintf("%d-%02d-%02d", year, month, day))
	t = easter.AddDate(0, 0, -47)
	print_date(t, "Shrove/Pancake Tuesday")
	t = easter.AddDate(0, 0, -46)
	print_date(t, "Carnival/Ash Wednesday")
	t = easter.AddDate(0, 0, -7)
	print_date(t, "Palm Sunday")
	t = easter.AddDate(0, 0, -4)
	print_date(t, "Holy Wednesday")
	t = easter.AddDate(0, 0, -3)
	print_date(t, "Maundy Thursday")
	t = easter.AddDate(0, 0, -2)
	print_date(t, "Good Friday")
	t = easter.AddDate(0, 0, -1)
	print_date(t, "Holy Saturday")
	print_date(easter, "Easter Sunday")
	t = easter.AddDate(0, 0, 1)
	print_date(t, "Easter Monday")
	t = easter.AddDate(0, 0, 6)
	print_date(t, "Easter Saturday")
	t = easter.AddDate(0, 0, 39)
	print_date(t, "Ascension Day")
	t = easter.AddDate(0, 0, 49)
	print_date(t, "Whit/Pentecost Sunday")
	t = easter.AddDate(0, 0, 50)
	print_date(t, "Whit/Pentecost Monday")
	t = easter.AddDate(0, 0, 56)
	print_date(t, "Trinity Sunday")
	t = easter.AddDate(0, 0, 60)
	print_date(t, "Corpus Christi")

	// April 1st
	// https://en.wikipedia.org/wiki/April_Fools'_Day
	// https://fr.wikipedia.org/wiki/Poisson_d%27avril
	// Poisson d'avril
	t = find_date(fmt.Sprintf("%d-04-01", year))
	print_date(t, "April Fool's Day")

	// April 6th
	// https://en.wikipedia.org/wiki/Tartan_Day
	// https://fr.wikipedia.org/wiki/Tartan_Day
	// Journée du Tartan
	t = find_date(fmt.Sprintf("%d-04-06", year))
	print_date(t, "Tartan Day")

	// April 9th
	// https://en.wikipedia.org/wiki/Vimy_Ridge_Day
	// Jour de la crête de Vimy
	t = find_date(fmt.Sprintf("%d-04-09", year))
	print_date(t, "Vimy Ridge Day")

	// April 22nd
	// https://en.wikipedia.org/wiki/Earth_Day
	// https://fr.wikipedia.org/wiki/Jour_de_la_Terre
	// Jour de la Terre
	t = find_date(fmt.Sprintf("%d-04-22", year))
	print_date(t, "Earth Day")

	// the Monday before May 25th
	// https://en.wikipedia.org/wiki/Victoria_Day
	// https://en.wikipedia.org/wiki/National_Patriots%27_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Reine_(Canada)
	// https://en.wikipedia.org/wiki/King%27s_Official_Birthday
	// https://fr.wikipedia.org/wiki/Anniversaire_officiel_du_roi
	// Fête de la Reine, Fête de Victoria, Journée nationale des patriotes (CA-QC)
	t = find_nearby_date(fmt.Sprintf("%d-05-21", year), uint32(time.Monday))
	print_date(t, "Victoria Day (CA)")
	print_date(t, "National Patriot's Day (CA-QC)")

	// 1st Sunday in June
	// https://en.wikipedia.org/wiki/Armed_Forces_Day
	// https://fr.wikipedia.org/wiki/Jour_des_forces_arm%C3%A9es
	// Journée des forces armées (CA)
	// Journée des forces armées canadiennes (CA)
	// Canadian Armed Forces Day
	t = find_nearby_date(fmt.Sprintf("%d-06-04", year), uint32(time.Sunday))
	print_date(t, "Armed Forces Day (CA)")

	// June 19th
	// https://en.wikipedia.org/wiki/Upper_Canada
	// https://fr.wikipedia.org/wiki/Haut-Canada
	// https://en.wikipedia.org/wiki/Constitutional_history_of_Canada
	// https://fr.wikipedia.org/wiki/Histoire_constitutionnelle_du_Canada
	// https://www.ontario.ca/laws/statute/97u42
	// https://www.ontario.ca/fr/lois/loi/97u42
	t = find_date(fmt.Sprintf("%d-06-19", year))
	print_date(t, "Loyalist Day (CA-ON)")

	// June 21st
	// https://en.wikipedia.org/wiki/National_Aboriginal_Day
	// https://en.wikipedia.org/wiki/National_Indigenous_Peoples_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_des_peuples_autochtones
	// https://www.canada.ca/en/canadian-heritage/campaigns/indigenous-peoples-day.html
	// https://www.canada.ca/fr/patrimoine-canadien/campagnes/journee-peuples-autochtones.html
	// Journée nationale des peuples autochtones (CA)
	// National Aboriginal Day (CA)
	// Journée nationale des Autochthones (CA)
	t = find_date(fmt.Sprintf("%d-06-21", year))
	print_date(t, "National Indigenous Peoples Day (CA)")

	// June 24th
	// https://en.wikipedia.org/wiki/Discovery_Day
	// https://en.wikipedia.org/wiki/Saint-Jean-Baptiste_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_nationale_du_Qu%C3%A9bec
	// https://en.wikipedia.org/wiki/John_the_Baptist
	// https://fr.wikipedia.org/wiki/Jean_le_Baptiste
	// https://en.wikipedia.org/wiki/Nativity_of_St_John_the_Baptist
	// Fête nationale du Québec
	// St. John the Baptist's Day
	// Fête de la Saint-Jean-Baptiste
	// Nativity of St. John the Baptist
	// Nativité de saint Jean-Baptiste
	// observé
	t = find_date(fmt.Sprintf("%d-06-24", year))
	print_date(t, "June Day (CA-NL)")
	print_date(t, "Saint-Jean-Baptiste Day")
	if t.Weekday() == time.Sunday {
		t = t.AddDate(0, 0, 1)
		print_date(t, "Saint-Jean-Baptiste Day Observed")
	} // else if t.Weekday() == time.Saturday {
	// XXX FIXME TODO  The rules are vague about what happens if this is on a Saturday
	// }

	// June 27th
	// https://en.wikipedia.org/wiki/Multiculturalism_in_Canada
	// https://www.canada.ca/en/canadian-heritage/campaigns/multiculturalism-day.html
	// https://www.canada.ca/fr/patrimoine-canadien/campagnes/journee-multiculturalisme.html
	// Journée canadienne du multiculturalisme
	t = find_date(fmt.Sprintf("%d-06-27", year))
	print_date(t, "Canadian Multiculturalism Day")

	// July 1st
	// https://en.wikipedia.org/wiki/Canada_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_du_Canada
	// https://en.wikipedia.org/wiki/Memorial_Day_(Newfoundland_and_Labrador)
	// Fête du Canada, Fête du Canada observé
	t = find_date(fmt.Sprintf("%d-07-01", year))
	print_date(t, "Memorial Day (CA-NL)")
	print_date(t, "Canada Day")
	if t.Weekday() == time.Sunday {
		t = t.AddDate(0, 0, 1)
		print_date(t, "Canada Day Observed")
	} else if t.Weekday() == time.Saturday {
		t = t.AddDate(0, 0, 2)
		print_date(t, "Canada Day Observed")
	}

	// July 9th
	// https://en.wikipedia.org/wiki/Nunavut_Day
	// Fête du Nunavut (CA-NU)
	t = find_date(fmt.Sprintf("%d-07-09", year))
	print_date(t, "Nunavut Day ᓄᓇᕗᑦ ᐅᓪᓗᖓ  (CA-NU)")

	// July 12th
	// https://en.wikipedia.org/wiki/Orangemen%27s_Day
	// https://fr.wikipedia.org/wiki/Orange_Day
	// https://en.wikipedia.org/wiki/The_Twelfth#The_Twelfth_outside_Northern_Ireland
	// Battle of the Boyne
	// Fête des Orangistes (CA-NL)
	t = find_date(fmt.Sprintf("%d-07-12", year))
	print_date(t, "Orangemen's Day (CA-NL)")

	// begins on the 2nd last Sunday of July
	// ends 2 weeks later
	// https://en.wikipedia.org/wiki/Construction_Holiday_%28Quebec%29
	// https://fr.wikipedia.org/wiki/Vacances_de_la_construction
	// https://www.ccq.org/en/avantages-sociaux/dates-conges-vacances
	// https://www.ccq.org/fr-CA/avantages-sociaux/dates-conges-vacances
	// Début des vacances de la construction (CA-QC)
	// Fin des vacances de la construction (CA-QC)
	t = find_nearby_date(fmt.Sprintf("%d-07-31", year), uint32(time.Sunday))
	t = t.AddDate(0, 0, -7)
	print_date(t, "Construction Holiday Begins (CA-QC)")
	t = t.AddDate(0, 0, 14)
	print_date(t, "Construction Holiday Ends (CA-QC)")

	// 1st Monday in August
	// https://en.wikipedia.org/wiki/Civic_Holiday
	// https://en.wikipedia.org/wiki/Public_holidays_in_Canada
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
	// Simcoe Day (CA-ON)
	// Jour férié, Premier lundi d'août, Congé civique
	// Fête du patrimoine (CA-AB), Jour de la Colombie-Britannique (CA-BC)
	// Jour de Nouveau Brunswick (CA-NB), Jour de la Fondation (CA-NS)
	// Jour de Saskatchewan (CA-SK)
	t = find_nearby_date(fmt.Sprintf("%d-08-04", year), uint32(time.Monday))
	print_date(t, "Civic Holiday (CA-NL, CA-NT, CA-NU, CA-ON)")
	print_date(t, "Heritage Day (CA-AB)")
	print_date(t, "British Columbia Day (CA-BC)")
	print_date(t, "Terry Fox Day (CA-MB)")
	print_date(t, "New Brunswick Day (CA-NB)")
	print_date(t, "Natal Day (CA-NS)")
	print_date(t, "Saskatchewan Day (CA-SK)")

	// August 9th
	// https://en.wikipedia.org/wiki/International_Day_of_the_World's_Indigenous_Peoples
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_des_populations_autochtones
	// Journée internationale des populations autochtones du monde
	t = find_date(fmt.Sprintf("%d-08-09", year))
	print_date(t, "International Day of the World's Indigenous Peoples")

	// 3rd Monday in August
	// https://en.wikipedia.org/wiki/Discovery_Day
	// Journée de la Découverte (CA-YT)
	t = find_nearby_date(fmt.Sprintf("%d-08-18", year), uint32(time.Monday))
	print_date(t, "Discovery Day (CA-YT)")

	// 3rd Friday in August
	// https://en.wikipedia.org/wiki/Public_holidays_in_Canada
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
	// Défilé de la Coupe d'or (CA-PE)
	t = find_nearby_date(fmt.Sprintf("%d-08-18", year), uint32(time.Friday))
	print_date(t, "Gold Cup Parade Day (CA-PE)")

	// 1st Monday in September
	// https://en.wikipedia.org/wiki/Labour_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
	// Fête du Travail
	t = find_nearby_date(fmt.Sprintf("%d-09-04", year), uint32(time.Monday))
	print_date(t, "Labour Day")

	// September 30th
	// https://en.wikipedia.org/wiki/Public_holidays_in_Canada
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
	// https://en.wikipedia.org/wiki/Orange_Shirt_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_de_la_v%C3%A9rit%C3%A9_et_de_la_r%C3%A9conciliation
	// https://www.orangeshirtday.org/
	// Journée de la vérité et de la réconciliation (CA)
	// Orange Shirt Day (CA)
	// Journée du chandail orange (CA)
	t = find_date(fmt.Sprintf("%d-09-30", year))
	print_date(t, "Truth and Reconciliation Day (CA)")

	// October 10th
	// https://en.wikipedia.org/wiki/World_Mental_Health_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_mondiale_de_la_sant%C3%A9_mentale
	t = find_date(fmt.Sprintf("%d-10-10", year))
	print_date(t, "World Mental Health Day")

	// 2nd Monday in October
	// the Friday before 2nd Monday in October, ends the Saturday after
	// https://en.wikipedia.org/wiki/Thanksgiving#Canada
	// https://fr.wikipedia.org/wiki/Action_de_gr%C3%A2ce_(Canada)
	// https://en.wikipedia.org/wiki/Oktoberfest
	// https://fr.wikipedia.org/wiki/Oktoberfest
	// Action de grâce (CA)
	// Début de l'Oktoberfest, Fin de l'Oktoberfest (CA-ON)
	t = find_nearby_date(fmt.Sprintf("%d-10-11", year), uint32(time.Monday))
	print_date(t, "Thanksgiving Day (CA)")
	t = t.AddDate(0, 0, -3)
	print_date(t, "Oktoberfest Begins (CA-ON)")
	t = t.AddDate(0, 0, 8)
	print_date(t, "Oktoberfest Ends (CA-ON)")

	// October 31st, November 1st, 2nd
	// https://en.wikipedia.org/wiki/Allhallowtide
	// https://en.wikipedia.org/wiki/Halloween
	// https://fr.wikipedia.org/wiki/Halloween
	// https://en.wikipedia.org/wiki/All_Saints%27_Day
	// https://fr.wikipedia.org/wiki/Toussaint
	// https://en.wikipedia.org/wiki/All_Souls%27_Day
	// https://fr.wikipedia.org/wiki/Comm%C3%A9moration_des_fid%C3%A8les_d%C3%A9funts
	// https://en.wikipedia.org/wiki/Day_of_the_Dead
	// https://fr.wikipedia.org/wiki/Jour_des_morts_(Mexique)
	// Toussaint, Fête des Morts
	t = find_date(fmt.Sprintf("%d-10-31", year))
	print_date(t, "Hallowe'en")
	print_date(t, "All Hallows' Eve")
	t = find_date(fmt.Sprintf("%d-11-01", year))
	print_date(t, "All Hallows' Day")
	print_date(t, "All Saints' Day")
	t = find_date(fmt.Sprintf("%d-11-02", year))
	print_date(t, "All Souls' Day")

	// November 11th, September 3rd
	// https://en.wikipedia.org/wiki/Remembrance_Day
	// https://fr.wikipedia.org/wiki/Jour_du_Souvenir
	// https://en.wikipedia.org/wiki/Armistice_Day
	// https://fr.wikipedia.org/wiki/Jour_du_Souvenir
	// https://en.wikipedia.org/wiki/Veterans_Day
	// https://fr.wikipedia.org/wiki/Veterans_Day
	// https://en.wikipedia.org/wiki/Armistice_Day
	// https://fr.wikipedia.org/wiki/Jour_de_l%27Armistice
	// https://en.wikipedia.org/wiki/Merchant_Navy_(United_Kingdom)
	// Jour du Souvenir
	// Jour de l'Armistice (CA-NL, UK)
	// Journée des anciens combattants (US)
	// Merchant Navy Rememberance Day
	// Jour de la marine marchande
	t = find_date(fmt.Sprintf("%d-11-11", year))
	print_date(t, "Rememberance Day")
	print_date(t, "Armistice Day (CA-NL, UK)")
	print_date(t, "Veterans Day (US)")
	t = find_date(fmt.Sprintf("%d-09-03", year))
	print_date(t, "Merchant Navy Day")

	// December 11th, 1931
	// https://en.wikipedia.org/wiki/Statute_of_Westminster_1931
	// https://fr.wikipedia.org/wiki/Statut_de_Westminster_de_1931
	// https://www.canada.ca/en/canadian-heritage/services/important-commemorative-days/anniversary-statute-westminster.html
	// https://www.canada.ca/fr/patrimoine-canadien/services/journees-importantes-commemoratives/anniversaire-statut-westminster.html
	// Anniversaire du Statut de Westminster
	t = find_date(fmt.Sprintf("%d-12-11", year))
	print_date(t, fmt.Sprintf("%s Anniversary of the Statute of Westminster", ordinal(int(year-1931), "en")))

	// 1st Saturday in December
	// https://canlii.org/en/on/laws/stat/so-2015-c-12/latest/so-2015-c-12.html
	// https://canlii.org/fr/on/legis/lois/lo-2015-c-12/derniere/lo-2015-c-12.html
	t = find_nearby_date(fmt.Sprintf("%d-12-04", year), uint32(time.Saturday))
	print_date(t, "Christmas Tree Day (CA-ON)")

	// December 8th
	// https://en.wikipedia.org/wiki/Immaculate_Conception
	// https://fr.wikipedia.org/wiki/Immacul%C3%A9e_Conception
	// https://es.wikipedia.org/wiki/Inmaculada_Concepci%C3%B3n
	// La Inmaculada
	t = find_date(fmt.Sprintf("%d-12-08", year))
	print_date(t, "Immaculate Conception Day")

	// 4th Sunday before December 25th
	// https://en.wikipedia.org/wiki/Advent
	// https://fr.wikipedia.org/wiki/Avent
	// https://en.wikipedia.org/wiki/Advent_Sunday
	// https://fr.wikipedia.org/wiki/Premier_dimanche_de_l%27Avent
	// https://en.wikipedia.org/wiki/Christmas_tree
	// https://fr.wikipedia.org/wiki/Sapin_de_No%C3%ABl
	t = find_nearby_date(fmt.Sprintf("%d-12-21", year), uint32(time.Sunday))
	t = t.AddDate(0, 0, -21)
	print_date(t, "Advent Sunday")

	// December 24th, 25th, 26th
	// https://en.wikipedia.org/wiki/Christmastide
	// https://fr.wikipedia.org/wiki/Temps_de_No%C3%ABl
	// https://en.wikipedia.org/wiki/Christmas_Eve
	// https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_No%C3%ABl
	// https://en.wikipedia.org/wiki/Christmas
	// https://fr.wikipedia.org/wiki/No%C3%ABl
	// https://es.wikipedia.org/wiki/Navidad
	// https://en.wikipedia.org/wiki/Boxing_Day
	// https://fr.wikipedia.org/wiki/Boxing_Day
	// https://en.wikipedia.org/wiki/Saint_Stephen%27s_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Saint-%C3%89tienne
	// https://es.wikipedia.org/wiki/D%C3%ADa_de_San_Esteban
	// Veille de Noël
	// Noël, Navidad
	// Le jour des boîtes, Lendemain de Noël, Après-Noël
	// Fête de la Saint-Étienne, Día de San Esteban
	// Noël observé, Le jour des boîtes observé
	t = find_date(fmt.Sprintf("%d-12-24", year))
	print_date(t, "Christmas Eve")
	t = find_date(fmt.Sprintf("%d-12-25", year))
	print_date(t, "Christmas Day")
	if t.Weekday() == time.Sunday {
		t = t.AddDate(0, 0, 1)
		print_date(t, "Christmas Day Observed")
	} else if t.Weekday() == time.Saturday {
		t = t.AddDate(0, 0, 2)
		print_date(t, "Christmas Day Observed")
	}
	t = find_date(fmt.Sprintf("%d-12-26", year))
	print_date(t, "St. Stephen's Day")
	print_date(t, "Boxing Day")
	if t.Weekday() == time.Sunday {
		t = t.AddDate(0, 0, 1)
		print_date(t, "Boxing Day Observed")
	} else if t.Weekday() == time.Saturday {
		t = t.AddDate(0, 0, 2)
		print_date(t, "Boxing Day Observed")
	}

	// January 6th to February 2nd
	// https://en.wikipedia.org/wiki/Epiphany_season
	// https://en.wikipedia.org/wiki/Twelfth_Night_(holiday)
	// https://en.wikipedia.org/wiki/Epiphany_(holiday)
	// https://fr.wikipedia.org/wiki/%C3%89piphanie
	// https://es.wikipedia.org/wiki/Epifan%C3%ADa
	// https://en.wikipedia.org/wiki/Candlemas
	// https://fr.wikipedia.org/wiki/Chandeleur
	// https://en.wikipedia.org/wiki/Christmas_tree
	// https://fr.wikipedia.org/wiki/Sapin_de_No%C3%ABl
	// Epiphanytide
	// Épiphanie, Epifanía
	t = find_date(fmt.Sprintf("%d-01-05", year))
	print_date(t, "Epiphany Eve")
	t = find_date(fmt.Sprintf("%d-01-06", year))
	print_date(t, "Epiphany")
	t = find_date(fmt.Sprintf("%d-02-02", year))
	print_date(t, "Candlemas")

	// December 26th to January 1st
	// https://en.wikipedia.org/wiki/Kwanzaa
	// https://fr.wikipedia.org/wiki/Kwanzaa
	// Début de Kwanzaa, Fin de Kwanzaa
	t = find_date(fmt.Sprintf("%d-12-26", year))
	print_date(t, "Kwanzaa Begins")
	t = find_date(fmt.Sprintf("%d-01-01", year))
	print_date(t, "Kwanzaa Ends")
}
