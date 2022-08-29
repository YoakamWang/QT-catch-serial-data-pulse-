import pandas as pd
import matplotlib.pyplot as plt

firstIndex =2
steps=10000000 #14400 - two hours
data1 = pd.read_csv("wavedata_save08150917.csv")
#inner=0
try:
	inner1 = data1.inner[firstIndex + steps] - data1.inner[firstIndex]  # 14400
	moto1 = data1.moto[firstIndex + steps] - data1.moto[firstIndex]
	outer1 = data1.outer[firstIndex + steps] - data1.outer[firstIndex]
except Exception:
	inner1 = data1.inner[len(data1.inner)-1] - data1.inner[firstIndex]  # 14400
	moto1 = data1.moto[len(data1.inner)-1] - data1.moto[firstIndex]
	outer1 = data1.outer[len(data1.inner)-1] - data1.outer[firstIndex]
#print(data.inner[firstIndex])
data2 = pd.read_csv("wavedata_save08231630.csv")
#inner=0
try:
	inner2 = data2.inner[firstIndex + steps] - data2.inner[firstIndex]  # 14400
	moto2 = data2.moto[firstIndex + steps] - data2.moto[firstIndex]
	outer2 = data2.outer[firstIndex + steps] - data2.outer[firstIndex]
except Exception:
	inner2 = data2.inner[len(data2.inner)-1] - data2.inner[firstIndex]  # 14400
	moto2 = data2.moto[len(data2.inner)-1] - data2.moto[firstIndex]
	outer2 = data2.outer[len(data2.inner)-1] - data2.outer[firstIndex]

data3 = pd.read_csv("wavedata_save0829.csv")
#inner=0
try:
	inner3 = data3.inner[firstIndex + steps] - data3.inner[firstIndex]  # 14400
	moto3 = data3.moto[firstIndex + steps] - data3.moto[firstIndex]
	outer3 = data3.outer[firstIndex + steps] - data3.outer[firstIndex]
except Exception:
	inner3 = data3.inner[len(data3.inner)-1] - data3.inner[firstIndex]  # 14400
	moto3 = data3.moto[len(data3.inner)-1] - data3.moto[firstIndex]
	outer3 = data3.outer[len(data3.inner)-1] - data3.outer[firstIndex]
inner=inner1+inner2+inner3
moto=moto1+moto2+moto3
outer=outer1+outer2+outer3
#print(data.inner[firstIndex])
#print(data.inner[firstIndex])
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

dataItem = {"Inner": innerdis, "innerwheel": innerwheel, "Outer": outerdis, "outerwheel": motodis}
items = list(dataItem.keys())
dis = list(dataItem.values())

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

plt.show()

