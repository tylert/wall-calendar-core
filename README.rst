Using
-----

::

    # Initial setup
    make venv && source .venv/bin/activate

    # Show all events for this year
    ( go run . --year 2024 ; \
        ./holiday_religious.py --year 2024 ; \
        ./holiday_other.py --year 2024 ) | sort

    # Find out when the next few Easters will occur
    for (( year=2024 ; year<2034 ; year++ )); do
        ./holiday_religious.py --year ${year} | grep 'Easter Sunday'
    done


Golang
------

* https://github.com/rickar/cal/blob/master/v2/holiday.go  Easter and structs?
* http://dates.gmarts.org/eastalg.htm  Easter algorithms
* https://github.com/soniakeys/meeus  aphelion, perihelion, solstice, etc.
* https://github.com/janczer/goMoonPhase  Golang moon phase
* https://www.golangprograms.com/golang-package-examples/example-to-use-weekday-and-yearday-function.html
* https://www.golangprograms.com/regular-expression-to-extract-date-yyyy-mm-dd-from-string.html
* https://github.com/yamadayuki/go-calendar
* https://github.com/floAr/calendargo  example of building calendars using gg
* https://github.com/fogleman/gg  2d drawings

::

    AU     Australia/Australie
    BD     Bangladesh/Bangladesh
    CA-AB  Canada - Alberta
    CA-BC  Canada - British Columbia/Colombie-Britannique
    CA-MB  Canada - Manitoba
    CA-NB  Canada - New Brunswick/Nouveau Brunswick
    CA-NL  Canada - Newfoundland and Labrador/Terre-Neuve-et-Labrador
    CA-NS  Canada - Nova Scotia/Nouvelle-Écosse
    CA-NT  Canada - Northwest Territories/Territoires du Nord-Ouest
    CA-NU  Canada - Nunavut/ᓄᓇᕗᑦ
    CA-ON  Canada - Ontario
    CA-PE  Canada - Prince Edward Island/Île-du-Prince-Édouard
    CA-QC  Canada - Quebec/Québec
    CA-SK  Canada - Saskatchewan
    CA-YT  Canada - Yukon
    JP     Japan/Japon
    NZ     New Zealand/Nouvelle-Zélande
    UK     United Kingdom of Great Britain and Northern Ireland/Royaume-Uni de Grande-Bretagne et d'Irlande du Nord
    UN     United Nations/Les Nations Unies
    US     United States of America/Les États-Unis d'Amérique


Links
-----

* https://en.wikipedia.org/wiki/ISO_3166-2:CA
* https://en.wikipedia.org/wiki/ISO_3166-2:ES
* https://ilyabirman.net/forebruary/
* https://elf.org/moons/index.html  beautiful moon calendars
* http://www.farmersalmanac.com/astronomy/fullmoonnames.html
* https://stackoverflow.com/questions/704108/how-do-i-compute-equinox-solstice-moments
* https://jol.dev/blog/2021-11-16-n2-sed-challenge-join-cal-y-months-into-a-single-column.html
* https://github.com/jimblandy/spiral-calendar
* https://georgexyz.com/python-calendar-app.html
* https://github.com/lynxur/Kalender
* https://arrow.readthedocs.io/en/latest/index.html
* http://cvsweb.openbsd.org/cgi-bin/cvsweb/src/usr.bin/calendar/calendars/
* http://stackoverflow.com/questions/7276017/producing-a-printable-calendar-with-python
* http://quasar.as.utexas.edu/BillInfo/ReligiousCalendars.html
* http://www.ben-daglish.net/moon.shtml
* https://www.timeanddate.com/calendar/determining-easter-date.html
* https://www.assa.org.au/edm
* https://bloben.com/  CalDAV client
* https://github.com/nibdo/bloben-app  source for bloben CalDAV client
* https://endler.dev/2022/zerocal/  just the event, please!
