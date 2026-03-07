//go:build !alt

package main

import (
	"container/list"
	"fmt"
	"os"
	"strconv"
)

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
			os.Exit(1)
		}
	}

	e := list.New()
	englishAustralia(u32, e)    // en-AU
	englishCanada(u32, e)       // en-CA
	englishGreatBritain(u32, e) // en-GB
	englishUnitedStates(u32, e) // en-US
	englishOther(u32, e)        // en-XX

	for x := e.Front(); x != nil; x = x.Next() {
		y := Event(x.Value.(Event))
		print_date(y.date, y.label)
	}
}
