package main

import (
	"fmt"
	"time"
)

func englishUnitedStates(u32 uint32) {
	var t time.Time

	// 3rd Monday in January
	// https://en.wikipedia.org/wiki/Martin_Luther_King_Jr._Day
	// https://fr.wikipedia.org/wiki/Martin_Luther_King_Day
	// Journée de Martin Luther King Jr. (US)
	t = find_nearby_date(fmt.Sprintf("%d-01-18", u32), uint32(time.Monday))
	print_date(t, "Martin Luther King Jr. Day (US)")

	// 3rd Monday in February
	// https://en.wikipedia.org/wiki/Washington's_Birthday
	// https://en.wikipedia.org/wiki/Presidents%27_Day
	// https://fr.wikipedia.org/wiki/Presidents_Day
	// Journée de la Présidence (US)
	t = find_nearby_date(fmt.Sprintf("%d-02-18", u32), uint32(time.Monday))
	print_date(t, "President's Day (US)")

	// June 14th
	// https://en.wikipedia.org/wiki/Flag_Day_(United_States)
	// https://fr.wikipedia.org/wiki/Jour_du_drapeau_(%C3%89tats-Unis)
	// Jour du drapeau (US)
	t = find_date(fmt.Sprintf("%d-06-14", u32))
	print_date(t, "Flag Day (US)")

	// July 4th
	// https://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
	// https://fr.wikipedia.org/wiki/Jour_de_l%27Ind%C3%A9pendance_(%C3%89tats-Unis)
	// Jour de l'indépendance (US)
	t = find_date(fmt.Sprintf("%d-07-04", u32))
	print_date(t, "Independence Day (US)")

	// 2nd Monday in October
	// https://en.wikipedia.org/wiki/Columbus_Day
	// https://fr.wikipedia.org/wiki/Jour_de_Christophe_Colomb
	// https://theoatmeal.com/comics/columbus_day
	t = find_nearby_date(fmt.Sprintf("%d-10-11", u32), uint32(time.Monday))
	print_date(t, "Columbus Day (US)")
	print_date(t, "Bartolomé Day (US)")

	// 4th Thursday in November and the following Friday and Monday
	// https://en.wikipedia.org/wiki/Thanksgiving
	// https://fr.wikipedia.org/wiki/Thanksgiving
	// https://en.wikipedia.org/wiki/Black_Friday_(shopping)
	// https://fr.wikipedia.org/wiki/Black_Friday_(commerce)
	// https://en.wikipedia.org/wiki/Cyber_Monday
	// https://fr.wikipedia.org/wiki/Cyber_Monday
	// Action de Grâce (US)
	// Vendredi Noir, Cyber Lundi (US)
	t = find_nearby_date(fmt.Sprintf("%d-11-25", u32), uint32(time.Thursday))
	print_date(t, "Thanksgiving Day (US)")
	t = t.AddDate(0, 0, 1)
	print_date(t, "Black Friday (US)")
	t = t.AddDate(0, 0, 3)
	print_date(t, "Cyber Monday (US)")

	// December 7th
	// https://en.wikipedia.org/wiki/National_Pearl_Harbor_Remembrance_Day
	t = find_date(fmt.Sprintf("%d-12-07", u32))
	print_date(t, "Pearl Harbor Day (US)")
}
