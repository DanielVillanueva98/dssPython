import matplotlib.pyplot as plt
import pandas as pd
from machinecode.pydsstools.pydsstools.heclib.dss import HecDss
from machinecode.pydsstools.pydsstools.heclib.dss.HecDss import Open

dss_file = "C:\\Users\\HEC\\Desktop\\DssFiles\\FlowData.dss"
pathname = "/CUMBERLAND RIVER/BARBOURVILLE/FLOW//30MIN/OBS/"
pathname2 = "/CUMBERLAND RIVER/CUMBERLAND FALLS/FLOW//30MIN/MISSING/"
pathname3 = "/CUMBERLAND RIVER/CUMBERLAND FALLS/FLOW//30MIN/OBS/"
pathname4 = "/CUMBERLAND RIVER/WILLIAMSBURG/FLOW//30MIN/OBS/"

fid = HecDss.Open(dss_file)
pathArr = [pathname,pathname4, pathname2, pathname3, ]
names = ["data1","data2","data3","data4"]

ts = fid.read_ts(pathname)
values = ts.values
df = pd.DataFrame(ts.pytimes,columns=['Dates'])
i = 0

for path in pathArr:
    ts = fid.read_ts(path)
    df[names[i]] = ts.values
    i += 1


df.plot()
plt.show()

print(df)

# dataSet = {'Dates': ts.pytimes, 'Data': ts.values}
# df = pd.DataFrame(dataSet)
# df.plot(x='Dates', y='Data', kind='line')
# plt.show()

# for info in values:
#     dates.append(str(ts.pytimes[i]))
#     data.append(info)
#     # print(str(ts.pytimes[i]) + "," + str(data))
#     # print(str(ts.pytimes[i]))
#     i += 1


# plt.plot(times[~ts.nodata],values[~ts.nodata],"o")
# plt.show()
# fid.close()
