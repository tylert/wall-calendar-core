package main

import (
	"container/list"
	"fmt"
	"time"
)

func englishGreatBritain(year uint32, events *list.List) {
	var t time.Time

	// GB      United Kingdom of Great Britain and Northern Ireland/Royaume-Uni de Grande-Bretagne et d'Irlande du Nord
	// GB-CHA  Channel Islands/Les îles Anglo-Normandes
	// GB-CYM  Wales/Galles
	// GB-EAW  England and Wales/Angleterre et Galles
	// GB-ENG  England/Angleterre
	// GB-GBN  United Kingdom of Great Britain and Northern Ireland/Royaume-Uni de Grande-Bretagne et d'Irlande du Nord
	// GB-GSY  Guernsey/L'Guernesey
	// GB-IOM  Isle of Man/L'île de Man
	// GB-JSY  Jersey
	// GB-NIR  Northern Ireland/Irlande du Nord
	// GB-SCT  Scotland/Écosse
	// GB-UKM  United Kingdom of Great Britain and Northern Ireland/Royaume-Uni de Grande-Bretagne et d'Irlande du Nord
	// GB-WLS  Wales/Galles
	// https://en.wikipedia.org/wiki/ISO_3166-2:GB
	// https://fr.wikipedia.org/wiki/ISO_3166-2:GB
	// https://en.wikipedia.org/wiki/Public_holidays_in_the_United_Kingdom
	// https://fr.wikipedia.org/wiki/F%C3%AAtes_et_jours_f%C3%A9ri%C3%A9s_au_Royaume-Uni

	// exactly 3 weeks before Easter Sunday (4th Sunday of Lent)
	// https://en.wikipedia.org/wiki/Mothering_Sunday
	monthG, dayG := Gregorian(int(year))
	easter := find_date(fmt.Sprintf("%04d-%02d-%02d", year, monthG, dayG))
	t = easter.AddDate(0, 0, -21)
	events.PushBack(Event{t, "Mothering Sunday (GB)", 1})

	// 1st Monday in May, last Monday in May, 1st Monday in June
	// 1st Monday in August, last Monday in August, last Monday in October
	// https://en.wikipedia.org/wiki/Bank_holiday
	// https://en.wikipedia.org/wiki/May_Day
	// https://uk-public-holidays.com/early-may-bank-holiday
	// https://uk-public-holidays.com/spring-bank-holiday
	// https://uk-public-holidays.com/summer-bank-holiday
	t = find_nearby_date(fmt.Sprintf("%04d-%02d-%02d", year, time.May, Month1st), uint32(time.Monday))
	events.PushBack(Event{t, "Early May Bank Holiday (GB)", 1})
	t = find_nearby_date(fmt.Sprintf("%04d-%02d-31", year, time.May), uint32(time.Monday))
	events.PushBack(Event{t, "Spring Bank Holiday (GB)", 1})
	t = find_nearby_date(fmt.Sprintf("%04d-%02d-%02d", year, time.August, Month1st), uint32(time.Monday))
	events.PushBack(Event{t, "Summer Bank Holiday (GB-SCT)", 1})
	t = find_nearby_date(fmt.Sprintf("%04d-%02d-31", year, time.August), uint32(time.Monday))
	events.PushBack(Event{t, "August Bank Holiday (GB-ENG, GB-WLS)", 1})

	// November 5th (November 5th, 1605)
	// https://en.wikipedia.org/wiki/Guy_Fawkes_Night
	// https://fr.wikipedia.org/wiki/Guy_Fawkes_Night
	// Journée de Guy Fawkes (GB)
	t = find_date(fmt.Sprintf("%04d-%02d-05", year, time.November))
	events.PushBack(Event{t, "Guy Fawkes Day (GB)", 1})

	// December 31st
	// https://en.wikipedia.org/wiki/Hogmanay
	// https://fr.wikipedia.org/wiki/Hogmanay
	t = find_date(fmt.Sprintf("%04d-%02d-31", year, time.December))
	events.PushBack(Event{t, "Hogmanay (GB)", 1})
}
