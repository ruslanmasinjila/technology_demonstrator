import pandas as pd
import numpy as np

# Load training and test data
train_data = pd.read_csv("train.csv")
test_data = pd.read_csv("test.csv")

# Remove galaxy year from training and testing.
# I trust this is not time series.

del train_data["galactic year"]
del test_data["galactic year"]

print(list(train_data.columns))


