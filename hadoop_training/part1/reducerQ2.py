#!/usr/bin/python

import sys

old_key = None
maximum_value_store = 0
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next item category

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_maximum_value = data_mapped

    this_maximum_value = float(this_maximum_value)

    if old_key and old_key != this_key:
        print old_key, "\t", maximum_value_store
        maximum_value_store = this_maximum_value

    old_key = this_key
    if this_maximum_value > maximum_value_store:
        maximum_value_store = this_maximum_value

if old_key != None:
    print old_key, "\t", maximum_value_store

