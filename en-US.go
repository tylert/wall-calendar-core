package main

import (
	"fmt"
	"time"
)

func englishUnitedStates(year uint32) {
	var t time.Time

	// 3rd Monday in January
	// https://en.wikipedia.org/wiki/Martin_Luther_King_Jr._Day
	// https://fr.wikipedia.org/wiki/Martin_Luther_King_Day
	// Journée de Martin Luther King Jr. (US)
	t = find_nearby_date(fmt.Sprintf("%d-01-18", year), uint32(time.Monday))
	print_date(t, "Martin Luther King Jr. Day (US)")

	// January 20th or the 21st if the 20th is a Sunday
	// every 4th year where "year%4 == 1" (2001, ..., 2013, 2017, 2021, 2025, 2029, etc.)
	// https://en.wikipedia.org/wiki/United_States_presidential_inauguration
	// Jour d'inauguration (US)
	if 1 == year%4 {
		t = find_date(fmt.Sprintf("%d-01-20", year))
		if t.Weekday() == time.Sunday {
			t = t.AddDate(0, 0, 1)
			print_date(t, "Inauguration Day (US)")
		} else {
			print_date(t, "Inauguration Day (US)")
		}
	}

	// 3rd Monday in February
	// https://en.wikipedia.org/wiki/Washington's_Birthday
	// https://en.wikipedia.org/wiki/Presidents%27_Day
	// https://fr.wikipedia.org/wiki/Presidents_Day
	// Journée de la Présidence (US)
	t = find_nearby_date(fmt.Sprintf("%d-02-18", year), uint32(time.Monday))
	print_date(t, "President's Day (US)")

	// May 5th
	// https://en.wikipedia.org/wiki/Cinco_de_Mayo
	// https://fr.wikipedia.org/wiki/Cinco_de_Mayo
	// Fête du 5 mai (US)
	t = find_date(fmt.Sprintf("%d-05-05", year))
	print_date(t, "Cinco de Mayo (US)")

	// 2nd Saturday in May
	// 3rd Saturday in May
	// last Monday in May
	// https://en.wikipedia.org/wiki/Armed_Forces_Day
	// https://fr.wikipedia.org/wiki/Jour_des_forces_arm%C3%A9es
	// https://en.wikipedia.org/wiki/Memorial_Day
	// https://fr.wikipedia.org/wiki/Memorial_Day
	// Journée des forces armées (US)
	t = find_nearby_date(fmt.Sprintf("%d-05-11", year), uint32(time.Saturday))
	print_date(t, "Armed Forces Week (US)")
	t = find_nearby_date(fmt.Sprintf("%d-05-18", year), uint32(time.Saturday))
	print_date(t, "Armed Forces Day (US)")
	t = find_nearby_date(fmt.Sprintf("%d-05-31", year), uint32(time.Monday))
	print_date(t, "Memorial Day (US)")

	// June 14th
	// https://en.wikipedia.org/wiki/Flag_Day_(United_States)
	// https://fr.wikipedia.org/wiki/Jour_du_drapeau_(%C3%89tats-Unis)
	// Jour du drapeau (US)
	t = find_date(fmt.Sprintf("%d-06-14", year))
	print_date(t, "Flag Day (US)")

	// June 19th
	// https://en.wikipedia.org/wiki/Juneteenth
	// https://fr.wikipedia.org/wiki/Juneteenth
	t = find_date(fmt.Sprintf("%d-06-19", year))
	print_date(t, "Juneteenth (US)")

	// July 4th
	// https://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
	// https://fr.wikipedia.org/wiki/Jour_de_l%27Ind%C3%A9pendance_(%C3%89tats-Unis)
	// Jour de l'indépendance (US)
	t = find_date(fmt.Sprintf("%d-07-04", year))
	print_date(t, "Independence Day (US)")

	// 2nd Monday in October
	// https://en.wikipedia.org/wiki/Columbus_Day
	// https://fr.wikipedia.org/wiki/Jour_de_Christophe_Colomb
	// https://theoatmeal.com/comics/columbus_day
	t = find_nearby_date(fmt.Sprintf("%d-10-11", year), uint32(time.Monday))
	print_date(t, "Columbus Day (US)")
	print_date(t, "Bartolomé Day (US)")

	// 4th Thursday in November, Friday, Monday
	// https://en.wikipedia.org/wiki/Thanksgiving
	// https://fr.wikipedia.org/wiki/Thanksgiving
	// https://en.wikipedia.org/wiki/Black_Friday_(shopping)
	// https://fr.wikipedia.org/wiki/Black_Friday_(commerce)
	// https://en.wikipedia.org/wiki/Cyber_Monday
	// https://fr.wikipedia.org/wiki/Cyber_Monday
	// Action de Grâce (US)
	// Vendredi Noir, Cyber Lundi (US)
	t = find_nearby_date(fmt.Sprintf("%d-11-25", year), uint32(time.Thursday))
	print_date(t, "Thanksgiving Day (US)")
	t = t.AddDate(0, 0, 1)
	print_date(t, "Black Friday (US)")
	t = t.AddDate(0, 0, 3)
	print_date(t, "Cyber Monday (US)")

	// December 7th (December 7th, 1941)
	// https://en.wikipedia.org/wiki/National_Pearl_Harbor_Remembrance_Day
	t = find_date(fmt.Sprintf("%d-12-07", year))
	print_date(t, "Pearl Harbor Day (US)")

	// December 8th
	// https://en.wikipedia.org/wiki/Christmas_tree
	// https://fr.wikipedia.org/wiki/Sapin_de_No%C3%ABl
	// https://checkiday.com/2e2a58a06269bc06cefe283f22b8173e/national-christmas-tree-day
	t = find_date(fmt.Sprintf("%d-12-08", year))
	print_date(t, "Christmas Tree Day (US)")
}
