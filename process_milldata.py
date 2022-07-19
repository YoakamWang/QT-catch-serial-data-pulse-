import numpy
import pandas as pd
import datetime
import matplotlib.pyplot as plt

inner = 934452
moto = 279750
outer = 1167410


def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i]+320, y[i], horizontalalignment='center', verticalalignment='center',
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
plt.ylabel("No. of Total Mileage")

plt.title("Outer wheel distance percent: %.4f%%\n" % (outerpercent * 100) + "Inner wheel distance percent: %.4f%%" % (
            innerpercent * 100))

plt.show()
