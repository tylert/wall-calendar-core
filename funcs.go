package main

import (
	"fmt"
	"time"
)

// Sun = 0, Mon = 1, Tue = 2, Wed = 3, Thu = 4, Fri = 5, Sat = 6
// 1st = 4, 2nd = 11, 3rd = 18, 4th = 25, 5th/last = 31

func closest(nearby time.Time, desired uint32) time.Time {
	// Find out how many days to shift over to find the desired weekday
	offset := -(int(nearby.Weekday()) - (int(desired) % 7))
	if offset < -3 {
		offset += 7
	}
	if offset > 3 {
		offset -= 7
	}
	found := nearby.AddDate(0, 0, offset)

	// Make sure the date found is still in the desired month
	if found.After(nearby) && (found.Month() != nearby.Month()) {
		return found.AddDate(0, 0, -7)
	} else if found.Before(nearby) && (found.Month() != nearby.Month()) {
		return found.AddDate(0, 0, 7)
	} else {
		return found
	}
}

func find_date(date string) time.Time {
	t, _ := time.Parse(time.DateOnly, date)
	return t
}

func find_nearby_date(date string, desired uint32) time.Time {
	t := closest(find_date(date), desired)
	return t
}

func print_date(whatzit time.Time, label string) {
	fmt.Println(fmt.Sprintf("%d-%02d-%02d  [%s]  %s", whatzit.Year(), whatzit.Month(), whatzit.Day(), whatzit.Weekday(), label))
}

func is_leap(year uint32) bool {
	return year%4 == 0 && (year%100 != 0 || year%400 == 0)
}

func ordinal(num int, lang string) string {
	switch lang {
	case "en":
		switch {
		case num > 10 && num < 20:
			return fmt.Sprintf("%dth", num)
		case num%10 == 1:
			return fmt.Sprintf("%dst", num)
		case num%10 == 2:
			return fmt.Sprintf("%dnd", num)
		case num%10 == 3:
			return fmt.Sprintf("%drd", num)
		default:
			return fmt.Sprintf("%dth", num)
		}
	case "fr":
		switch {
		case num == 1:
			return fmt.Sprintf("%der", num)
		default:
			return fmt.Sprintf("%de", num)
		}
	default:
		return fmt.Sprintf("%dx", num)
	}
}
