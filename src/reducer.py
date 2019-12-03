#!/usr/bin/env python3
import sys
import statistics

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
            print("Column: %s\t # Data Points: %s\t Max: %s\t Min: %s\t Median: %s\t Standard Deviation: %s" \
                % (current_key, len(num_list), max(num_list), min(num_list), statistics.median(num_list), statistics.pstdev(num_list)))
        num_list.clear()
        num_list.append(value)
        current_key = key

# Output last value if needed
if current_key == key:
    print("Column: %s\t # Data Points: %s\t Max: %s\t Min: %s\t Median: %s\t Standard Deviation: %s" \
                % (current_key, len(num_list), max(num_list), min(num_list), statistics.median(num_list), statistics.pstdev(num_list)))
