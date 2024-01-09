#!/usr/bin/env python


from datetime import date, timedelta


today_date = date.today()

# ---==[s]==---
s = today_date - date(2017, 10, 10)  # count up from a date
print(
    f'S^ {s.days} days, {s.days / 7:.2f} weeks, {s.days / 30:.2f} months, {s.days / 365:.2f} years'
)

# ---==[b]==---
if today_date.month > 6 or (today_date.month == 6 and today_date.day > 15):
    b = date(today_date.year + 1, 6, 15) - today_date  # count down to next mid-June
else:
    b = date(today_date.year, 6, 15) - today_date  # count down to this mid-June
print(
    f'Bv {b.days} days, {b.days / 7:.2f} weeks, {b.days / 30:.2f} months, {b.days / 365:.2f} years'
)
# v=10000;w=.1;x=1.1;y=1;z=.5;print(((v*.5*w*x)+(v*.5*w*x*y))*z)

# ---==[k]==---
k = date(2024, 2, 29) - today_date  # count down to a date
print(f'Kv {k.days} days, {k.days / 7:.2f} weeks, {k.days / 30:.2f} months, {k.days / 365:.2f} years')

d2 = date(2024, 2, 29)
daygenerator = (today_date + timedelta(x + 1) for x in range((d2 - today_date).days))
print(f'   {sum(1 for day in daygenerator if day.weekday() < 5)} weekdays')

# ---==[a]==---
a = date(2024, 4, 5) - today_date  # count down to a date
print(f'Av {a.days} days, {a.days / 7:.2f} weeks, {a.days / 30:.2f} months, {a.days / 365:.2f} years')

d2 = date(2024, 4, 5)
daygenerator = (today_date + timedelta(x + 1) for x in range((d2 - today_date).days))
print(f'   {sum(1 for day in daygenerator if day.weekday() < 5)} weekdays')
