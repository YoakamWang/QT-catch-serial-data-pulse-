import pandas as pd
import matplotlib.pyplot as plt
import sys
import os

path = sys.argv[1]

firstIndex = 10
steps = 1000  # 14400 - two hours
data = pd.read_csv(path)
inner = data.inner[firstIndex + steps] - data.inner[firstIndex]  # 14400
moto = data.moto[firstIndex + steps] - data.moto[firstIndex]
outer = data.outer[firstIndex + steps] - data.outer[firstIndex]


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
