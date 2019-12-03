#!/usr/bin/env python3
import sys
import csv

# Load data
data = csv.DictReader(sys.stdin, fieldnames=("CPUUtilization_Average", "NetworkIn_Average", "NetworkOut_Average", "MemoryUtilization_Average", "Final_Target"))

# Prints/Passes key-value (col-value) to reducer.py
for row in data:
    print('%s\t%s' % (sys.argv[1], row[sys.argv[1]]))