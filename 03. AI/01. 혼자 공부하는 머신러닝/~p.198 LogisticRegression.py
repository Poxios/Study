# 로지스틱 회귀
# 무게와 길이가 주어졌을때 주변에 있는 객체의 구성을 확률로 나타내는?
import pandas as pd
fish=pd.read_csv('https://bit.ly/fish_csv_data')
fish.head() # 이렇게하면 맨 앞 5개만 출력된다.

# 이렇게하면 JS Set처럼 중복을 없애고 나머지를 반환함.
print(pd.unique(fish['Species']))

fish_input = fish[['Weight', 'Length','Diagonal','Height','Width']].to_numpy()

print(fish_input[:5])
fish_target = fish['Species'].to_numpy()

from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(fish_input, fish_target, random_state=42)

# 시작하기 전에, 각 특성에다가 일정한 비율로 넣기 값을 적용하기 위해 스케일링 한다.
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.neighbors import KNeighborsClassifier
kn=KNeighborsClassifier(n_neighbors=3)
kn.fit(train_scaled, train_target)

# 점수는 그냥 잊어보자. 지금은 확률에 집중하자.
print(kn.score(train_scaled, train_target))
print(kn.score(test_scaled, test_target))

# 위에 타겟 이름들 순서랑 달라진다.
print(kn.classes_) # 이렇게 해야 순서가 그대로 나온다.

print(kn.predict(test_scaled[:5]))

# 위 순서는 어떤 확률로 만들어졌는가? - predict_proba()를 이용하면 된다.
import numpy as np
proba = kn.predict_proba(test_scaled[:5])
# print(np.round(proba, decimals=4)) #참고로 순서는 위에 classes_에 있던 순서랑 같다.

distances, indexes = kn.kneighbors(test_scaled[3:4])
print(train_target[indexes])
# 이렇게 하면 3개의 이웃 중에서 어떤게 선택되는지, 즉, 확률이 어떻게 되는지를 알 수 있다.

# 로지스틱 회귀란, 이름은 회귀이지만 분류 모델이다.
# z=a(Weight) + b(Length) + c(Diagonal) + d(Height) + e(Width) + f
# 이렇게하면 z가 무조건 0~1 사이에 들어오게 할 수가 없다.
# 이때 사용되는 것이 시그모이드 함수 or 로지스틱 함수이다.
# sig = 1/(1+e^(-z))

# 넘파이로 시그모이드 함수를 직접 그려보자
import matplotlib.pyplot as plt
z = np.arange(-5,5,0.1)
phi= 1/(1+np.exp(-z))
plt.plot(z,phi)
plt.xlabel('z')
plt.ylabel('phi')
plt.show()

# 정확히 0.5일때는 라이브러리마다 다르긴한데 사이킷런은 0.5이면 음성임.
# 이렇게하면 넘파이에서 자동으로 Boolean Indexing을 통해 변환해준다.
bream_smelt_indexes = (train_target == "Bream") | (train_target == "Smelt")
train_bream_smelt = train_scaled[bream_smelt_indexes]
target_bream_smelt = train_target[bream_smelt_indexes]
# 위 과정을 통해 여러가지 조건에 부합하는 원소들을 뽑아낼수있다!! JS의 map이랑 뭐가 다른거지?

# 로지스틱 회귀는 회귀지만 분류를 한다.
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()
lr.fit(train_bream_smelt, target_bream_smelt)
print(lr.predict(train_bream_smelt[:5]))
print(lr.predict_proba(train_bream_smelt[:5]))

print(lr.classes_)
print(lr.coef_, lr.intercept_)

# 아래의 함수는 로지스틱 회귀 모델의 방정식을 적용해볼 수 있는 함수이다.
decisions = lr.decision_function(train_bream_smelt[:5])
print(decisions)

# 시그모이드 함수로 확률을 얻어내는 과정
from scipy.special import expit
print(expit(decisions)) # 해보면 알겠지만 predict_proba의 두번째 열과 같다.

lr = LogisticRegression(C=20, max_iter=1000)
lr.fit(train_scaled, train_target)
print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))

# 로지스틱 회귀를 이용한 모델이다.
print(lr.predict(test_scaled[:5]))

proba = lr.predict_proba(test_scaled[:5])
print(np.round(proba, decimals=3))
print(lr.classes_) # 이렇게 어떤 클래스인지 확인가능.

print(lr.coef_.shape, lr.intercept_.shape)

# 소프트맥스 함수란, 시그모이드 함수랑 다르게 출력값을 0~1 사이로 압축하고 그 합이 1이 되게 만든다.
# e_sum = e^z1 + e^z2 + e^z3 하고 우항에 좌항을 나눠주면 된다.

# 만약 수동으로 시그모이드 함수를 소프트맥스 함수로 바꿔준다면?
decision = lr.decision_function(test_scaled[:5])
print(np.round(decision, decimals=2))

from scipy.special import softmax
proba = softmax(decision, axis=1)
print(np.round(proba, decimals=3))
