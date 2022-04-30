import numpy as np
perch_length = np.array([8.4, 13.7, 15.0, 16.2, 17.4, 18.0, 18.7, 19.0, 19.6, 20.0, 21.0,
       21.0, 21.0, 21.3, 22.0, 22.0, 22.0, 22.0, 22.0, 22.5, 22.5, 22.7,
       23.0, 23.5, 24.0, 24.0, 24.6, 25.0, 25.6, 26.5, 27.3, 27.5, 27.5,
       27.5, 28.0, 28.7, 30.0, 32.8, 34.5, 35.0, 36.5, 36.0, 37.0, 37.0,
       39.0, 39.0, 39.0, 40.0, 40.0, 40.0, 40.0, 42.0, 43.0, 43.0, 43.5,
       44.0])

perch_weight = np.array([5.9, 32.0, 40.0, 51.5, 70.0, 100.0, 78.0, 80.0, 85.0, 85.0, 110.0,
       115.0, 125.0, 130.0, 120.0, 120.0, 130.0, 135.0, 110.0, 130.0,
       150.0, 145.0, 150.0, 170.0, 225.0, 145.0, 188.0, 180.0, 197.0,
       218.0, 300.0, 260.0, 265.0, 250.0, 250.0, 300.0, 320.0, 514.0,
       556.0, 840.0, 685.0, 700.0, 700.0, 690.0, 900.0, 650.0, 820.0,
       850.0, 900.0, 1015.0, 820.0, 1100.0, 1000.0, 1100.0, 1000.0,
       1000.0])


# 테스트 세트, 훈련 세트 나누자.
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)
from sklearn.neighbors import KNeighborsRegressor
knr = KNeighborsRegressor(n_neighbors=3)
knr.fit(train_input, train_target)

print(knr.predict([[50]]))
distances, indexes = knr.kneighbors([[50]])
'''
import matplotlib.pyplot as plt

plt.scatter(train_input, train_target)
plt.scatter(train_input[indexes], train_target[indexes], marker='D')
plt.scatter(50,1033, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
'''

print(np.mean(train_target[indexes]))
# KNeighbor 예측의 한계이다. 가장 가까운 점들의 평균을 내는게 전부이기 때문이다.
# 선형회귀 시작
from sklearn.linear_model import LinearRegression
lr = LinearRegression()

lr.fit(train_input, train_target)
print(lr.predict([[50]]))
print(lr.coef_, lr.intercept_) # y=ax+b에서 가장 적절한 a, b를 찾아냈다.
# coefficient, weight = 계수, 가중치 (기울기와 같은 말.)
# 모델 파라미터 - 머신러닝 알고리즘이 찾은 값임. 모델 기반 학습 = 최적의 모델 파라미터 찾기.
# k-최근접 이웃은 모델 파라미터가 없고, 훈련 세트를 저장하는것이 전부 - 사례기반 학습


# 1차 함수로 나타낸게 이거다.
import matplotlib.pyplot as plt
plt.scatter(train_input, train_target)
plt.plot([15,50], [15*lr.coef_+lr.intercept_, 50*lr.coef_+lr.intercept_])

plt.scatter(50,1241.8, marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 이렇게 점수를 체크해보면, 뭔가 이상하다.
print(lr.score(train_input, train_target))
print(lr.score(test_input, test_target))

# 지금부터 다항회귀를 해야한다
# 그럴려면 데이터셋에 인풋을 제곱한 항이 추가되어야 한다.
train_poly = np.column_stack((train_input**2, train_input))
test_poly = np.column_stack((test_input**2, test_input))
print(train_poly.shape, test_poly.shape)
'''
[x^2,x],
[x^2,x],
[x^2,x],
이렇게 생겨먹었다.
'''
lr=LinearRegression()
lr.fit(train_poly, train_target)
print(lr.predict([[50**2, 50]]))
print(lr.coef_, lr.intercept_) # y=ax^2+bx+c에서 가장 적절한 a, b, c를 찾아냈다.

point = np.arange(15,50)
plt.scatter(train_input, train_target)
plt.plot(point,1.01*point**2-21.6*point+116.05)
plt.scatter(50,1574,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

print(lr.score(train_poly, train_target))
print(lr.score(test_poly, test_target))
