#!/usr/bin/env python


from datetime import date, timedelta


today_date = date.today()

# ---==[b]==---
if today_date.month > 6 or (today_date.month == 6 and today_date.day > 15):
    b = date(today_date.year + 1, 6, 15) - today_date  # count down to next mid-June
else:
    b = date(today_date.year, 6, 15) - today_date  # count down to this mid-June
print(
    f'Bv {b.days} days, {b.days / 7:.2f} weeks, {b.days / 30:.2f} months, {b.days / 365:.2f} years'
)
# v=10000;w=.1;x=1.1;y=1;z=.5;print(((v*.5*w*x)+(v*.5*w*x*y))*z)

# ---==[s]==---
s = today_date - date(2017, 10, 10)  # count up from a date
print(
    f'S^ {s.days} days, {s.days / 7:.2f} weeks, {s.days / 30:.2f} months, {s.days / 365:.2f} years'
)

# ---==[a]==---
a = date(2024, 4, 5) - today_date  # count down to a date
print(f'Av {a.days} days, {a.days / 7:.2f} weeks, {a.days / 30:.2f} months, {a.days / 365:.2f} years')
