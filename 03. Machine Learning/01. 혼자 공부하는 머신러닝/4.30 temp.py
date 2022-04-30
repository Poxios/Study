# 기존의 특성을 이용해서 새로운 특성을 뽑아내는 것 = 특성 공학
# 농어의 두께, 길이, 무게등의 모든 특성을 이용하자. 그리고, 특성끼리 곱까지 하여서 더 정확하게 만들자.
import pandas as pd
# csv파일을 바로 데이터프레임으로 바꿔준다.
df = pd.read_csv('https://bit.ly/perch_csv_data')
perch_full = df.to_numpy() # 넘파이 배열로도 바로 바꿀수있다.
print(perch_full)

import numpy as np
perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])

from sklearn.model_selection import train_test_split
# 테스트 세트, 훈련 세트 나누자.
train_input, test_input, train_target, test_target = train_test_split(perch_full, perch_weight, random_state=42)

# PolynomialFeatures에 대해 알아보자
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(include_bias = False) # include_bias 안하면 자동으로 절편을 뜻하는 '1'이 특성에 추가됨.
poly.fit(train_input)
train_poly=poly.transform(train_input) # 기본적으로 각 특성을 제곱한 항을 추가하고 특성끼리 서로 곱한 항을 추가한다.
print(train_poly.shape)
poly.get_feature_names_out() # 각 특성이 어떤 원리로 만들어져 있는지 알 수 있음.
test_poly = poly.transform(test_input)


from sklearn.linear_model import LinearRegression
lr=LinearRegression()
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))

# 만약 특성을 더 많이 추가한다면?
poly = PolynomialFeatures(degree=5, include_bias=False)
poly.fit(train_input)
train_poly=poly.transform(train_input)
test_poly=poly.transform(test_input)
lr.fit(train_poly, train_target)
print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target)) # 과대 적합되어서 형편없는 점수가 나옴.

# 이런 과대적합을 해결하기 위해선 - 정규화
from sklearn.preprocessing import StandardScaler
ss=StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

# 릿지 회귀
from sklearn.linear_model import Ridge
ridge = Ridge()
ridge.fit(train_scaled, train_target)
print(ridge.score(train_scaled,train_target))
# alpha값이 있는데 이건 사람이 조정하는 값이다. 높을 수록 규제가 강해진다.
# 적절한 alpha값을 찾는 방법은 훈련, 테스트 점수가 가장 가까운 지점이 그것이다.
import matplotlib.pyplot as plt
train_score=[]
test_score=[]
alpha_list=[0.001, 0.01, 0.1, 1, 10, 100]
for alpha in alpha_list:
  ridge = Ridge(alpha=alpha)
  ridge.fit(train_scaled,train_target)
  train_score.append(ridge.score(train_scaled, train_target))
  test_score.append(ridge.score(test_scaled,test_target))

plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()

# 임시 - p.162 하는 주