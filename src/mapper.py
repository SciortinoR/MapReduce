import sys
import pandas as pd

# Load data
data = pd.read_csv(sys.stdin)

# Prints/Passes values to reducer.py
for value in data[sys.argv[1]].values.tolist():
    print('%s' % value)