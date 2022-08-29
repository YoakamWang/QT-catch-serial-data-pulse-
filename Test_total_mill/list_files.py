import os
import matplotlib.pyplot as plt
import pandas as pd

dir_list = os.listdir('.')
# print(dir_list)
files = []
firstIndex = 2
steps = 10000000
for (root, dirs, file) in os.walk(os.getcwd()):
    for f in file:
        if '.csv' in f:
            # print(root)
            # real_path=root+'/'+f
            # print(real_path)
            files.append(os.path.abspath(f))


def get_data(file):
    with open(file) as fd:
        data = pd.read_csv(fd)
    # print(data)
    try:
        inner = data.inner[firstIndex + steps] - data.inner[firstIndex]  # 14400
        moto = data.moto[firstIndex + steps] - data.moto[firstIndex]
        outer = data.outer[firstIndex + steps] - data.outer[firstIndex]
    except Exception:
        # print(data)
        inner = data.inner[len(data.inner) - 2] - data.inner[firstIndex]  # 14400
        moto = data.moto[len(data.inner) - 2] - data.moto[firstIndex]
        outer = data.outer[len(data.inner) - 2] - data.outer[firstIndex]
    # print(inner)
    return inner, moto, outer


inner_total = 0
moto_total = 0
outer_total = 0

for file in files:
    # print(file)
    c_inner, c_moto, c_outer = get_data(file)
    inner_total += c_inner
    moto_total += c_moto
    outer_total += c_outer


# print(inner_total)

def addlabels(x, y):
    for i in range(len(x)):
        plt.text(i, y[i], y[i], horizontalalignment='center', verticalalignment='center',
                 bbox=dict(facecolor='orange', alpha=0.4))



innerdis = inner_total / 13 * 0.038 * 3.1415
outerdis = outer_total / 13 * 0.038 * 3.1415
motodis = moto_total / 15 * 0.197 * 3.1415
innerwheel = moto_total / 15 * 0.1499 * 3.1415

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
