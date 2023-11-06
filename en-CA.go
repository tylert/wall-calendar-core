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

	// 3rd Monday in February
	// https://en.wikipedia.org/wiki/Family_Day
	// https://en.wikipedia.org/wiki/Family_Day_%28Canada%29
	// https://fr.wikipedia.org/wiki/Jour_de_Louis_Riel
	// Fête de la famille, Journée Louis Riel (CA-MB), Fête des Insulaires (CA-PE), Journée du patrimoine (CA-NS)
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Family Day (CA-AB, CA-BC, CA-NB, CA-ON, CA-SK)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Louis Riel Day (CA-MB)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Heritage Day (CA-NS)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "Islander Day (CA-PE)", uint32(time.Monday))

	// 2nd Sunday in March and 1st Sunday in November
	// last Sunday in March and last Sunday in October
	// https://en.wikipedia.org/wiki/Daylight_saving_time_in_Canada
	// https://en.wikipedia.org/wiki/Daylight_saving_time_by_country
	// UTC-12:00 -> Yankee https://www.timeanddate.com/time/zones/y
	// UTC-05:00 -> Romeo  https://www.timeanddate.com/time/zones/r
	// UTC-04:00 -> Quebec https://www.timeanddate.com/time/zones/q
	// UTC+00:00 -> Zulu   https://www.timeanddate.com/time/zones/z
	// UTC+01:00 -> Alpha  https://www.timeanddate.com/time/zones/a
	// UTC+02:00 -> Bravo  https://www.timeanddate.com/time/zones/b
	// UTC+12:00 -> Mike   https://www.timeanddate.com/time/zones/m
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
	// Fête du patrimoine (CA-AB, CA-YT), Jour de la Colombie-Britannique (CA-BC)
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
