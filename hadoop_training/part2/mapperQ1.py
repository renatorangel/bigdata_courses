#!/usr/bin/python

import sys
import re

for line in sys.stdin:
    regex = '([(\d\.)]+) (-|\w+) (-|\w+) \[(.*?)\] "(.*?)" (\d+) (\d+|-)'

    match = re.match(regex, line)
    if match is not None:
        data = match.groups()

        if len(data) == 7:
            ip, first_dash, second_dash, time_date, request_line, status_code, size = data
            print "{0}".format(request_line)
