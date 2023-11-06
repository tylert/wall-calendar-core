package main

import (
	"fmt"
	"time"
)

func englishUnitedStates(u32 uint32) {
	// 3rd Monday in January
	// https://en.wikipedia.org/wiki/Martin_Luther_King_Jr._Day
	// https://fr.wikipedia.org/wiki/Martin_Luther_King_Day
	// Journée de Martin Luther King Jr. (US)
	print_wiggly_event(fmt.Sprintf("%d-01-18", u32), "Martin Luther King Jr. Day (US)", uint32(time.Monday))

	// 3rd Monday in February
	// https://en.wikipedia.org/wiki/Washington's_Birthday
	// https://en.wikipedia.org/wiki/Presidents%27_Day
	// https://fr.wikipedia.org/wiki/Presidents_Day
	// Journée de la Présidence (US)
	print_wiggly_event(fmt.Sprintf("%d-02-18", u32), "President's Day (US)", uint32(time.Monday))

	// July 4th
	// https://en.wikipedia.org/wiki/Independence_Day_%28United_States%29
	// Jour de l'indépendance (US)
	print_event(fmt.Sprintf("%d-07-04", u32), "Independence Day (US)")

	// 2nd Monday in October
	// https://en.wikipedia.org/wiki/Columbus_Day
	// https://fr.wikipedia.org/wiki/Jour_de_Christophe_Colomb
	// https://theoatmeal.com/comics/columbus_day
	print_wiggly_event(fmt.Sprintf("%d-10-11", u32), "Columbus Day (US)", uint32(time.Monday))
	print_wiggly_event(fmt.Sprintf("%d-10-11", u32), "Bartolomé Day (US)", uint32(time.Monday))

	// December 7th
	// https://en.wikipedia.org/wiki/National_Pearl_Harbor_Remembrance_Day
	print_event(fmt.Sprintf("%d-12-07", u32), "Pearl Harbor Day (US)")
}
