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

= 2025
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
