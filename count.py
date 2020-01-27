#!/usr/bin/env python

from datetime import date, timedelta


today_date = date.today()

# ---==[b]==---
if today_date.month >= 6:
    b = date(today_date.year + 1, 6, 1) - today_date  # count down to next June
    print('Bv {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(b.days, b.days / 7, b.days / 30, b.days / 365))
else:
    b = date(today_date.year, 6, 1) - today_date  # count down to this June
    print('Bv {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(b.days, b.days / 7, b.days / 30, b.days / 365))

# ---==[c]==---
c = today_date - date(2018, 11, 5)  # count up from start date
print('C^ {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(c.days, c.days / 7, c.days / 30, c.days / 365))

# ---==[e]==---
e = today_date - date(2017, 10, 10)  # count up from start date
print('E^ {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(e.days, e.days / 7, e.days / 30, e.days / 365))

# ---==[d]==---
# d = date(2017, 10, 10) + timedelta(days=365 * 2) - today_date  # count down to date
# print('Dv {} days, {:.2f} weeks, {:.2f} months, {:.2f} years'.format(d.days, d.days / 7, d.days / 30, d.days / 365))
