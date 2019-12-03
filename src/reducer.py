#!/usr/bin/env python3
import sys
import statistics

def print_stats(current_key, num_list):
    maximum = max(num_list)
    minimum = min(num_list)
    print("Column: %s\t # Data Pts.: %s\t Max: %s\t Min: %s\t Median: %s\t Std. Dev.: %s\n" \
                % (current_key, len(num_list), maximum, minimum, statistics.median(num_list), statistics.pstdev(num_list)))
    
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
