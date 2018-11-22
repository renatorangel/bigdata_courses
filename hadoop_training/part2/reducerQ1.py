#!/usr/bin/python

import sys
count = 0
for line in sys.stdin:
    data_mapped = line.strip().split()
    if len(data_mapped) != 3:
        # Something has gone wrong. Skip this line.
        continue

    get, page, http = data_mapped

    if page == "/assets/js/the-associates.js":
        count += 1

print count

