import pandas as pd
import numpy as np

import os
from sklearn import metrics
from sklearn.ensemble.forest import RandomForestRegressor
from matplotlib.pyplot import axis
from builtins import int
from nbformat.notebooknode import from_dict

def softmax(A):
    expA = np.exp(A)
    return expA / expA.sum()

def setNumerics(df, colName):
    fld = df[colName]

pd.set_option('display.expand_frame_repr', False)
dtypes = {"ReceivedTimestamp":"str"}

df = pd.read_csv( "ITM_20190121.csv", dtype = dtypes, low_memory = False)
# df = df.drop(columns="ID").drop(columns="Vin").drop(columns="ProcessedTimestamp")
# df[[c for c in df if df[c].isnull().sum() < 2]]

# df = pd.DataFrame({"ReceivedTimestamp":pd.date_range('02:00:00', periods=4, freq='23H')})

df = df[df["TripState"] == "Engine On"]

print("test run")
timeList = []

temp = 0
for i in df["ReceivedTimestamp"]:
    newStr = i
    intVal = i[0:5].split(":")
    intVal2 = (int(intVal[0]) *3600) + (int(intVal[1]) * 60)
    timeList.append(intVal2)
    temp += 1
    if temp == 100:
        break


print(timeList)

features = df["DeviceSerial"]
targets = [0, 7200, 14400, 21600, 28800, 36000, 43200, 50400, 57600, 64800, 72000, 79200]

df_pre = {'Times':timeList}
df_x = np.array(timeList)
df2_pre = {'Targets':targets}
df_y = np.array(targets)

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))


# m.fit(timeList, df["ReceivedTimestamp"])
# m.predict("ReceivedTimestamp")
