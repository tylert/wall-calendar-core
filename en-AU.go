package main

import (
	"fmt"
	"time"
)

func englishAustralia(year uint32) {
	var t time.Time

	// https://en.wikipedia.org/wiki/Public_holidays_in_Australia

	// April 25th
	// https://en.wikipedia.org/wiki/Anzac_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_de_l%27ANZAC
	// Jour de l'Anzac (AU, NZ)
	t = find_date(fmt.Sprintf("%d-04-25", year))
	print_date(t, "Anzac Day (AU, NZ)")
}
