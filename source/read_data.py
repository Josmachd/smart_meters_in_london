import pandas as pd
from tqdm import tqdm
import os


class Data:    
    def __init__(self, path): # Get dir
        self.path, dirs, self.files = next(
            os.walk(path))
        self.file_count = len(self.files)
        
    def load(self): # Load the file into dataframe
        df_list = []
        
        df = pd.DataFrame()
        # append datasets to the list 
        for i in tqdm(range(self.file_count)):
            temp_df = pd.read_csv(self.path + self.files[i], low_memory=False)
            df_list.append(temp_df)
            df = pd.concat(df_list)
        print('\n')
        return df
