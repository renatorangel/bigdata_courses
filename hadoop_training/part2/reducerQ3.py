#!/usr/bin/python
import sys

biggest_url = None
count_biggest_url = 0

count_old_url = 0
old_url = None

for line in sys.stdin:
    address = line.strip()

    if old_url and old_url != address:
        if count_old_url > biggest_url:
            biggest_url = old_url
            count_biggest_url = count_old_url

        # print old_url, "\t", count_old_url

        old_url = address;
        count_old_url = 0

    old_url = address
    count_old_url += 1

print biggest_url, "\t", count_biggest_url
