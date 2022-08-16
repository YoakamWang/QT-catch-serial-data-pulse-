import os

import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

firstIndex = 10
steps = 18782  # 14400 - two hours
data = pd.read_csv("wavedata_save07221604.csv")
inner = data.inner[firstIndex + steps] - data.inner[firstIndex]  # 14400
moto = data.moto[firstIndex + steps] - data.moto[firstIndex]
outer = data.outer[firstIndex + steps] - data.outer[firstIndex]


def check(db_name, table_name):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    sql = '''SELECT tbl_name FROM sqlite_master WHERE type = 'table' '''
    cursor.execute(sql)
    values = cursor.fetchall()
    tables = []
    for v in values:
        tables.append(v[0])
    if table_name not in tables:
        return False  # 可以建表
    else:
        return True  # 不能建表


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
filename="result1.png"
plt.savefig(filename)
pathurl = os.getcwd() + "/"+filename


def main():
    conn = sqlite3.connect('pictures.db')
    # 创建一个游标 cursor
    cur = conn.cursor()
    # 如果没有表则执行建表的sql语句
    if (check("pictures.db", "pictures") == False):
        sql_text_1 = '''CREATE TABLE pictures
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                    url TEXT);'''
        # 执行sql语句
        cur.execute(sql_text_1)
    sql_text_check = '''SELECT * FROM pictures;'''
    data = cur.execute(sql_text_check)
    if not len(data.fetchall()):
        cur.executemany('INSERT INTO pictures VALUES (?,?)',[(1,pathurl)])
        conn.commit()
    else:
        cur.executemany('UPDATE pictures set URL=(?) where ID=(?)', [(pathurl,1)])
        conn.commit()
    data1 = cur.execute(sql_text_check)
    print(data1.fetchall())

if __name__ == '__main__':
    main()
    # print("done")

# while True:
#     op = int(input("请输入:"))
#     if op == 1:
#         S_name = input("请输入要添加的学生的姓名(如:张三):")
#         S_class = input("请输入要添加的学生的班级(如:一班):")
#         S_xb = input("请输入该学生性别:")
#         S_Chinese = int(input("请输入该学生语文成绩(只输入一个数字,如:82):"))
#         S_Maths = int(input("请输入该学生数学成绩(只输入一个数字,如:95):"))
#         S_English = int(input("请输入该学生英语成绩(只输入一个数字,如:98):"))
#         S_gj = S_Maths+S_Chinese+S_English # 总分
#         data = [(S_name, S_class, S_xb, S_Chinese, S_Maths, S_English,S_gj)]
#         cur.executemany('INSERT INTO scores VALUES (?,?,?,?,?,?,?)', data)
# conn.commit()
# cur.close()
# conn.close()
