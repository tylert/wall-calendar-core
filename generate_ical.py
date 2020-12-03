#!/usr/bin/env python

from datetime import datetime

import click
from vobject import iCalendar


def generate_ical():
    '''
    '''

    # http://eventable.github.io/vobject/
    # https://en.wikipedia.org/wiki/ICalendar

    calendar = iCalendar()
    event = calendar.add('vevent')

    event.add('summary').value = 'WCARC'

    # utc = vobject.icalendar.utc
    # event.add('dtstart').value = datetime(2020, 2, 28, tzinfo=utc)
    event.add('dtstart').value = datetime(2020, 2, 28, 19)

    return calendar


# @click.command()
# @click.option('', '', default='', help='')
def main():
    '''
    '''

    calendar = generate_ical()
    print(calendar.serialize())


if __name__ == '__main__':
    main()
