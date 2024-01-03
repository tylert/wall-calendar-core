package main

import (
	"fmt"
	"time"
)

func englishOther(year uint32) {
	var t time.Time

	// https://en.wikipedia.org/wiki/Liturgical_year
	// https://fr.wikipedia.org/wiki/Calendrier_liturgique

	// the Sunday following the full moon on or after the March equinox (March 21st)
	// https://en.wikipedia.org/wiki/Ecclesiastical_full_moon
	// https://en.wikipedia.org/wiki/Computus
	// https://en.wikipedia.org/wiki/Date_of_Easter
	// https://fr.wikipedia.org/wiki/Calcul_de_la_date_de_P%C3%A2ques
	// https://en.wikipedia.org/wiki/Easter_cycle
	// https://en.wikipedia.org/wiki/Shrovetide
	// https://fr.wikipedia.org/wiki/Septuag%C3%A9sime
	// https://en.wikipedia.org/wiki/Quinquagesima
	// https://fr.wikipedia.org/wiki/Dimanche_Gras
	// https://en.wikipedia.org/wiki/Sexagesima
	// https://en.wikipedia.org/wiki/Shrove_Tuesday
	// https://fr.wikipedia.org/wiki/Mardi_gras
	// https://en.wikipedia.org/wiki/Ash_Wednesday
	// https://fr.wikipedia.org/wiki/Mercredi_des_Cendres
	// https://en.wikipedia.org/wiki/Lent
	// https://fr.wikipedia.org/wiki/Car%C3%AAme
	// https://en.wikipedia.org/wiki/Quadragesima_Sunday
	// https://fr.wikipedia.org/wiki/Premier_dimanche_de_Car%C3%AAme
	// https://en.wikipedia.org/wiki/Laetare_Sunday
	// https://fr.wikipedia.org/wiki/Quatri%C3%A8me_dimanche_de_Car%C3%AAme
	// https://en.wikipedia.org/wiki/Palm_Sunday
	// https://fr.wikipedia.org/wiki/Dimanche_des_Rameaux
	// https://en.wikipedia.org/wiki/Holy_Wednesday
	// https://fr.wikipedia.org/wiki/Mercredi_saint
	// https://en.wikipedia.org/wiki/Maundy_Thursday
	// https://fr.wikipedia.org/wiki/Jeudi_saint
	// https://en.wikipedia.org/wiki/Good_Friday
	// https://fr.wikipedia.org/wiki/Vendredi_saint
	// https://es.wikipedia.org/wiki/Viernes_Santo
	// https://en.wikipedia.org/wiki/Holy_Saturday
	// https://fr.wikipedia.org/wiki/Samedi_saint
	// https://en.wikipedia.org/wiki/Easter
	// https://fr.wikipedia.org/wiki/P%C3%A2ques
	// https://es.wikipedia.org/wiki/Pascua
	// https://en.wikipedia.org/wiki/Easter_Saturday
	// https://en.wikipedia.org/wiki/Feast_of_the_Ascension
	// https://fr.wikipedia.org/wiki/Ascension_(f%C3%AAte)
	// https://en.wikipedia.org/wiki/Pentecost
	// https://fr.wikipedia.org/wiki/Pentec%C3%B4te
	// https://en.wikipedia.org/wiki/Trinity_Sunday
	// https://fr.wikipedia.org/wiki/F%C3%AAte_de_la_Sainte-Trinit%C3%A9
	// https://en.wikipedia.org/wiki/Feast_of_Corpus_Christi
	// https://fr.wikipedia.org/wiki/F%C3%AAte-Dieu
	// https://en.wikipedia.org/wiki/Carnival
	// https://fr.wikipedia.org/wiki/Carnaval
	// https://www.timeanddate.com/holidays/common/carnival-wednesday
	// https://www.timeanddate.com/holidays/common/whit-sunday
	// https://www.timeanddate.com/holidays/common/whit-monday
	// Pascua (ES) = Easter
	// Mardi Gras
	// Mercredi des Cendres
	// Lent / Carême
	// Dimanche des Rameaux
	// Mercredi saint
	// Jeudi saint
	// Vendredi saint, Viernes Santo (ES)
	// Samedi saint
	// Dimanche de Pâques
	// Lundi de Pâques
	// Ascension
	// Pentecôte
	monthG, dayG := Gregorian(int(year))
	easter := find_date(fmt.Sprintf("%d-%02d-%02d", year, monthG, dayG))
	t = easter.AddDate(0, 0, -63)
	print_date(t, "Septuagesima Sunday") // "70th", 3rd Sunday before Lent (9th before Easter)
	t = easter.AddDate(0, 0, -56)
	print_date(t, "Sexagesima Sunday") // "60th", 2nd Sunday before Lent (8th before Easter)
	t = easter.AddDate(0, 0, -49)
	print_date(t, "Quinquagesima/Shrove/Pork Sunday") // "50th", last Sunday before Lent (7th before Easter)
	t = easter.AddDate(0, 0, -47)
	print_date(t, "Shrove/Pancake Tuesday") // day before Lent
	t = easter.AddDate(0, 0, -46)
	print_date(t, "Carnival/Ash Wednesday") // Lent begins
	t = easter.AddDate(0, 0, -42)
	print_date(t, "Invocabit Sunday") // "40th", 1st Sunday after Lent (6th before Easter)
	t = easter.AddDate(0, 0, -21)
	print_date(t, "Laetare Sunday") // 4th before Easter
	t = easter.AddDate(0, 0, -7)
	print_date(t, "Palm Sunday")
	t = easter.AddDate(0, 0, -4)
	print_date(t, "Holy Wednesday")
	t = easter.AddDate(0, 0, -3)
	print_date(t, "Maundy Thursday")
	t = easter.AddDate(0, 0, -2)
	print_date(t, "Good Friday")
	t = easter.AddDate(0, 0, -1)
	print_date(t, "Holy Saturday")
	print_date(easter, "Easter Sunday")
	t = easter.AddDate(0, 0, 1)
	print_date(t, "Easter Monday")
	t = easter.AddDate(0, 0, 6)
	print_date(t, "Easter Saturday")
	t = easter.AddDate(0, 0, 39)
	print_date(t, "Ascension Day")
	t = easter.AddDate(0, 0, 49)
	print_date(t, "Whit/Pentecost Sunday")
	t = easter.AddDate(0, 0, 50)
	print_date(t, "Whit/Pentecost Monday")
	t = easter.AddDate(0, 0, 56)
	print_date(t, "Trinity Sunday")
	t = easter.AddDate(0, 0, 60)
	print_date(t, "Corpus Christi")
	// Passover begins on 14 or 15 Nisan and goes until 21 or 22 Nisan
	// https://en.wikipedia.org/wiki/Passover
	// https://fr.wikipedia.org/wiki/Pessa%27h
	// https://en.wikipedia.org/wiki/Pascha
	// https://en.wikipedia.org/wiki/Passover_(Christian_holiday)
	// https://en.wikipedia.org/wiki/Passover_Seder
	// https://fr.wikipedia.org/wiki/S%C3%A9der_de_Pessa%27h
	// https://en.wikipedia.org/wiki/Nisan
	// https://fr.wikipedia.org/wiki/Nissan_(mois)
	// Début de Pâque des Juifs, Fin de Pâque des Juifs
	// Passover = Pesach = Pascha = Jewish Easter
	// Pessa'h
	// XXX FIXME TODO  Palm Sunday Orthodox???
	monthJ, dayJ := Julian(int(year))
	pascha := find_date(fmt.Sprintf("%d-%02d-%02d", year, monthJ, dayJ))
	print_date(pascha, "Passover")
	//t = pascha.AddDate(0, 0, 8)
	//print_date(t, "Orthodox Easter Sunday")

	// 2nd Sunday in May
	// exactly 3 weeks before Easter Sunday (4th Sunday of Lent)
	// https://en.wikipedia.org/wiki/Mother's_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_des_M%C3%A8res
	// https://en.wikipedia.org/wiki/Mothering_Sunday
	// Fête des mères
	t = easter.AddDate(0, 0, -21)
	print_date(t, "Mothering Sunday (UK)")
	t = find_nearby_date(fmt.Sprintf("%d-05-11", year), uint32(time.Sunday))
	print_date(t, "Mother's Day")

	// 3rd Sunday in June
	// https://en.wikipedia.org/wiki/Father's_Day
	// https://fr.wikipedia.org/wiki/F%C3%AAte_des_P%C3%A8res
	// Fête des pères
	t = find_nearby_date(fmt.Sprintf("%d-06-18", year), uint32(time.Sunday))
	print_date(t, "Father's Day")

	// March 20st, April 20th, May 21st, June 21st
	// July 23rd, August 23rd, September 23rd, October 23rd
	// November 22nd, December 22nd, January 20th, February 18th
	// https://en.wikipedia.org/wiki/Aries_(astrology)
	// https://fr.wikipedia.org/wiki/B%C3%A9lier_(astrologie)
	// https://en.wikipedia.org/wiki/Taurus_(astrology)
	// https://fr.wikipedia.org/wiki/Taureau_(astrologie)
	// https://en.wikipedia.org/wiki/Gemini_(astrology)
	// https://fr.wikipedia.org/wiki/G%C3%A9meaux_(astrologie)
	// https://en.wikipedia.org/wiki/Cancer_(astrology)
	// https://fr.wikipedia.org/wiki/Cancer_(astrologie)
	// https://en.wikipedia.org/wiki/Leo_(astrology)
	// https://fr.wikipedia.org/wiki/Lion_(astrologie)
	// https://en.wikipedia.org/wiki/Virgo_(astrology)
	// https://fr.wikipedia.org/wiki/Vierge_(astrologie)
	// https://en.wikipedia.org/wiki/Libra_(astrology)
	// https://fr.wikipedia.org/wiki/Balance_(astrologie)
	// https://en.wikipedia.org/wiki/Scorpio_(astrology)
	// https://fr.wikipedia.org/wiki/Scorpion_(astrologie)
	// https://en.wikipedia.org/wiki/Sagittarius_(astrology)
	// https://fr.wikipedia.org/wiki/Sagittaire_(astrologie)
	// https://en.wikipedia.org/wiki/Capricorn_(astrology)
	// https://fr.wikipedia.org/wiki/Capricorne_(astrologie)
	// https://en.wikipedia.org/wiki/Aquarius_(astrology)
	// https://fr.wikipedia.org/wiki/Verseau_(astrologie)
	// https://en.wikipedia.org/wiki/Pisces_(astrology)
	// https://fr.wikipedia.org/wiki/Poissons_(astrologie)
	// Ascension du bélier, Descension du bélier
	// Ascension du taureau, Descension du taureau
	// Ascension des gémeaux, Descension des gémeaux
	// Ascension du cancer, Descension du cancer
	// Ascension du lion, Descension du lion
	// Ascension de la vierge, Descension de la vierge
	// Ascension de la balance, Descension de la balance
	// Ascension du scorpion, Descension du scorpion
	// Ascension du sagittaire, Descension du sagittaire
	// Ascension du capricorne, Descension du capricorne
	// Ascension du verseau, Descension du verseau
	// Ascension des poissons, Descension des poissons
	t = find_date(fmt.Sprintf("%d-03-20", year))
	print_date(t, "♈︎ Aries Rises")
	t = find_date(fmt.Sprintf("%d-04-20", year))
	print_date(t, "♉︎ Taurus Rises")
	t = find_date(fmt.Sprintf("%d-05-21", year))
	print_date(t, "♊︎ Gemini Rises")
	t = find_date(fmt.Sprintf("%d-06-21", year))
	print_date(t, "♋︎ Cancer Rises")
	t = find_date(fmt.Sprintf("%d-07-23", year))
	print_date(t, "♌︎ Leo Rises")
	t = find_date(fmt.Sprintf("%d-08-23", year))
	print_date(t, "♍︎ Virgo Rises")
	t = find_date(fmt.Sprintf("%d-09-23", year))
	print_date(t, "♎︎ Libra Rises")
	t = find_date(fmt.Sprintf("%d-10-23", year))
	print_date(t, "♏︎ Scorpio Rises")
	t = find_date(fmt.Sprintf("%d-11-22", year))
	print_date(t, "♐︎ Sagittarius Rises")
	t = find_date(fmt.Sprintf("%d-12-22", year))
	print_date(t, "♑︎ Capricorn Rises")
	t = find_date(fmt.Sprintf("%d-01-20", year))
	print_date(t, "♒︎ Aquarius Rises")
	t = find_date(fmt.Sprintf("%d-02-18", year))
	print_date(t, "♓︎ Pisces Rises")

	// February 1st, May 1st, August 1st, November 1st
	// March 21st, June 21st, September 21st, December 21st
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

	// December 23rd
	// https://en.wikipedia.org/wiki/Festivus
	t = find_date(fmt.Sprintf("%d-12-23", year))
	print_date(t, "Festivus")

	// Caturday
	// February 17th, February 22nd, March 1st, August 8th, October 29th
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

	// April 7, 2005
	// https://en.wikipedia.org/wiki/Git
	// https://fr.wikipedia.org/wiki/Git
	t = find_date(fmt.Sprintf("%d-04-07", year))
	print_date(t, fmt.Sprintf("%s Birthday of Git", ordinal(int(year-2005), "en")))

	// January 25th, 2011
	// https://en.wikipedia.org/wiki/LibreOffice
	// https://fr.wikipedia.org/wiki/LibreOffice
	t = find_date(fmt.Sprintf("%d-01-25", year))
	print_date(t, fmt.Sprintf("%s Birthday of LibreOffice", ordinal(int(year-2010), "en")))

	// September 19th
	// https://en.wikipedia.org/wiki/International_Talk_Like_a_Pirate_Day
	// https://fr.wikipedia.org/wiki/International_Talk_Like_a_Pirate_Day
	t = find_date(fmt.Sprintf("%d-09-19", year))
	print_date(t, "International Talk Like a Pirate Day")

	// August 13th
	// https://en.wikipedia.org/wiki/International_Lefthanders_Day
	// https://fr.wikipedia.org/wiki/Journ%C3%A9e_internationale_des_gauchers
	// Journée internationale des gauchers
	t = find_date(fmt.Sprintf("%d-08-13", year))
	print_date(t, "Left-Handers' Day")

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

	// 2nd Tuesday of October
	// https://en.wikipedia.org/wiki/Ada_Lovelace_Day
	// https://fr.wikipedia.org/wiki/Ada_Lovelace_Day
	// https://findingada.com/about/when-is-ald
	// Journée de Ada Lovelace
	t = find_nearby_date(fmt.Sprintf("%d-10-11", year), uint32(time.Tuesday))
	print_date(t, "Ada Lovelace Day")

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
