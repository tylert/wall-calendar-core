Using
-----

::

    # Initial setup
    make venv ; source .venv/bin/activate

    # Show all events for this year
    ( ./holiday_canada.py ; \
      ./holiday_religious.py ; \
      ./holiday_other.py ) | sort

    # Find out when the next few Easters will occur
    for (( year=2022 ; year<2033 ; year++ )); do
        ./holiday_religious.py --year $year | grep 'Easter Sunday'
    done


Docs
----

* https://docs.python.org/3/library/datetime.html
* https://docs.python.org/3/library/calendar.html
* PyMeeus https://pymeeus.readthedocs.io/en/latest/
* Pyluach https://pyluach.readthedocs.io/en/latest/

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
