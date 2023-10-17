# csvtojson
Quick and simple CSV to JSON converter with ability for up to 2 column categories

## Rules
1. File must be CSV format, delimited by commas
2.  Remove ALL commas from cells
3.  Convert all numbers to "Number" format and remove thousands-separator (e.g. $42,000 -> 42000)
4.  Make sure category columns have text in every cell
5.  If JSON is broken at the end, try selecting all empty cells and deleting them
