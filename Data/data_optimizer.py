import math
import pandas as pd

input_data = pd.read_csv("HRDataset_v13.csv")

output_data = input_data.dropna(how="all")

print(output_data)

output_data.to_csv("HRDataset_v14.csv")
