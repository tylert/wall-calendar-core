#!/usr/bin/env python


import time


def countdown(seconds=None):
    while seconds > 0:
        mins = seconds // 60
        secs = seconds % 60
        timer = f'{mins:02d}:{secs:02d}'
        print(timer, end='\r') # overwrite previous line
        time.sleep(1)
        seconds -= 1
    print('Next speaker!!!')


countdown(seconds=180)
