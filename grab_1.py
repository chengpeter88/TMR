def search_word(word, word_list):
    data=[]
    for i in word_list:
        if word in i:
            data.append(i)
    return  data


order = [1,2,3,4,5,6]
order.remove(4) 
order.remove(order)

var_2 =  ['apple','orange','banana']
var_2.pop(0)


var_3 =  ['apple','orange','banana',1,2,3,5]

del var_3[1:3]

list = [1,3,4,7,4,7,1] 
list.index(7)
list.index(7, 4)
result=list.sort()
print(result)

squ = [] 
for i in range(10):
	result = i**2
	squ.append(result)

square = [x **2 for x in range(10) if x % 2 == 0]

com = [] 
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            com.append((x, y))

comp = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
cart = dict(zip(['a', 'b', 'c'], [1, 2, 3]))  
dict = {x: x**2 for x in (2, 4, 6)}  

dic ={1: 'apple', 2: 'orange', 3: 'banana'} 
dic[1]
for idex, value in dic.items():
    print(idex, value)  


cart = {'apple':2, 'orange':3, 'banana':4}
cart['apple']


import pandas as pd
import numpy as np

# 假設我們有一個DataFrame
df = pd.DataFrame({
    'A': np.random.rand(10),
    'B': np.random.rand(10),
    'C': np.random.choice(['apple', 'banana', 'cherry'], 10)
})

# 使用df.info()來獲取DataFrame的信息
print(df.info())

# 使用df.describe()來獲取DataFrame的描述性統計信息
print(df.describe())

# 使用df.head()來獲取DataFrame的前5行
print(df.head())

# 使用df.apply()來對DataFrame的每一列應用一個函數
print(df.apply(np.mean))

# 使用df.groupby()來對DataFrame進行分組
print(df.groupby('C').mean())

# 使用df.sort_values()來對DataFrame進行排序
print(df.sort_values('A'))

# 使用df.sample()來從DataFrame中隨機抽樣
print(df.sample(5))

# 使用pd.read_csv()來讀取一個CSV文件
# df = pd.read_csv('filename.csv')

# 使用df.to_csv()來將DataFrame寫入一個CSV文件
# df.to_csv('filename.csv', index=False)

# 使用df.plot()來繪製DataFrame的圖形
df.plot()

# 使用pd.to_datetime()來將一個列轉換為日期時間格式
# df['date'] = pd.to_datetime(df['date'])

# 使用df.filter()來過濾DataFrame的列
print(df.filter(items=['A', 'B']))

# 使用df.drop()來刪除DataFrame的一列
print(df.drop('C', axis=1))

# 使用df.rank()來獲取DataFrame的排名
print(df.rank())

# 假設我們有另一個DataFrame df2
df2 = pd.DataFrame({
    'A': np.random.rand(5),
    'B': np.random.rand(5),
    'C': np.random.choice(['apple', 'banana', 'cherry'], 5)
})

# 使用df.append()來將df2添加到df的末尾
print(df.append(df2))

# 使用pd.isnull()來檢查DataFrame中的缺失值
print(pd.isnull(df))

# 使用pd.concat()來將df和df2連接起來
print(pd.concat([df, df2]))

# 使用pd.merge()來將df和df2合併起來
# print(pd.merge(df, df2, on='A'))