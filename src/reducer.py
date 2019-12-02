#!/usr/bin/env python3
import sys
import statistics

num_list = []

for value in sys.stdin:
    # Remove leading and trailng whitespace
    value = value.strip()

    # Convert string to int
    try:
        value = float(value)
    except ValueError:
        # Skip the value
        continue

    # Append number and calculate stats for every iteration
    num_list.append(value)
    print("Iteration %s\t --> Max: %s\t Min: %s\t Median: %s\t Standard Deviation: %s" \
        % (len(num_list), max(num_list), min(num_list), statistics.median(num_list), statistics.pstdev(num_list)))

