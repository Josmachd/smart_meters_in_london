import pandas as pd
import numpy as np

from read_data import Data
from df_treat import Dataframe
from isolation_model import Iso
from plot import *


# =================================== Energy Data =================================== #


path = "data/daily_dataset/"
data = Data(path)
# Limit files (comment if you want to use all 112 files)
data.file_count = 10
data = Dataframe(data.load())

#Data treatment
data.frame.dropna()
data.c_drop([2,3,4,5,6,8])
data.frame.columns = ['house', 'time', 'energy']
data.frame['time'] = pd.to_datetime(data.frame['time'], format="%Y/%m/%d")

data.remove_counts('house', 650)

# Monday=0, Sunday=6
data.frame['DayOfTheWeek'] = data.frame['time'].dt.dayofweek
# Weekday=1, weekend=0
data.frame['WeekDay'] = (data.frame['DayOfTheWeek'] < 5).astype(int)
# Write time as integer 
data.frame['day_int'] = (data.frame['time'].astype(np.int64)/100000000000).astype(np.int64)
# January= 0, December=13
data.frame['MonthOfTheYear'] = data.frame['time'].dt.month


# =================================== Weather Data =================================== #


path ="data/weather_daily_darksky/"
weather = Data(path)
weather = Dataframe(weather.load())

#Data treatment
weather.frame.dropna()
weather.c_drop(
    [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,22,23,24,25,26,27,28,29,30,31]
)
weather.frame.columns = ['max', 'time', 'min']
weather.frame['time'] = pd.to_datetime(weather.frame['time'], format="%Y/%m/%d")

# Temperature mean
weather.frame['mean'] = (weather.frame["max"] + weather.frame["min"]) / 2

# Merge weather into main df
#print(data.frame.info())
#data.frame = data.frame.merge(weather.frame, left_on='time', right_on='time')
#print(data.frame.info())


# =================================== Isolation Forest =================================== #

# Create traning dataset
train = Dataframe(data.frame[['energy', 'WeekDay', 'MonthOfTheYear','DayOfTheWeek']])
train.scale()

# Apply model
iso = Iso(0.005)
iso.fit(train.frame)
data.frame['anomaly_forest'] = pd.Series(iso.predict(train.frame), dtype='float64')
print(data.frame['anomaly_forest'].value_counts())
print('\n')

# Plot resolts
plot1(data.frame)
plot2(data.frame)
plot3(data.frame)
show_plots()
