import matplotlib.pyplot as plt
import pandas as pd
from machinecode.pydsstools.pydsstools.heclib.dss import HecDss
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler

from machinecode.pydsstools.pydsstools.heclib.dss.HecDss import Open

dss_file = "C:\\Users\\HEC\\Desktop\\DssFiles\\FlowData.dss"
pathname = "/CUMBERLAND RIVER/BARBOURVILLE/FLOW//30MIN/OBS/"
pathname2 = "/CUMBERLAND RIVER/CUMBERLAND FALLS/FLOW//30MIN/MISSING/"
pathname3 = "/CUMBERLAND RIVER/CUMBERLAND FALLS/FLOW//30MIN/OBS/"
pathname4 = "/CUMBERLAND RIVER/WILLIAMSBURG/FLOW//30MIN/OBS/"

fid = HecDss.Open(dss_file)
pathArr = [pathname, pathname2, pathname3, pathname4]
names = ["data1", "data2", "data3", "data4"]

# we have to now replace -901 to missing values in the dataframe
ts = fid.read_ts(pathname)
values = ts.values
df = pd.DataFrame(ts.pytimes, columns=['Dates'])
df.set_index('Dates', inplace=True)
i = 0
for path in pathArr:
    ts = fid.read_ts(path)
    df[names[i]] = ts.values
    i += 1

df.loc[(df['data2'] < 0, 'data2')] = np.NaN
file = df.to_csv("flowData.csv")

# # a problem that needs to be done is inserting values from dataset date and times
dataSet = pd.read_csv("flowData.csv", index_col=0, parse_dates=True)
dataSet.loc['11/1/2019  12:00:00 AM':'31/1/2020  23:00:00'].plot(subplots=True, figsize=(24, 18))
plt.legend(loc='best')
plt.xticks(rotation='vertical')
plt.show()

# we create a date column to extract the week number
dataSet['Dates'] = dataSet.index
# apply a lambda function to the whole panda dataframe column
dataSet['week'] = dataSet['Dates'].apply(lambda x: x.isocalendar()[1])
# drop the date column because we dont need it
del dataSet['Dates']
# del dataSet['week']
# let see our dataframe
dataSet.head()

corr = dataSet.corr()
print(corr)

ax = sns.heatmap(corr,
                 xticklabels=corr.columns.values,
                 yticklabels=corr.columns.values, annot=True)


X_train = dataSet.loc['24/11/2019  00:00:00':'01/1/2020  00:00:00',['data1','data3','week']].astype(np.float32).values
y_train = dataSet.loc['24Nov2019  0000':'01Jan2020  0000','data2'].astype(np.float32).values

scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
#
# placeHolder= X_train[:20]


# look at dss file to see what mising value defaults to
