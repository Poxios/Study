# 회귀를 공부한다
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

# 길이 -> 특성 / 무게 -> 타겟

import matplotlib.pyplot as plt
plt.scatter(perch_length, perch_weight)
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

# 테스트 세트, 훈련 세트 나누자.
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(perch_length, perch_weight, random_state=42)

# 1차원 배열을 2차원 배열로 바꿔야 한다. 배열은 모든 차원의 개수가 같아야 한다.
# print(np.shape(np.array([[1,2],[1,2],[1,2]]))) 여기서 하나가 1,2가 아니고 1이면 안된다.

# -1은 unknown dimension으로 나머지 차원들을 모두 채우고 남은 애들을 넣어준다.
train_input = train_input.reshape(-1,1)
test_input = test_input.reshape(-1,1)
print(train_input.shape, test_input.shape)

# 결정계수 R^2
from sklearn.neighbors import KNeighborsRegressor
knr = KNeighborsRegressor()

# k-최근접 이웃 회귀 모델을 훈련
knr.fit(train_input, train_target)

print(knr.score(test_input, test_target)) # 이 경우는 정확한 숫자를 맞추는건 불가하기에 결정계수로 평가.

# R^2 = 1 - ((타깃 - 예측)^2의 합)/((타깃 - 타깃평균)^2의 합)
# 이렇게 하면 만약 예측이 평균 정도를 맞추는 수준이라면 점수가 낮음.

from sklearn.metrics import mean_absolute_error
# 얼마나 예측이 벗어났는지 확인하기 위해 다른 방법 사용

# 테스트 세트에 대한 예측을 만듦
test_prediction = knr.predict(test_input)

# 테스트 세트에 대한 평균 절댓값 오차를 계산
mae = mean_absolute_error(test_target, test_prediction)
print(mae)

# 만약 훈련시킨 값으로 점수를 낸다면?
print(knr.score(train_input, train_target))

# 이러면 훈련 세트를 이용한 점수가 더 낮은, 과소적합이 일어난다. 데이터 세트의 크기가 너무 작기 때문이다.

# 모델을 좀 더 복잡하게, 즉 k-이웃을 줄이면 된다. k의 수가 내려가면 국지적인 패턴에 민감해지고, 올라가면 전체적인 패턴을 따른다.
knr.n_neighbors = 3
knr.fit(train_input, train_target)
print(knr.score(train_input, train_target))
# 이렇게하면 과소적합이 해결되었고, 두 점수의 차이도 그리 크지 않으므로 과대적합되지도 않았다.

