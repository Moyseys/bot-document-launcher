import pandas as pd
import json

with open("logs.json", "r") as file:
    data = json.load(file)

data_frame = pd.json_normalize(data)
data_frame.to_excel("logs_vizualization.xlsx", index=False)
