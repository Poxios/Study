# 결정 트리
import pandas as pd
wine = pd.read_csv('https://bit.ly/wine_csv_data')
wine.head()

wine.info() # 누락된게 있는지 등에 대해 알 수 있다. 만약 누락된게 있다면 평균 등으로 채울 수 있다.
wine.describe() # 대략적인 통계를 볼 수 있다. 평균, 최소, 최대 등.

data = wine[['alcohol', 'sugar', 'pH']].to_numpy()
target = wine['class'].to_numpy()

from sklearn.model_selection import train_test_split
# test_size는 기본적으로 0.25인데 지금 데이터가 충분히 많기에 0.2로 설정.
train_input, test_input, train_target, test_target = train_test_split(data, target, test_size=0.2, random_state=42)

# 시작하기 전에, 각 특성에다가 일정한 비율로 넣기 값을 적용하기 위해 스케일링 한다.
from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
ss.fit(train_input)
train_scaled = ss.transform(train_input)
test_scaled = ss.transform(test_input)

from sklearn.linear_model import LogisticRegression
lr =LogisticRegression()
lr.fit(train_scaled, train_target)
print(lr.score(train_scaled, train_target))
print(lr.score(test_scaled, test_target))

print(lr.coef_, lr.intercept_)
# 이런 식으로 하면 대체 이 모델이 어떤걸 근거해서 결과를 출력하는지 알 수가 없다.
# 결정 트리를 사용하자. DecisionTreeClassifier

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(random_state=42)
dt.fit(train_scaled, train_target)
print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled, test_target))

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(10,7))
plot_tree(dt, max_depth=1, filled=True, feature_names=['alcohol','sugar','pH'])
plt.show()


# gini란 뭘까? criterion 매개변수의 기본값임.
# 지니 불순도 = 1 - (음성 클래스 비율^2 + 양성 클래스 비율^2)
# 이렇게 하면, 두 클래스가 똑같이 섞여있으면 가장 최악의 상황이 나온다.
# 만약 한쪽에 다 쏠려있으면 0으로, 가장 최상의 시나리오인것이다.

# 부모와 자식노드의 불순도 차이를 정보 이득이라고 부른다. 결정트리 알고리즘은 정보이득이 최대가 되도록 데이터를 나눈다.
# 엔트로피 불순도라는 것도 있는데 이건 지니 불순도와 다르게 제곱이 아니고 log2를 씌우는거다.

# 방금은 규제 없이 자라났기에 과대적합이 일어났음. 가지치기 작업을 해야한다.
dt = DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(train_scaled, train_target)
print(dt.score(train_scaled, train_target))
print(dt.score(test_scaled, test_target))

plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol','sugar','pH'])
plt.show()

# 여기서 중요한 사실 하나 !
# 불순도를 기준으로 샘플을 나누는 이 결정 트리 알고리즘은, 어차피 분류할 때 비율만을 가지고 따지기 때문에
# 전처리가 전혀 필요 없다!

dt = DecisionTreeClassifier(max_depth=3,random_state=42)
dt.fit(train_input, train_target)
print(dt.score(train_input, train_target))
print(dt.score(test_input, test_target))

# 이렇게 하면 특성값을 스케일링하지 않았기에 훨씬 보기 편해진다!
plt.figure(figsize=(20,15))
plot_tree(dt, filled=True, feature_names=['alcohol','sugar','pH'])
plt.show()
print(dt.feature_importances_) # 어떤 특성이 가장 중요한지 비율로 나타내준다. sugar이 1위다!

