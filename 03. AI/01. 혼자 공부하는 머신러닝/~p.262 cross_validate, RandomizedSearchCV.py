# 교차 검증과 그리드 서치

# 테스트 세트를 너무 많이 쓰면 테스트 세트에 결과가 맞춰진다! 그러니까 검증 세트가 필요하다.
import pandas as pd
wine = pd.read_csv("https://bit.ly/wine_csv_data")

data = wine[['alcohol','sugar','pH']].to_numpy()
target = wine['class'].to_numpy()

# 일단 원래대로 테스트 세트와 훈련 세트를 나눠준다.
from sklearn.model_selection import train_test_split
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

# 이렇게 하면 검증 세트까지 만들어진다. (val이 검증세트이다.)
sub_input, val_input, sub_target, val_target = train_test_split(train_input, train_target, test_size=0.2, random_state=42)

print(sub_input.shape, val_input.shape)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(sub_input, sub_target)
print(dt.score(sub_input, sub_target))
print(dt.score(val_input, val_target))

# 교차 검증은 검증 세트를 떼어 내어 평가하는 과정을 여러 번 반복하는 것. (k-겹 교차 검증이라고도 부름. 보통 5, 10을 많이 사용.)
# 이 점수를 평균하여 최종 검증 점수를 얻는다.

# 이 때, 원래 test 세트는 사용하지 않는다.
from sklearn.model_selection import cross_validate
scores = cross_validate(dt, train_input, train_target) # 여기서, 회귀 모델인 경우에 KFold 분할기를 사용하고 분류 모델인 경우는 StatifiedKFold를 사용한다.
print(scores)

import numpy as np
print(np.mean(scores['test_score'])) # 이름은 test_score이지만 test가 아닌 val, 즉 검증 세트의 점수이다.

# 여기서 주의해야 할 점은, train_test_split()은 이미 내용물을 섞어주기 때문에 지금은 괜찮지만,
# cross_validate 전에 섞어주기 위해서는 따로 조치를 해야 한다.

# 만약에 10폴드로 하고 섞고 싶으면 이렇게 하면 된다.
from sklearn.model_selection import StratifiedKFold
splitter = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
scores = cross_validate(dt, train_input, train_target, cv=splitter)

# 다음으로 하이퍼파라미터에 대해서 조정해보자. 보통은 매개변수에 들어가는 식으로 되는데,
# 이것을 자동으로 조정해주는 것을 AutoML이라고 말한다.

# 수동으로 하이퍼파라미터를 찾아도 되는데, 사람이 생각하기에는 너무 힘들다.
# 매개변수가 하나면 몰라도, 두 개 이상이면 하나를 고정해두고 다른걸 바꾸는 식으로
# 갈 수가 없다. 상호 영향을 끼치기 때문이다.
# 이때 사용하는게 GridSearchCV이다.

from sklearn.model_selection import GridSearchCV
#params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005]}
params = {'min_impurity_decrease': [0.0001, 0.0002, 0.0003, 0.0004, 0.0005],
          'max_depth': range(5, 20, 1),
          'min_samples_split': range(2, 100, 10)}
gs = GridSearchCV(DecisionTreeClassifier(random_state=42), params, n_jobs=-1) # 이 때 n_jobs는 사용할 CPU 코어 수이다.
gs.fit(train_input, train_target)

dt = gs.best_estimator_
print(dt.score(train_input,train_target))
print(gs.score(train_input,train_target))
print(gs.best_params_) # 이렇게 하면 가장 좋은 params를 얻을 수 있다.
# print(gs.cv_results_['mean_test_score']) # 각 테스트의 결과가 나왔다. 주석 해제하면 출력 엄청 크니까 조심

best_index = np.argmax(gs.cv_results_['mean_test_score'])
# print(gs.cv_results_['params'][best_index]) # 위 best_params_와 동일한 결과를 출력한다
print(np.max(gs.cv_results_['mean_test_score']))

# ---------------------------------------------------------------

# 이렇게 해서 매개변수를 자동으로 탐색 시키는 것까지 공부했다.
# 그런데, 매개변수의 후보들의 간격도 자동으로 탐색할 수 있지 않을까?
# 이게 랜덤 서치이다. 매개변수 값의 목록을 전달하는 것이 아니라 매개변수를 샘플링할 수 있는 확률 분포 객체를 전달합니다.

from scipy.stats import uniform, randint
# 모두 주어진 범위에서 고르게 값을 뽑는 클래스
# randint는 정숫값을 뽑는거고,
# uniform은 실숫값을 뽑는거다.

rgen = randint(0, 10)
rgen.rvs(10)

np.unique(rgen.rvs(1000), return_counts=True) # 개수를 반환해서 어떻게 작동되는지 테스트
ugen = uniform(0,10)
ugen.rvs(10)

params = {'min_impurity_decrease': uniform(0.0001, 0.001),
          'max_depth': randint(20, 50),
          'min_samples_split': randint(2,25),
          'min_samples_leaf': randint(1, 25)
          }

from sklearn.model_selection import RandomizedSearchCV
gs = RandomizedSearchCV(DecisionTreeClassifier(random_state=42), params, n_iter=100, n_jobs=-1, random_state=42)
gs.fit(train_input, train_target)

print(gs.best_params_)

print(np.max(gs.cv_results_['mean_test_score']))
dt = gs.best_estimator_
print(dt.score(test_input, test_target))