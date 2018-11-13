#!/usr/bin/python

import sys

salesTotal = 0
i = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisSale = data_mapped


    i = i + 1
    salesTotal += float(thisSale)

print i, "\t", salesTotal

