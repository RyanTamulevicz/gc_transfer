import pandas as pd
from const import resource_path

class Data:
    def __init__(self):
        self.data = pd.read_csv(resource_path('src/data.csv'))

        self.data["amount"] = self.data["amount"].replace('[\$,]', '', regex=True).astype(float)
        self.data = self.data[self.data["amount"] != 0.00]
        self.data["amount"] = self.data["amount"].map(lambda x: f"{x:.2f}")
