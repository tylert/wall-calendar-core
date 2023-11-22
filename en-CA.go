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

	// December 31st and January 1st
	// https://en.wikipedia.org/wiki/New_Year's_Eve
	// https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_la_Saint-Sylvestre
	// https://en.wikipedia.org/wiki/Hogmanay
	// https://fr.wikipedia.org/wiki/Hogmanay
	// https://en.wikipedia.org/wiki/New_Year's_Day
	// https://fr.wikipedia.org/wiki/Jour_de_l%27an
	// Veille du Nouvel An, Jour de l'an, Jour de l'an observé
	t = find_date(fmt.Sprintf("%d-12-31", year))
	print_date(t, "Hogmanay (UK)")
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

	// 2nd Sunday in March and 1st Sunday in November
	// last Sunday in March and last Sunday in October
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

	// 2nd Monday in March
	// https://en.wikipedia.org/wiki/Commonwealth_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_Commonwealth
	// Journée du Commonwealth
	t = find_nearby_date(fmt.Sprintf("%d-03-11", year), uint32(time.Monday))
	print_date(t, "Commonwealth Day")

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
	print_date(t, "Canada Day")
	print_date(t, "Memorial Day (CA-NL)")

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

	// begins on the 2nd last Sunday of July and lasts for 2 weeks
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

	// 1st Monday in September
	// https://en.wikipedia.org/wiki/Labour_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
	// Fête du Travail
	t = find_nearby_date(fmt.Sprintf("%d-09-04", year), uint32(time.Monday))
	print_date(t, "Labour Day")

	// September 30th
	// https://en.wikipedia.org/wiki/Orange_Shirt_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_de_la_v%C3%A9rit%C3%A9_et_de_la_r%C3%A9conciliation
	// https://www.orangeshirtday.org/
	// Journée nationale de la vérité et de la réconciliation (CA)
	// Orange Shirt Day (CA)
	// Journée du chandail orange (CA)
	t = find_date(fmt.Sprintf("%d-09-30", year))
	print_date(t, "National Day for Truth and Reconciliation (CA)")

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

	// October 31st, November 1st and 2nd
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

	// February 1st, May 1st, August 1st, November 1st
	// https://en.wikipedia.org/wiki/Imbolc
	// https://fr.wikipedia.org/wiki/Imbolc
	// https://en.wikipedia.org/wiki/Beltane
	// https://fr.wikipedia.org/wiki/Beltaine
	// https://en.wikipedia.org/wiki/Lughnasadh
	// https://fr.wikipedia.org/wiki/Lugnasad
	// https://en.wikipedia.org/wiki/Samhain
	// https://fr.wikipedia.org/wiki/Samain_(mythologie)
	t = find_date(fmt.Sprintf("%d-02-01", year))
	print_date(t, "Imbolc")
	t = find_date(fmt.Sprintf("%d-05-01", year))
	print_date(t, "Beltane")
	t = find_date(fmt.Sprintf("%d-08-01", year))
	print_date(t, "Lughnasadh")
	t = find_date(fmt.Sprintf("%d-11-01", year))
	print_date(t, "Samhain")

	// November 11th and September 3rd
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
	// The Statute of Westminster was enacted on December 11th, 1931
	// Anniversaire du Statut de Westminster
	t = find_date(fmt.Sprintf("%d-12-11", year))
	print_date(t, fmt.Sprintf("%s Anniversary of the Statute of Westminster", ordinal(int(year-1931), "en")))

	// December 24th, 25th and 26th
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

	// December 26th to January 1st
	// https://en.wikipedia.org/wiki/Kwanzaa
	// https://fr.wikipedia.org/wiki/Kwanzaa
	// Début de Kwanzaa, Fin de Kwanzaa
	t = find_date(fmt.Sprintf("%d-12-26", year))
	print_date(t, "Kwanzaa Begins")
	t = find_date(fmt.Sprintf("%d-01-01", year))
	print_date(t, "Kwanzaa Ends")

	// 1st Friday in March
	// https://en.wikipedia.org/wiki/Employee_Appreciation_Day
	t = find_nearby_date(fmt.Sprintf("%d-03-04", year), uint32(time.Friday))
	print_date(t, "Employee Appreciation Day (AU, CA, IN, SG, US, UK)")

	// March 14th, June 28th, July 22nd, Nov 9th or 10th (314th day of the year)
	// https://en.wikipedia.org/wiki/Pi_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_de_pi
	// https://piday.org
	// https://tauday.com
	// https://piapproximationday.com
	// Journée de pi 3.14
	// Journée de tau 6.28
	// Journée d'approximation pi 22/7
	// Journée d'approximation pi 314e jour
	t = find_date(fmt.Sprintf("%d-03-14", year))
	print_date(t, "Pi Day 3.14")
	t = find_date(fmt.Sprintf("%d-06-28", year))
	print_date(t, "Tau Day 6.28")
	t = find_date(fmt.Sprintf("%d-07-22", year))
	print_date(t, "Pi Approximation Day 22/7")
	if is_leap(year) {
		t = find_date(fmt.Sprintf("%d-11-09", year))
		print_date(t, "Pi Approximation Day 314th day")
	} else {
		t = find_date(fmt.Sprintf("%d-11-10", year))
		print_date(t, "Pi Approximation Day 314th day")
	}

	// September 12th or 13th (256th day of the year)
	// https://en.wikipedia.org/wiki/Day_of_the_Programmer
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_des_programmeurs
	// Jour du programmeur 256e jour
	if is_leap(year) {
		t = find_date(fmt.Sprintf("%d-09-12", year))
		print_date(t, "Day of the Programmer 256th day")
	} else {
		t = find_date(fmt.Sprintf("%d-09-13", year))
		print_date(t, "Day of the Programmer 256th day")
	}
}
