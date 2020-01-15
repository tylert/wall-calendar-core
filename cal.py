#!/usr/bin/env python

from calendar import HTMLCalendar


class Hoojah:
    def __init__(self, year, month):
        self.year = year
        self.month = month

    def __repr__(self):
        return HTMLCalendar().formatmonth(self.year, self.month)


print(Hoojah(2020, 1))
