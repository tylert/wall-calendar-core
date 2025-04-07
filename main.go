//go:build !alt

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

	englishAustralia(u32)    // en-AU
	englishCanada(u32)       // en-CA
	englishGreatBritain(u32) // en-GB
	englishUnitedStates(u32) // en-US
	englishOther(u32)        // en-XX
}
