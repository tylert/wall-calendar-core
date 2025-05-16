Using
-----

::

    # Initial setup
    make venv && source .venv/bin/activate

    # Show all events for this year
    ( go run . --year 2024 ; \
        ./holiday_other.py --year 2024 ) | sort

    # Find out when the next few Easters will occur
    for (( year=2024 ; year<2034 ; year++ )); do
        go run . --year ${year} | grep 'Easter Sunday'
    done


Golang
------

* https://github.com/rickar/cal/blob/master/v2/holiday.go  Easter and structs?
* https://dates.gmarts.org/eastalg.htm  Easter algorithms
* https://github.com/soniakeys/meeus  aphelion, perihelion, solstice, etc.
* https://github.com/janczer/goMoonPhase  Golang moon phase
* https://github.com/yamadayuki/go-calendar
* https://github.com/floAr/calendargo  example of building calendars using gg
* https://github.com/fogleman/gg  2d drawings
* https://github.com/jbreckmckye/daylight  network-based sunset/sunrise times


Links
-----

* https://ilyabirman.net/forebruary
* https://elf.org/moons/index.html  beautiful moon calendars
* https://www.farmersalmanac.com/astronomy/fullmoonnames.html
* https://stackoverflow.com/questions/704108/how-do-i-compute-equinox-solstice-moments
* https://jol.dev/blog/2021-11-16-n2-sed-challenge-join-cal-y-months-into-a-single-column.html
* https://github.com/jimblandy/spiral-calendar
* https://georgexyz.com/python-calendar-app.html
* https://github.com/lynxur/Kalender
* https://arrow.readthedocs.io/en/latest/index.html
* https://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/calendar/calendars
* https://stackoverflow.com/questions/7276017/producing-a-printable-calendar-with-python
* https://quasar.as.utexas.edu/BillInfo/ReligiousCalendars.html
* https://github.com/aharmon413/moon-project
* https://github.com/alohaas/lun-phase
* https://www.timeanddate.com/calendar/determining-easter-date.html
* https://www.assa.org.au/edm
* https://bloben.com  CalDAV client
* https://github.com/nibdo/bloben-app  source for bloben CalDAV client
* https://endler.dev/2022/zerocal  just the event, please!
* https://github.com/vacanza/python-holidays
* https://www.futilitycloset.com/2024/05/24/day-tripper  calculate weekday number for any date
* https://typst.app/universe/package/cineca
* https://github.com/HPDell/typst-cineca
* https://github.com/extua/october
* https://forum.typst.app/t/how-to-split-a-list-of-calendar-entries-by-month/824
* https://terokarvinen.com/2021/calendar-txt
* https://todotxt.org
* https://hueffner.de/falk/blog/a-leap-year-check-in-three-instructions.html
