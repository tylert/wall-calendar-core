package main

import (
	"fmt"
	"time"
)

func englishUnitedKingdom(year uint32) {
	var t time.Time

	// https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Royaume-Uni

	// 1st Monday in May
	// last Monday in May
	// 1st Monday in June
	// 1st Monday in August
	// last Monday in August
	// last Monday in October
	// https://en.wikipedia.org/wiki/Bank_holiday
	// https://en.wikipedia.org/wiki/May_Day
	// https://uk-public-holidays.com/early-may-bank-holiday/
	// https://uk-public-holidays.com/spring-bank-holiday/
	// https://uk-public-holidays.com/summer-bank-holiday/
	t = find_nearby_date(fmt.Sprintf("%d-05-04", year), uint32(time.Monday))
	print_date(t, "Early May Bank Holiday (UK)")
	t = find_nearby_date(fmt.Sprintf("%d-05-31", year), uint32(time.Monday))
	print_date(t, "Spring Bank Holiday (UK)")
	t = find_nearby_date(fmt.Sprintf("%d-08-04", year), uint32(time.Monday))
	print_date(t, "Summer Bank Holiday (GB-SCT)")
	t = find_nearby_date(fmt.Sprintf("%d-08-31", year), uint32(time.Monday))
	print_date(t, "August Bank Holiday (GB-ENG, GB-WLS)")

	// November 5th (November 5th, 1605)
	// https://en.wikipedia.org/wiki/Guy_Fawkes_Night
	// https://fr.wikipedia.org/wiki/Guy_Fawkes_Night
	// Journée de Guy Fawkes (UK)
	t = find_date(fmt.Sprintf("%d-11-05", year))
	print_date(t, "Guy Fawkes Day (UK)")

	// December 31st
	// https://en.wikipedia.org/wiki/Hogmanay
	// https://fr.wikipedia.org/wiki/Hogmanay
	t = find_date(fmt.Sprintf("%d-12-31", year))
	print_date(t, "Hogmanay (UK)")
}
