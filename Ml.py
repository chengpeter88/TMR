import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split    
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, PolynomialFeatures
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer    
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier 
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVR

from sklearn.metrics import r2_score
df = pd.read_csv('Data.csv')
df.isna().sum()

X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values   

# 缺值用 平均數田
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 1:3]) # 缺少的用mean 填寫 實體化
X[:,1:3] = imputer.transform(X[:, 1:3]) # 塞回去原本的缺少

# onehot encoding
#col方入要改的label
ct=ColumnTransformer(transformers=
						[('encoder', OneHotEncoder(), [0])], 
						remainder='passthrough')

X= np.array(ct.fit_transform(X))

# label encoding
le = LabelEncoder()
y = le.fit_transform(y)


# split data    
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 1)

# feature scaling
sc = StandardScaler()
X_train[:, 3:] = sc.fit_transform(X_train[:, 3:])
X_test[:, 3:] = sc.transform(X_test[:, 3:])

# polynomial regression

poly_reg = PolynomialFeatures(degree = 2)
X_poly = poly_reg.fit_transform(X_train)

# model instance
lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
svm_reg = SVR(kernel = 'rbf')
svm_reg.fit(X_train, y_train)
dt = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dt.fit(X_train, y_train)
rf = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)
rf.fit(X_train, y_train)

lin_reg_poly = LinearRegression()

# 使用線性迴歸模型來擬合轉換後的數據
lin_reg_poly.fit(X_poly, y_train)

# 使用線性迴歸模型來預測測試數據

# predict
np.set_printoptions(precision=2)
y_pred_lin = lin_reg.predict(X_test)
y_pred_poly = lin_reg_poly.predict(poly_reg.transform(X_test))   
y_pred_svm = svm_reg.predict(X_test)
y_pred_dt = dt.predict(X_test)
y_pred_rf = rf.predict(X_test)

df_predictions = pd.DataFrame({
    'Actual': y_test,
    'Linear Regression': y_pred_lin,
    'Polynomial Regression': y_pred_poly,
    'SVM': y_pred_svm,
    'Decision Tree': y_pred_dt,
    'Random Forest': y_pred_rf
})

# y_pred = regressor.predict(X_test)
# np.set_printoptions(precision=2)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))


# accuracy
lin_r2=r2_score(y_test, y_pred_lin)
ploy_r2=r2_score(y_test, y_pred_poly)
svm_r2=r2_score(y_test, y_pred_svm)
# not use accuracy_score 比較不好
dt_r2=r2_score(y_test, y_pred_dt)
rf_r2=r2_score(y_test, y_pred_rf)
df_r2 = pd.DataFrame({
    'Model': ['Linear Regression', 'Polynomial Regression', 'SVM', 'Decision Tree', 'Random Forest'],
    'r2': [lin_r2, ploy_r2, svm_r2, dt_r2, rf_r2]
})

# plot








# Path: Ml.py