import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from matplotlib import pyplot as plt
csv = pd.read_csv(r"cian_parsing_result_sale_1_50_moskva_10_Dec_2023_18_25_25_942997.csv", sep=';')
csv['total_meters'] = csv['total_meters'].apply(np.int64)
X = csv.drop('price',axis=1)
y = csv['price']

model = CatBoostRegressor(depth=2, verbose=False, iterations=1).fit(X, y)
 model.plot_tree(
     tree_idx=0,
 )

x_values = csv['total_meters']
y_values = csv['price']
plt.scatter(x_values, y_values)
plt.show

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state = 1)
LR = LinearRegression()
LR.fit(X_train, y_train)

LR.predict(X_test)
result_df = pd.DataFrame(index=X_test.index, columns=['LR','Actual'])
result_df.Actual = y_test
result_df.LR =LR.predict(X_test)
result_df['LR'] = result_df['LR'].apply(np.int64)
result_df

LR.score(X_test, y_test)
