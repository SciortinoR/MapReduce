import sys
import numpy as np

num_list = np.array([])

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
    num_list = np.append(num_list, value)
    print("Iteration %s\t --> Max: %s\t Min: %s\t Median: %s\t Standard Deviation: %s" \
        % (num_list.shape[0], np.max(num_list), np.min(num_list), np.median(num_list), np.std(num_list)))

