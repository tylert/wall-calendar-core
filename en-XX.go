package main

import (
	"fmt"
	"time"
)

func englishOther(year uint32) {
	var t time.Time

	// 2nd Sunday in May
	// exactly 3 weeks before Easter Sunday (4th Sunday of Lent)
	// https://en.wikipedia.org/wiki/Mother's_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_des_M%C3%A8res
	// https://en.wikipedia.org/wiki/Mothering_Sunday
	// Fête des mères
	t = find_nearby_date(fmt.Sprintf("%d-05-11", year), uint32(time.Sunday))
	print_date(t, "Mother's Day")
	month, day := Gregorian(int(year))
	easter := find_date(fmt.Sprintf("%d-%02d-%02d", year, month, day))
	t = easter.AddDate(0, 0, -21)
	print_date(t, "Mothering Sunday (UK)")

	// 3rd Sunday in June
	// https://en.wikipedia.org/wiki/Father's_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_des_P%C3%A8res
	// Fête des pères
	t = find_nearby_date(fmt.Sprintf("%d-06-18", year), uint32(time.Sunday))
	print_date(t, "Father's Day")

	// February 29, 2012
	// https://en.wikipedia.org/wiki/Raspberry_Pi
	// https://fr.wikipedia.org/wiki/Raspberry_Pi
	if is_leap(year) {
		t = find_date(fmt.Sprintf("%d-02-29", year))
	} else {
		t = find_date(fmt.Sprintf("%d-02-28", year))
	}
	print_date(t, fmt.Sprintf("%s Birthday of Raspberry Pi", ordinal(int(year-2012), "en")))

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
	} else {
		t = find_date(fmt.Sprintf("%d-11-10", year))
	}
	print_date(t, "Pi Approximation Day 314th day")

	// September 12th or 13th (256th day of the year)
	// https://en.wikipedia.org/wiki/Day_of_the_Programmer
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_des_programmeurs
	// Jour du programmeur 256e jour
	if is_leap(year) {
		t = find_date(fmt.Sprintf("%d-09-12", year))
	} else {
		t = find_date(fmt.Sprintf("%d-09-13", year))
	}
	print_date(t, "Day of the Programmer 256th day")

	// 3rd Saturday in September
	// https://en.wikipedia.org/wiki/Software_Freedom_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_du_logiciel_libre
	// Journée de la liberté des logiciels
	t = find_nearby_date(fmt.Sprintf("%d-09-18", year), uint32(time.Saturday))
	print_date(t, "Software Freedom Day")

	// September 19th
	// https://en.wikipedia.org/wiki/International_Talk_Like_a_Pirate_Day
	// https://fr.wikipedia.org/wiki/International_Talk_Like_a_Pirate_Day
	t = find_date(fmt.Sprintf("%d-09-19", year))
	print_date(t, "International Talk Like a Pirate Day")

	// June 28th, October 22nd
	// https://en.wikipedia.org/wiki/Caps_lock#International_Caps_Lock_Day
	// https://fr.wikipedia.org/wiki/Touche_de_verrouillage_des_majuscules
	// JOURNÉE INTERNATIONALE DU VERROUILLAGE DES MAJUSCULES
	t = find_date(fmt.Sprintf("%d-06-28", year))
	print_date(t, "INTERNATIONAL CAPS LOCK DAY")
	t = find_date(fmt.Sprintf("%d-10-22", year))
	print_date(t, "INTERNATIONAL CAPS LOCK DAY")

	// Caturday
	// https://en.wikipedia.org/wiki/International_Cat_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_du_chat
	// https://en.wikipedia.org/wiki/National_Cat_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_nationale_du_chat
	t = find_date(fmt.Sprintf("%d-02-17", year))
	print_date(t, "National Cat Day (BR, IT)")
	t = find_date(fmt.Sprintf("%d-02-22", year))
	print_date(t, "National Cat Day (JP)")
	t = find_date(fmt.Sprintf("%d-03-01", year))
	print_date(t, "National Cat Day (RU)")
	t = find_date(fmt.Sprintf("%d-08-08", year))
	print_date(t, "International Cat Day")
	print_date(t, "National Cat Day (CA)")
	t = find_date(fmt.Sprintf("%d-10-29", year))
	print_date(t, "National Cat Day (US)")
}
