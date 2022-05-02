# 확률적 경사 하강법
# 데이터가 계속 많이진다면, 이전 데이터를 버리지 않고 계속 학습시킬 수 있는 방법이 있을까?
# 이게 점진적 학습이다. - 대표적인 알고리즘은 확률적 경사 하강법이 있다.

# 에포크 - 확률적 경사 하강법에서 훈련 세트를 한 번 모두 사용하는 과정
# 미니배치 경사 하강법 - 여러 개의 샘플을 사용해 경사 하강법을 수행하는 방식
# 배치 경사 하강법 - 극단적으로 전체 샘플을 한번에 이용하는 것

# 어떤 산을 내려가야 하는가? - 손실함수이다.
# 손실함수 - 어떤 문제에서 머신러닝 알고리즘이 얼마나 엉터리인지 측정하는 기준.
# 하지만 어떤 값이 최소인지는 모르기에, 적당히 해보고 빼야한다.
# 비용함수는 원래는 손실함수랑 다른 말이지만 섞어서 쓴다. 손실함수의 모든 합이 비용함수이다.

# 분류에서 손실이란, 정답을 못맞추는거다.
# 그런데 이때 정확도를 손실함수로 사용하면, 가능한 상황이 매우 적다. 즉, 연속적이지 않고, 미분 가능하지 않기 때문에, 안된다.
# 산의 경사면은 연속적이어야 한다!

# 로지스틱 손실 함수를 만들어보자
# 0.9, 0.3 0.2 0.8 의 예측 확률이 있다고 했을 때, 0.9 x 1 = 0.9 에다가 음수를 씌우면 -0.9이므로, 양성 클래스가 1이라고
# 한다면 충분히 쓸만한 손실함수이다.

# 그런데 이때 타깃이 음성 클래스라면, 0.2 x 0이 되어야 하는데 이러면 무조건 0이 되기 때문에,
# 생각을 바꿔서 양성 클래스를 맞춘다고 생각해보자. 이러면 0.2가 아닌 0.8이 되는거다.
# 이걸 로지스틱 손실 함수, 또는 이진 크로스엔트로피 손실 함수라고 부른다.

# 다중 분류인 경우에는 크로스엔트로피 손실 함수를 사용한다.

# 그럼 회귀에서는? 평균 절댓값 오차를 이용할 수 있는데, 평균 제곱 오차를 더 많이 쓴다.

import pandas as pd
fish = pd.read_csv('https://bit.ly/fish_csv_data')

fish_input = fish[['Weight','Length','Diagonal','Height','Width']].to_numpy()
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

# 시작하기 전에, 각 특성에다가 일정한 비율로 넣기 값을 적용하기 위해 스케일링 한다.
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import SGDClassifier
sc=SGDClassifier(loss='log', max_iter=10, random_state=42)
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

sc.partial_fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

# 여기도 똑같이 너무 큰 에포크를 설정하면 과대적합 되어버린다.
import numpy as np
sc=SGDClassifier(loss='log', max_iter=10, random_state=42)
train_score=[]
test_score=[]
classes=np.unique(train_target)

for _ in range(0, 300):
  # fit 없이 partial_fit만 사용하려면 
  sc.partial_fit(train_scaled, train_target, classes=classes)
  train_score.append(sc.score(train_scaled, train_target))
  test_score.append(sc.score(test_scaled, test_target))

import matplotlib.pyplot as plt
plt.plot(train_score)
plt.plot(test_score)
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.show()

# tol을 None으로 지정하지 않으면 자체적으로 판단해서 멈춰버린다.
# loss를 'hinge'로 넣을 수도 있는데, 이건 서포트 벡터 머신일때 쓰는거다.
sc=SGDClassifier(loss='log', max_iter=100,tol=None, random_state=42)
sc.fit(train_scaled, train_target)
print(sc.score(train_scaled, train_target))
print(sc.score(test_scaled, test_target))

# SGDRegressor은 위 원리를 이용한 회귀모델이다. 그냥 참고.
