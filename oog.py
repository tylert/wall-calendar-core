#!/usr/bin/env python

from paper_cal import moon_phase, DAYS_IN_MONTH


year = 2020
month = 2

for i in range(1, DAYS_IN_MONTH[month]+1):
    print(moon_phase(year, month, i), end='')
    print(' {}'.format(i))
