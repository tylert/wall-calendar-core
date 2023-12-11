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

	// February 1st, May 1st, August 1st, November 1st
	// https://en.wikipedia.org/wiki/Wheel_of_the_Year
	// https://fr.wikipedia.org/wiki/Roue_de_l%27ann%C3%A9e
	// https://en.wikipedia.org/wiki/Imbolc
	// https://fr.wikipedia.org/wiki/Imbolc
	// https://en.wikipedia.org/wiki/%C4%92ostre
	// https://fr.wikipedia.org/wiki/%C3%89ostre
	// https://en.wikipedia.org/wiki/Beltane
	// https://fr.wikipedia.org/wiki/Beltaine
	// https://en.wikipedia.org/wiki/Lughnasadh
	// https://fr.wikipedia.org/wiki/Lugnasad
	// https://en.wikipedia.org/wiki/Samhain
	// https://fr.wikipedia.org/wiki/Samain_(mythologie)
	// https://en.wikipedia.org/wiki/Yule
	// https://fr.wikipedia.org/wiki/Yule
	t = find_date(fmt.Sprintf("%d-02-01", year))
	print_date(t, "Imbolc")
	t = find_date(fmt.Sprintf("%d-03-21", year))
	print_date(t, "Ostara")
	t = find_date(fmt.Sprintf("%d-05-01", year))
	print_date(t, "Beltane")
	t = find_date(fmt.Sprintf("%d-06-21", year))
	print_date(t, "Litha")
	t = find_date(fmt.Sprintf("%d-08-01", year))
	print_date(t, "Lughnasadh")
	t = find_date(fmt.Sprintf("%d-09-21", year))
	print_date(t, "Mabon")
	t = find_date(fmt.Sprintf("%d-11-01", year))
	print_date(t, "Samhain")
	t = find_date(fmt.Sprintf("%d-12-21", year))
	print_date(t, "Yule")

	// December 17th to 23rd
	// https://en.wikipedia.org/wiki/Saturnalia
	// https://fr.wikipedia.org/wiki/Saturnales
	t = find_date(fmt.Sprintf("%d-12-17", year))
	print_date(t, "Saturnalia Begins")

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

	// February 13th
	// https://en.wikipedia.org/wiki/World_Radio_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_mondiale_de_la_radio
	// Journée mondiale de la radio
	t = find_date(fmt.Sprintf("%d-02-13", year))
	print_date(t, "World Radio Day")

	// April 18th
	// https://www.iaru.org/on-the-air/world-amateur-radio-day
	// https://www.rac.ca/operating/world-amateur-radio-day-april-18
	// https://www.arrl.org/world-amateur-radio-day
	// Journée de la radio amateur
	t = find_date(fmt.Sprintf("%d-04-18", year))
	print_date(t, "World Amateur Radio Day")

	// November 27, 1923
	// https://en.wikipedia.org/wiki/History_of_amateur_radio
	t = find_date(fmt.Sprintf("%d-11-27", year))
	print_date(t, fmt.Sprintf("%s Anniversary of first transatlantic two-way ham contact", ordinal(int(year-1923), "en")))

	// February 12th (February 12th, 1809)
	// https://en.wikipedia.org/wiki/Darwin_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_Darwin
	// Journée de Darwin
	t = find_date(fmt.Sprintf("%d-02-12", year))
	print_date(t, "Darwin Day")

	// July 10th
	// https://en.wikipedia.org/wiki/Nikola_Tesla
	// https://fr.wikipedia.org/wiki/Nikola_Tesla
	// https://nikolatesladay.com/
	t = find_date(fmt.Sprintf("%d-07-10", year))
	print_date(t, "Nikola Tesla Day")

	// October 4th, 1957
	// https://en.wikipedia.org/wiki/Sputnik_1
	// https://fr.wikipedia.org/wiki/Spoutnik_1
	// Anniversaire du lancement de Spoutnik 1
	t = find_date(fmt.Sprintf("%d-10-04", year))
	print_date(t, fmt.Sprintf("%s Anniversary of launch of Sputnik 1", ordinal(int(year-1957), "en")))

	// July 20th, 1969
	// December 11th, 1972
	// https://en.wikipedia.org/wiki/Apollo_11
	// https://fr.wikipedia.org/wiki/Apollo_11
	// https://en.wikipedia.org/wiki/Apollo_17
	// https://fr.wikipedia.org/wiki/Apollo_17
	t = find_date(fmt.Sprintf("%d-07-20", year))
	print_date(t, fmt.Sprintf("%s Anniversary of first lunar landing", ordinal(int(year-1969), "en")))
	t = find_date(fmt.Sprintf("%d-12-11", year))
	print_date(t, fmt.Sprintf("%s Anniversary of last lunar landing", ordinal(int(year-1972), "en")))

	// August 7th, 2027
	// October 26th, 2028
	// https://en.wikipedia.org/wiki/(137108)_1999_AN10
	// https://fr.wikipedia.org/wiki/(137108)_1999_AN10
	// https://en.wikipedia.org/wiki/(35396)_1997_XF11
	// https://fr.wikipedia.org/wiki/(35396)_1997_XF11
	if 2027 == year {
		t = find_date("2027-08-07")
		print_date(t, "06:48 1999 AN10 Asteroid Pass")
	}
	if 2028 == year {
		t = find_date("2028-10-26")
		print_date(t, "06:44 1997 XF11 Asteroid Pass")
	}

	// February 7th, 2036
	// January 19th, 2038
	// https://en.wikipedia.org/wiki/Year_2038_problem
	// https://fr.wikipedia.org/wiki/Bug_de_l%27an_2038
	// https://en.wikipedia.org/wiki/Network_Time_Protocol
	// https://fr.wikipedia.org/wiki/Network_Time_Protocol
	// NTP 00:00:00 UTC January 1st, 1900 to 06:28:16 UTC February 7th, 2036
	// POSIX 00:00:00 UTC January 1st, 1970 to 03:14:07 UTC January 19th, 2038
	// POSIX unsigned 32-bit overflow 06:28:15 UTC February 7th, 2106
	if 2036 == year {
		t = find_date("2036-02-07")
		print_date(t, "06:28:16 UTC NTP 32-bit Overflow")
	}
	if 2038 == year {
		t = find_date("2038-01-19")
		print_date(t, "03:14:07 UTC POSIX 32-bit Overflow")
	}
}
