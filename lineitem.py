#!/usr/bin/python3

# Line item is a module that makes it very simple to output
# well formated tables of information created by iterated 
# processes.

# column_names stores an ordered list of the column headers.

# column_prod stores a list of the generators for each of 
# columns.

# These are some miscellaneous parameters that control 
# how the table is printed.

class LineItem:
    column_names = []
    column_prod = []

    __init__():


# Generate Line - genline()
# iterate through column_prod generators, evaluating each item
# compose each item into a line
    genline():
        for a in column_prod:
            print(line.format(eval(a)))

# Lots of ways to do pretty printing...
# result = somefunction()
# print(str(result).rjust(4))
# print("{0.4d}".format(result))
