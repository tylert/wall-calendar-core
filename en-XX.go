package main

import (
	"fmt"
	"time"
)

func englishOther(year uint32) {
	var t time.Time

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
