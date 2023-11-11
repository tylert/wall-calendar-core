package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

// Sun = 0, Mon = 1, Tue = 2, Wed = 3, Thu = 4, Fri = 5, Sat = 6
// 1st = 4, 2nd = 11, 3rd = 18, 4th = 25, 5th/last = 31(32)

func closest(nearby time.Time, desired uint32) time.Time {
	offset := -(int(nearby.Weekday()) - (int(desired) % 7))
	if offset < -3 {
		offset += 7
	}
	if offset > 3 {
		offset -= 7
	}
	found := nearby.AddDate(0, 0, offset)

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
	// fmt.Println(fmt.Sprintf("%s, %s %d, %d  %s", whatzit.Weekday(), whatzit.Month().String(), whatzit.Day(), whatzit.Year(), label))
	fmt.Println(fmt.Sprintf("%d-%02d-%02d  %s", whatzit.Year(), whatzit.Month(), whatzit.Day(), label))
}

func main() {
	// Print out the version information
	if aVersion {
		fmt.Println(GetVersion())
		os.Exit(0)
	}

	var (
		err error
		u64 uint64
		u32 uint32
	)

	if aYear != "" {
		u64, err = strconv.ParseUint(aYear, 10, 32)
		u32 = uint32(u64)

		if err != nil {
			fmt.Println("Error parsing uint32 string")
			os.Exit(2)
		}
	}

	englishCanada(u32)
	englishUnitedStates(u32)
	englishAustralia(u32)
}
