from paper_cal import scan_for, WEDNESDAY, THURSDAY, WEEK1, WEEK2, WEEK3


def main():
  '''
  '''

  # Ottawa Amateur Radio Club executive meetings are the 1st Wednesday of each
  # month except July and August
  # Ottawa Amateur Radio Club regular meetings are the 2nd Wednesday of each
  # month except July and August
  # https://www.oarc.net/
  for year in (2020, 2021):
      for month in (1, 2, 3, 4, 5, 6, 9, 10, 11, 12):
          # exécutif
          print(scan_for(WEDNESDAY, year, month, WEEK1), end='')
          print(':  1900-2100:  OARC Exec Meeting')
          print(scan_for(WEDNESDAY, year, month, WEEK2), end='')
          print(':  1930-2200:  OARC Meeting')

  # Rideau Lakes Amateur Radio Club meetings are the 3rd Thursday of each month
  # https://www.ve3rlr.ca/p/about.html
  for year in (2020, 2021):
      for month in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
          print(scan_for(THURSDAY, year, month, WEEK3), end='')
          print(':  RLARC Meeting')


if __name__ == '__main__':
    main()
