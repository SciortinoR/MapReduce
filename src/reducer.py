#!/usr/bin/env python3
import sys
import statistics

def percentile90(num_list):
    n = max(int(round(0.9 * len(num_list) + 0.5)), 2)
    return num_list[n-2]

def print_stats(current_key, num_list):
    num_list.sort()
    maximum = max(num_list)
    minimum = min(num_list)

    print("Column: %s" % current_key)
    print("# of Samples: %s" % len(num_list))
    print("Maximum: %s" % maximum)
    print("Minimum: %s" % minimum)
    print("Median: %s" % statistics.median(num_list))
    print("Standard Deviation: %s" % statistics.pstdev(num_list))
    print("Value at or below which 90%% of samples are found (90th Percentile): %s" % percentile90(num_list)) 
    print("Normalized column values: ")
    for value in num_list:
        print((value - minimum) / (maximum - minimum))

key = None
current_key = None
num_list = []
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
            print_stats(current_key, num_list)
        num_list.clear()
        num_list.append(value)
        current_key = key

# Output last value if needed
if current_key == key:
    print_stats(current_key, num_list)
