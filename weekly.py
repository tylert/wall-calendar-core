#!/usr/bin/env python


from datetime import datetime, timedelta
from subprocess import Popen, PIPE

#pip install latex
#from latex import build_pdf


days = 30
date = datetime.today()
rembin = 'remind.fr'
remfile = 'source/top.rem'


for index in range(0, days):
    command = rembin + ' ' + remfile + ' ' + date.strftime('%Y-%m-%d')
    proc = Popen(command, shell=True, stdout=PIPE)
    errno = proc.wait()

    for line in proc.stdout:
        print(line)
    print('===')

    date += timedelta(days=1)  # add a day
