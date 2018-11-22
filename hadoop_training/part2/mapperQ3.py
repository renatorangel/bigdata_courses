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


            data_mapped = request_line.split()
            if len(data_mapped) != 3:

                continue

            type, address, http = data_mapped
            address = address.replace("http://www.the-associates.co.uk", "")
            print "{0}".format(address)
