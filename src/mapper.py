#!/usr/bin/env python3
import sys
import csv

# Load data
data = csv.DictReader(sys.stdin)

# Prints/Passes values to reducer.py
for row in data:
    print('%s' % row[sys.argv[1]])