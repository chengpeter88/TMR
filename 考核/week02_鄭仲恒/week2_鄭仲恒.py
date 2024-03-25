# 總分為 115 分
# 及格分數為 80 分

#---------資料清理與機器學習模型訓練----------
# %%
# 問題：請讀取 saledata.csv 的資料，並命名為 dataset
# 5分
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
dataset = pd.read_csv('saledata.csv')   

# %%
# 問題：資料清理基礎
# 10分
'''
1. 請清除 sales 為 NA 的資料
2. 請將 No 欄位去除
'''
dataset=dataset.drop(['No'], axis=1)
dataset = dataset.dropna(subset=['sales'])


# %%
# 問題：請將非 sales 欄位的資料，設定為 X；將 sales 欄位的資料設定為 y
# 請自行判別類別欄位
# 5分
X = dataset.drop(['sales'], axis=1)
y = dataset['sales']
X.info()    

# %%
# 問題：請將 X 欄位中，資料型態為類別的資料進行 One-Hot encoding，將其轉換成數值形態
# 5分
# 針對cbwd欄位進行onehot encoding
# 年份之類也有可能是dummy呈現 不確定想法有沒有想同
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
ct=ColumnTransformer(transformers=
                        [('encoder', OneHotEncoder(), [7])], 
                        remainder='passthrough')

X= np.array(ct.fit_transform(X))    


# %%
# 問題：切分訓練與測試資料集，其中測試資料集的佔比為 30%、random_state 為 100
# 10分
from sklearn.model_selection import train_test_split    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)


# %%
# 問題：請分別使用下述模型來建模
# 15分
'''
1. 多重線性迴歸
2. 隨機森林
3. 決策樹
來執行預測任務

注意：
1. Regressor模型命名要有所不同，後續題目會使用到；舉例：決策樹的名稱可能為 dt_regressor
2. 請不要調整模型參數，保持模型原本的預設參數即可
'''
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
dt_regressor = DecisionTreeRegressor()
dt_regressor.fit(X_train, y_train)
rf_regressor = RandomForestRegressor()
rf_regressor.fit(X_train, y_train)


# %%
# 問題：請使用上述三種模型來預測測試資料集的成果，並將成果存到新變數
# 舉例：隨機森林預測出來的數值可請存到自創變數 rf_pred
# 10分
lin_pred = lin_reg.predict(X_test)
dt_pred = dt_regressor.predict(X_test)
rf_pred = rf_regressor.predict(X_test)


# %%
# 問題：請使用 RMSE 與 MAPE 來評估預測值與真實值之間的差距，並將成效評估後的成果存到新變數
# 舉例：隨機森林預測評測出來的數值可請存到自創變數 rf_rmse
# 25分
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_percentage_error
import math
lin_rmse = math.sqrt(mean_squared_error(y_test, lin_pred))
lin_mape = mean_absolute_percentage_error(y_test, lin_pred)
dt_rmse = math.sqrt(mean_squared_error(y_test, dt_pred))
dt_mape = mean_absolute_percentage_error(y_test, dt_pred)
rf_rmse = math.sqrt(mean_squared_error(y_test, rf_pred))
rf_mape = mean_absolute_percentage_error(y_test, rf_pred)
print(f'rmse數值:{lin_rmse,dt_rmse,rf_rmse}')
print(f'mape數值：{lin_mape,dt_mape,rf_mape}')

# %%
# 問題：將成效評估後的成果形塑如附檔範例「eval範例.png」的模樣，請存成「模型比較.csv」
# 10分 
df = pd.DataFrame({'Model': ['Linear Regression', 'Decision Tree', 'Random Forest'],
                   'RMSE': [lin_rmse, dt_rmse, rf_rmse],
                   'MAPE': [lin_mape, dt_mape, rf_mape]})
df.to_csv('模型比較.csv', index=False)



# %%
# 問題：請使用 plotly，將「模型比較」的 DataFrame 繪製如「繪圖範例.png」的 html 檔案
# 10分
# mape and rmse 的結果分開畫，沒想到怎麼合併
import plotly.express as px

#fig1 = px.bar(df, x='Model', y='RMSE', barmode='group')
#fig1.write_html('模型比較_RMSE.html')

#fig2 = px.bar(df, x='Model', y='MAPE', barmode='group')
#fig2.write_html('模型比較_MAPE.html')

import plotly.graph_objects as go


fig = go.Figure(data=[
    go.Bar(name='RMSE', x=df['Model'], y=df['RMSE'], marker_color='blue'),
])


fig.add_trace(
    go.Bar(name='MAPE', x=df['Model'], y=df['MAPE'], marker_color='orange')
)


fig.update_layout(
    title='模型性能比較',
    barmode='group', 
    xaxis_title='模型',
    yaxis_title='值',
    legend_title='指標'
)

# 输出为 HTML 文件
fig.write_html('RMSE_MAPE.html')



# %%
# 問題：請問，依照您的觀察，哪一個模型表現最好？為什麼？
# 10分
#根據RMSE和MAPE值，我們可以看到隨機森林（Random Forest）方法在這個案例中表現最好，
#因為它具有最低的RMSE和MAPE值

##線性回歸（Linear Regression）：
#RMSE：78.76
#MAPE：7370536878374.31

#決策樹（Decision Tree）：
#RMSE：53.37
#MAPE：1078448186631.36

#隨機森林（Random Forest）：
#RMSE：36.59
#MAPE：1689568825722.15