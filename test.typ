#set page(
  "us-letter",
  margin: (
    top: 1cm,
    bottom: 1cm,
    left: 1cm,
    right: 1cm,
  ),
)

#set text(
  10pt,
  font: "DejaVu Sans Mono",
  fill: gray,
)

// Wednesday start, not a leap year
= 2025/2031/2042/2053
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(29, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 3+1).map(str), // padding
)

// Thursday start, not a leap year
= 2026/2037/2043/2054
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(28, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 2+1).map(str), // padding
)

// Friday start, not a leap year
= 2027/2038/2049/2055
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(27, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 1+1).map(str), // padding
)

// Saturday start, leap year
= 2028/2056
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(26, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 29+1).map(str), // DEC
  [30/31]
)

// Monday start, not a leap year
= 2029/2035/2046/2057
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(31, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 5+1).map(str), // padding
)

// Tuesday start, not a leap year
= 2030/2041/2047/2058
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(30, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 4+1).map(str), // padding
)

// Thursday start, leap year
= 2032
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(28, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 1+1).map(str), // padding
)

// Saturday start, not a leap year
= 2033/2039/2050
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(26, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
)

// Sunday start, not a leap year
= 2034/2045/2051
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 28+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 6+1).map(str), // padding
)

// Tuesday start, leap year
= 2036
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(30, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 3+1).map(str), // padding
)

// Sunday start, leap year
= 2040
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 5+1).map(str), // padding
)

// Friday start, leap year
= 2044
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(27, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
)

// Wednesday start, leap year
= 2048
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(29, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 2+1).map(str), // padding
)

// Monday start, leap year
= 2052
#grid(
  columns: 7,
  column-gutter: 10pt,
  row-gutter: 6pt,
  ..range(31, 31+1).map(str), // padding
  text(stroke: black)[1],..range(2, 31+1).map(str), // JAN
  text(stroke: black)[1],..range(2, 29+1).map(str), // FEB
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAR
  text(stroke: black)[1],..range(2, 30+1).map(str), // APR
  text(stroke: black)[1],..range(2, 31+1).map(str), // MAY
  text(stroke: black)[1],..range(2, 30+1).map(str), // JUN
  text(stroke: black)[1],..range(2, 31+1).map(str), // JUL
  text(stroke: black)[1],..range(2, 31+1).map(str), // AUG
  text(stroke: black)[1],..range(2, 30+1).map(str), // SEP
  text(stroke: black)[1],..range(2, 31+1).map(str), // OCT
  text(stroke: black)[1],..range(2, 30+1).map(str), // NOV
  text(stroke: black)[1],..range(2, 31+1).map(str), // DEC
  ..range(1, 4+1).map(str), // padding
)
