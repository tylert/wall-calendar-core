#!/usr/bin/env bash

# https://jol.dev/blog/2021-11-16-n2-sed-challenge-join-cal-y-months-into-a-single-column.html

sed -E '1,2d;s/(.{20})   /\1\n/g;' |\
sed -E '
  # Middle column months
  2~3 {
    # Month-trios are 24 lines = 3 month columns * (monthline + weeklabel + max
    # 6-week coverage of a month)
    2~24h
    2~24! {
      H

      # Move line to where it belongs at the middle, using the right-month
      # name as an anchor to find the end of the middle month.
      #
      # For when there are less than 3 lines in the hold space, nothing needs
      # to be done. It"s only from the third line onwards that they must be
      # moved. This means that we can count on there being at least 2 newlines.
      x
      s/\n( +[A-Z][^\n]+.*)\n([^\n]*)$/\n\2\n\1/
      x
    }
  }

  # Right column months
  3~3 {H}

  $b get_held_months # no next trio, prepare to print held months

  # Only print on lines of left month (and at EOF via jump on previous line).
  1~3!d

  # New month-trio
  /^ +[A-Z]/ {
    1b # Skip for first line

    # Append, so the months held end up effectively prepended when they"re
    # gotten.
    H

    : get_held_months

    # Get the sorted middle and right month lines to output them.
    g
  }
' |\
sed -E '
  # Save the month name
  /^ +[A-Z]/{s/ //g;h}

  # Delete everything but the date lines
  /^ *[1-9]/!d

  # If on the week with the first of the month, add the month name to the right.
  /\b1\b/{G;s/\n/ /}
' |\
sed -E '
  # Not 7 days this week?
  /[0-9]+(\s+[0-9]+){6}/!{
    # and isn"t the first week of the first month?
    1b

    # We must be at the end of the month. Bring the start of the next month.
    N

    # Join the start of the next to this end.
    s/ +\n +/  /
  }
'
