package main

import (
	"fmt"
	"time"
)

func englishAustralia(year uint32) {
	var t time.Time

	// AU      Australia/Australie
	// AU-ACT  Australian Capital Territory
	// AU-NSW  New South Wales
	// AU-NT   Northern Territory
	// AU-QLD  Queensland
	// AU-SA   South Australia
	// AU-TAS  Tasmania
	// AU-VIC  Victoria
	// AU-WA   Western Australia
	// https://en.wikipedia.org/wiki/ISO_3166-2:AU
	// https://fr.wikipedia.org/wiki/ISO_3166-2:AU
	// https://en.wikipedia.org/wiki/Public_holidays_in_Australia

	// January 26th (January 26th, 1788)
	// https://en.wikipedia.org/wiki/Australia_Day
	// https://fr.wikipedia.org/wiki/Australia_Day
	t = find_date(fmt.Sprintf("%d-01-26", year))
	print_date(t, "Australia Day (AU)")

	// April 25th
	// https://en.wikipedia.org/wiki/Anzac_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_de_l%27ANZAC
	// Jour de l'Anzac (AU, NZ)
	t = find_date(fmt.Sprintf("%d-04-25", year))
	print_date(t, "Anzac Day (AU, NZ)")
}
