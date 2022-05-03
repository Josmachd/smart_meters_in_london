import pandas as pd
from sklearn import preprocessing


class Dataframe:
    def __init__(self, df): # Create dataframe
        self.frame = df

    def c_drop(self, dlist): # Drop columns
        self.frame = self.frame.drop(self.frame.columns[dlist], axis=1)
        
    def remove_counts(self, param,  n):  # Remove rows with low occurence
        h = self.frame[param].value_counts() > 650
        self.frame = self.frame[self.frame[param].isin(h[h].index)]

    def scale(self): # Scale the data
        min_max_scaler = preprocessing.StandardScaler()
        np_scaled = min_max_scaler.fit_transform(self.frame)
        self.frame = pd.DataFrame(np_scaled)
        
