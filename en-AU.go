package main

import (
	"fmt"
	"time"
)

func englishAustralia(u32 uint32) {
	var t time.Time

	// https://en.wikipedia.org/wiki/Public_holidays_in_Australia

	// https://en.wikipedia.org/wiki/Anzac_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_de_l%27ANZAC
	// Jour de l'Anzac (AU, NZ)
	t = find_date(fmt.Sprintf("%d-04-25", u32))
	print_date(t, "Anzac Day (AU, NZ)")
}
