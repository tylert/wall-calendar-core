#!/usr/bin/env python

from datetime import date, timedelta


today_date = date.today()

# ---==[b]==---
if today_date.month > 6 or (today_date.month == 6 and today_date.day > 15):
    b = date(today_date.year + 1, 6, 15) - today_date  # count down to next mid-June
else:
    b = date(today_date.year, 6, 15) - today_date  # count down to this mid-June
print(f'Bv {b.days} days, {b.days / 7:.2f} weeks, {b.days / 30:.2f} months, {b.days / 365:.2f} years')

# ---==[e]==---
e = today_date - date(2017, 10, 10)  # count up from date
print(f'E^ {e.days} days, {e.days / 7:.2f} weeks, {e.days / 30:.2f} months, {e.days / 365:.2f} years')

# ---==[r]==---
# r = date(2021, 6, 1) + timedelta(days=365 * 10) - today_date  # count down to date ten years in the future
# print(f'Rv {r.days} days, {r.days / 7:.2f} weeks, {r.days / 30:.2f} months, {r.days / 365:.2f} years')
