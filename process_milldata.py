import pandas as pd
import matplotlib.pyplot as plt
import sys
import os
from datetime import datetime
import time

path = sys.argv[1]
# if not sys.argv[2]:
#     duration=float(sys.argv[2])
try:
    float(sys.argv[2])
except Exception:
    duration = 2
else:
    duration = float(sys.argv[2])

firstIndex = 2
# steps = 18500  # 14400 - two hours
# data = pd.read_csv(path)
with open(path) as f:
    data = pd.read_csv(f)
    time_start1 = datetime.strptime(data.date[firstIndex], "%Y.%m.%d %H:%M:%S")
    # Use time.mktime to convert datetime to timestamp    "2022.07.22 13:19:25"
    timestamp_start1 = time.mktime(time_start1.timetuple())
    timestamp_end1 = timestamp_start1 + duration * 3600
    datetime_end1 = datetime.fromtimestamp(timestamp_end1).strftime("%Y.%m.%d %H:%M:%S")
    steps = 0
    # arr = data.date
    # searchValue = datetime_end1
    # index1 = arr.index(searchValue)
    while steps < len(data['date']):
        if data.date[steps] == datetime_end1:
            # print(index)
            break
        steps += 1

try:
    inner = data.inner[firstIndex + steps] - data.inner[firstIndex]  # 14400
    moto = data.moto[firstIndex + steps] - data.moto[firstIndex]
    # inner7 = data.inner7[firstIndex + steps] - data.inner7[firstIndex]
    outer = data.outer[firstIndex + steps] - data.outer[firstIndex]
except Exception:
    inner = data.inner[len(data.inner) - 2] - data.inner[firstIndex]
    # inner7 = data.inner7[len(data.inner)-1] - data.inner7[firstIndex]
    moto = data.moto[len(data.inner) - 2] - data.moto[firstIndex]
    outer = data.outer[len(data.inner) - 2] - data.outer[firstIndex]


# inner = 258870-14385
# moto = 77817-4369
# outer = 349397-19618


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], horizontalalignment='center', verticalalignment='center',
                 bbox=dict(facecolor='orange', alpha=0.4))


innerdis = inner / 13 * 0.038 * 3.1415
outerdis = outer / 13 * 0.038 * 3.1415
motodis = moto / 15 * 0.197 * 3.1415
innerwheel = moto / 15 * 0.1499 * 3.1415

innerpercent = (innerdis - innerwheel) / innerwheel
if (innerpercent < 0):
    innerpercent = -innerpercent
outerpercent = (outerdis - motodis) / motodis
if (outerpercent < 0):
    outerpercent = -outerpercent

data = {"Inner": innerdis, "innerwheel": innerwheel, "Outer": outerdis, "outerwheel": motodis}
items = list(data.keys())
dis = list(data.values())

fig = plt.figure(figsize=(10, 7))

# fig= plt.figure((7,7))
# creating the bar plot
# colors=['#E0FF5A','#FFEB00',"orange"]
plt.bar(items, dis, color='b', width=0.2)
addlabels(items, dis)
plt.xlabel("Total Mileage")
plt.ylabel("No. of Total Mileage  m")

plt.title("Outer encoder/Outer wheel distance percent: %.4f%%\n" % (
        outerpercent * 100) + "Inner encoder/Inner wheel distance percent: %.4f%%" % (
                  innerpercent * 100))

# plt.show()
filename = "result1.png"
plt.savefig(filename)
pathurl = os.getcwd() + "/" + filename
print(pathurl)
