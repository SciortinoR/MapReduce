import sys
import pandas as pd

# Determine which dataframe to load
data = pd.DataFrame()
if sys.argv[1] == "train":
    data = pd.read_csv("../datasets/NDBench-training.csv")
elif sys.argv[1] == "test":
    data = pd.read_csv("../datasets/NDBench-testing.csv")
else:
    print("No dataset specified. Please specify 'rain' or 'test' for the respective dataset.")
    exit(0)

# Prints/Passes values to reducer.py
for value in data[sys.argv[2]].values.tolist():
    print('%s' % value)