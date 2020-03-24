import pandas as pd
import os

# program 1

data = {
    'apples': [300, 240, 100, 140],
    'oranges': [125, 380, 750, 460],
    'Grapes': [580,350,900,630],
    'Banana' : [750,800,300,540]
}
sales = pd.DataFrame(data)
print(sales)
sales = pd.DataFrame(data, index=['KL', 'KR', 'TN', 'WB'])
print(sales)
print(sales.loc['TN'])
print(type(data))


#program 2
def Convert(toConvert):
    finalDict = { toConvert[i]: toConvert[i + 1] for i in range(0,len(toConvert), 3)}
    return finalDict

mylist1 = ['apples',3000,240,100,146,123]
print(mylist1)
print(Convert(mylist1))

# creating a list 
list12=["ram",79977,"venky",87758,"svr",84759,"rocky",83639]
def dic(li_st):
    convertedlist= {li_st[i]:li_st[i+1] for i in range(0,len(list12),2)}
    return convertedlist

print(dic(list12))

print(os.listdir())
print("current dir")
print(os.getcwd())
path='/Users/ADMIN/Desktop/ram'
os.chdir(path)
print(os.getcwd())
print(os.listdir())



# """
# output


#    apples  oranges  Grapes  Banana
# 0     300      125     580     750
# 1     240      380     350     800
# 2     100      750     900     300
# 3     140      460     630     540
#     apples  oranges  Grapes  Banana
# KL     300      125     580     750
# KR     240      380     350     800
# TN     100      750     900     300
# WB     140      460     630     540
# apples     100
# oranges    750
# Grapes     900
# Banana     300
# Name: TN, dtype: int64
# <class 'dict'>
# ['apples', 3000, 240, 100, 146, 123]
# {'apples': 3000, 100: 146}
# {'ram': 79977, 'venky': 87758, 'svr': 84759, 'rocky': 83639}
# ['.anaconda', '.conda', '.condarc', '.ipynb_checkpoints', '.ipython', '.jupyter', '.matplotlib', '.PyCharmCE2019.3', '.pylint.d', '.vscode', '3D Objects', 'AppData', 'Application Data', 'Contacts', 'Cookies', 'data.xlsx', 'Desktop', 'Documents', 'Downloads', 'Favorites', 'IntelGraphicsProfiles', 'Links', 'Local Settings', 'MicrosoftEdgeBackups', 'Music', 'My Documents', 'my_workbook.xlsx', 'NetHood', 'NTUSER.DAT', 'ntuser.dat.LOG1', 'ntuser.dat.LOG2', 'NTUSER.DAT{5188d876-fac3-11e9-ad01-c0b5d77bd21e}.TM.blf', 'NTUSER.DAT{5188d876-fac3-11e9-ad01-c0b5d77bd21e}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{5188d876-fac3-11e9-ad01-c0b5d77bd21e}.TMContainer00000000000000000002.regtrans-ms', 'NTUSER.DAT{848de40f-b6c8-11e9-acf1-0021706aa471}.TM.blf', 'NTUSER.DAT{848de40f-b6c8-11e9-acf1-0021706aa471}.TMContainer00000000000000000001.regtrans-ms', 'NTUSER.DAT{848de40f-b6c8-11e9-acf1-0021706aa471}.TMContainer00000000000000000002.regtrans-ms', 'ntuser.ini', 'OneDrive', 'Pictures', 'PrintHood', 'PycharmProjects', 'Recent', 'Saved Games', 'Searches', 'SendTo', 'Start Menu', 'Templates', 'Untitled.ipynb', 'Videos']
# current dir
# C:\Users\ADMIN
# C:\Users\ADMIN\Desktop\ram
# ['ex1.py', 'ex2.py', 'ex3.py', 'ex4.py', 'ex5.py', 'ex6.py', 'ex7.py', 'ex8.py', 'week5ex.py']
# """