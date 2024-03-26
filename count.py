#!/usr/bin/env python


from datetime import date, timedelta


t = date.today()

# ---==[e]==---
e = t - date(2017, 10, 10)  # count up from a date
print(
    f'e^ {e.days} days, {e.days / 7:.2f} weeks, {e.days / 30:.2f} months, {e.days / 365:.2f} years'
)

# ---==[b]==---
if t.month > 6 or (t.month == 6 and t.day > 15):
    b = date(t.year + 1, 6, 15) - t  # count down to next mid-June
else:
    b = date(t.year, 6, 15) - t  # count down to this mid-June
print(
    f'bv {b.days} days, {b.days / 7:.2f} weeks, {b.days / 30:.2f} months, {b.days / 365:.2f} years'
)
daygen = (t + timedelta(x + 1) for x in range(b.days))
print(f'   {sum(1 for x in daygen if x.weekday() < 5)} workdays')
# v=10000;w=.1;x=1.1;y=1;z=.5;print(((v*.5*w*x)+(v*.5*w*x*y))*z)

# ---==[f]==---
f = date(2024, 4, 5) - t  # count down to a date
print(f'fv {f.days} days, {f.days / 7:.2f} weeks, {f.days / 30:.2f} months, {f.days / 365:.2f} years')
daygen = (t + timedelta(x + 1) for x in range(f.days))
print(f'   {sum(1 for x in daygen if x.weekday() < 5)} workdays')
