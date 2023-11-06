package main

import (
	"fmt"
	"time"
)

func englishCanada(u32 uint32) {
	// https://en.wikipedia.org/wiki/Public_holidays_in_Canada
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada

	// December 31st and January 1st
	// https://en.wikipedia.org/wiki/New_Year's_Eve
	// https://fr.wikipedia.org/wiki/R%C3%A9veillon_de_la_Saint-Sylvestre
	// https://en.wikipedia.org/wiki/New_Year's_Day
	// https://fr.wikipedia.org/wiki/Jour_de_l%27an
	// Veille du Nouvel An, Jour de l'an, Jour de l'an observé
	print_event(fmt.Sprintf("%d-12-31", u32), "New Year's Eve")
	print_event(fmt.Sprintf("%d-01-01", u32), "New Year's Day")
	// XXX FIXME TODO  Add "observed" date too!!!

	// February 2nd
	// https://en.wikipedia.org/wiki/Groundhog_Day
	// https://fr.wikipedia.org/wiki/Jour_de_la_marmotte
	// Jour de la marmotte
	print_event(fmt.Sprintf("%d-02-02", u32), "Groundhog Day")

	// https://en.wikipedia.org/wiki/National_Flag_of_Canada_Day
	// https://fr.wikipedia.org/wiki/Jour_du_drapeau_national_du_Canada
	// Jour du drapeau national du Canada
	print_event(fmt.Sprintf("%d-02-15", u32), "Flag Day (CA)")

	// 3rd Monday in February
	// https://en.wikipedia.org/wiki/Family_Day
	// https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
	// https://fr.wikipedia.org/wiki/Jour_de_Louis_Riel
	// Fête de la famille, Journée Louis Riel (CA-MB), Fête des Insulaires (CA-PE), Journée du patrimoine (CA-NS)
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Family Day (CA-AB, CA-BC, CA-NB, CA-ON, CA-SK)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Louis Riel Day (CA-MB)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Heritage Day (CA-NS)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Islander Day (CA-PE)", uint32(time.Monday))

	// the Friday before the last Sunday in February
	// https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
	// Fête du patrimoine (CA-YT)
	tmp1, err := time.Parse(time.DateOnly, fmt.Sprintf("%d-02-29", u32))
	if err != nil {
		panic(err)
	}
	tmp2 := Closest(tmp1, uint32(time.Sunday))
	tmp3 := tmp2.AddDate(0, 0, -2)
	fmt.Println(fmt.Sprintf("%d-%02d-%02d  Heritage Day (CA-YT)", tmp3.Year(), tmp3.Month(), tmp3.Day()))

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
	print_wiggly_event(fmt.Sprintf("%d-03-11", u32), "02:00 DST Begins (CA, US)", uint32(time.Sunday))
	print_wiggly_event(fmt.Sprintf("%d-11-04", u32), "02:00 DST Ends (CA, US)", uint32(time.Sunday))
	print_wiggly_event(fmt.Sprintf("%d-03-31", u32), "01:00Z DST Begins (EU, UK)", uint32(time.Sunday))
	print_wiggly_event(fmt.Sprintf("%d-10-31", u32), "01:00Z DST Ends (EU, UK)", uint32(time.Sunday))

	// the Monday before May 25th
	// https://en.wikipedia.org/wiki/Victoria_Day
	// https://en.wikipedia.org/wiki/National_Patriots%27_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Reine_(Canada)
	// Fête de la Reine, Fête de Victoria, Journée nationale des patriotes (CA-QC)
	print_wiggly_event(fmt.Sprintf("%d-05-21", u32), "Victoria Day (CA)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-05-21", u32), "National Patriot's Day (CA-QC)", uint32(time.Monday))

	// June 19th
	// https://en.wikipedia.org/wiki/Upper_Canada
	// https://fr.wikipedia.org/wiki/Haut-Canada
	// https://en.wikipedia.org/wiki/Constitutional_history_of_Canada
	// https://fr.wikipedia.org/wiki/Histoire_constitutionnelle_du_Canada
	// https://www.ontario.ca/laws/statute/97u42
	// https://www.ontario.ca/fr/lois/loi/97u42
	print_event(fmt.Sprintf("%d-06-19", u32), "Loyalist Day (CA-ON)")

	// July 9th
	// https://en.wikipedia.org/wiki/Nunavut_Day
	// Fête du Nunavut (CA-NU)
	print_event(fmt.Sprintf("%d-07-09", u32), "Nunavut Day ᓄᓇᕗᑦ ᐅᓪᓗᖓ  (CA-NU)")

	// 1st Monday in August
	// https://en.wikipedia.org/wiki/Civic_Holiday
	// https://en.wikipedia.org/wiki/Public_holidays_in_Canada
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Canada
	// Simcoe Day (CA-ON)
	// Jour férié, Premier lundi d'août, Congé civique
	// Fête du patrimoine (CA-AB), Jour de la Colombie-Britannique (CA-BC)
	// Jour de Nouveau Brunswick (CA-NB), Jour de la Fondation (CA-NS)
	// Jour de Saskatchewan (CA-SK)
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "Civic Holiday (CA-NL, CA-NT, CA-NU, CA-ON)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "Heritage Day (CA-AB)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "British Columbia Day (CA-BC)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "Terry Fox Day (CA-MB)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "New Brunswick Day (CA-NB)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "Natal Day (CA-NS)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-08-04", u32), "Saskatchewan Day (CA-SK)", uint32(time.Monday))

	// 1st Monday in September
	// https://en.wikipedia.org/wiki/Labour_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_du_Travail
	// Fête du Travail
	print_wiggly_event(fmt.Sprintf("%d-09-04", u32), "Labour Day", uint32(time.Monday))

	// October 31st
	// https://en.wikipedia.org/wiki/Halloween
	// https://fr.wikipedia.org/wiki/Halloween
	print_event(fmt.Sprintf("%d-10-31", u32), "Hallowe'en")
}
