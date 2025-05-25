package main

import (
	"fmt"
	"os"
	"strconv"
	"time"
)

func wednesdays(year uint32) {
	var t time.Time

	// every Wednesday of the year
	t = find_nearby_date(fmt.Sprintf("%04d-%02d-%02d", year, time.January, Month1st), uint32(time.Wednesday))
	for i := 0; i < 53; i++ {
		if int(year) == t.Year() {
			print_date(t, "")
		}
		t = t.AddDate(0, 0, 7)
	}
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

	wednesdays(u32)
}
