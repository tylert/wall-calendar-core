#!/usr/bin/env python

from datetime import date, timedelta


today_date = date.today()

# ---==[b]==---
day = 15
if today_date.month >= 6 and today_date.day > day:
    b = date(today_date.year + 1, 6, day) - today_date  # count down to next mid-June
    print('Bv {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(b.days, b.days / 7, b.days / 30, b.days / 365))
else:
    b = date(today_date.year, 6, day) - today_date  # count down to this mid-June
    print('Bv {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(b.days, b.days / 7, b.days / 30, b.days / 365))

# ---==[s]==---
s = today_date - date(2020, 3, 9)  # count up from start date
print('S^ {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(s.days, s.days / 7, s.days / 30, s.days / 365))

# ---==[e]==---
e = today_date - date(2017, 10, 10)  # count up from start date
print('E^ {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(e.days, e.days / 7, e.days / 30, e.days / 365))

# ---==[d]==---
# d = date(2017, 10, 10) + timedelta(days=365 * 2) - today_date  # count down to date two years later
# print('Dv {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(d.days, d.days / 7, d.days / 30, d.days / 365))
