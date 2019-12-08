#!/usr/bin/env python3
import sys
import math
import statistics

key = None
current_key = None
num_list = []

PERCENTILE = 0.9

def percentile():
    num_list.sort()
    index = PERCENTILE * len(num_list) + 0.5
    if index % 0.5 == 0:
        index = math.ceil(index)
    else:
        round(index)
    return num_list[int(index) - 1]

def print_stats():
    maximum = max(num_list)
    minimum = min(num_list)

    print("Column: %s" % current_key)
    print("# of Samples: %s" % len(num_list))
    print("Maximum: %s" % maximum)
    print("Minimum: %s" % minimum)
    print("Median: %s" % statistics.median(num_list))
    print("Standard Deviation: %s" % statistics.pstdev(num_list))
    print("Value below which 90%% of samples are found (90th Percentile): %s" % percentile()) 
    print("Normalized column values [0-1]: ")
    for value in num_list:
        print((value - minimum) / (maximum - minimum))

for line in sys.stdin:
    # Remove leading and trailng whitespace
    line = line.strip()

    # Parse input 
    key, value = line.split('\t', 1)

    # Convert string to float
    try:
        value = float(value)
    except ValueError:
        # Skip the value
        continue

    if current_key == key:
        num_list.append(value)
    else:
        if current_key:
            print_stats()
        num_list.clear()
        num_list.append(value)
        current_key = key

# Output last value if needed
if current_key == key:
    print_stats()
