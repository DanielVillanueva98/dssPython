import matplotlib.pyplot as plt
import pandas as pd
from machinecode.pydsstools.pydsstools.heclib.dss import HecDss


dss_file = "C:\\Users\\HEC\\Desktop\\DssFiles\\FlowData.dss"
pathname = "/CUMBERLAND RIVER/BARBOURVILLE/FLOW//30MIN/OBS/"

fid = HecDss.Open(dss_file)
ts = fid.read_ts(pathname)
values = ts.values
i = 0
dates = []
data = []

while i < 30:
    dates.append(str(ts.pytimes[i]))
    data.append(values[i])
    i += 1

dataSet = {'Dates': dates, 'Data': data}
df = pd.DataFrame(dataSet)

df.plot(x='Dates',y='Data',kind='line')
plt.show()


















# for info in values:
#     dates.append(str(ts.pytimes[i]))
#     data.append(info)
#     # print(str(ts.pytimes[i]) + "," + str(data))
#     # print(str(ts.pytimes[i]))
#     i += 1


# plt.plot(times[~ts.nodata],values[~ts.nodata],"o")
# plt.show()
# fid.close()
