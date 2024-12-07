//go:build alt

package main

import (
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
			os.Exit(2)
		}
	}

	englishCanada(u32)
	englishGreatBritain(u32)
	englishUnitedStates(u32)
	englishAustralia(u32)
	englishOther(u32)
	englishPersonal(u32)
}
