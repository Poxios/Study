bream_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0]
bream_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0]

smelt_length = [9.8, 10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
smelt_weight = [6.7, 7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 위 값들은 책 링크에서 복붙해옴.

length = bream_length + smelt_length
weight = bream_weight + smelt_weight

fish_data = [[l,w] for l, w in zip(length, weight)]
fish_target = [1] * 35 + [0] * 14 # 물고기 종류 수 만큼 리스트 생성해줌.

from sklearn.neighbors import KNeighborsClassifier
kn = KNeighborsClassifier()
kn.fit(fish_data, fish_target)
kn.score(fish_data, fish_target)
kn.predict([[30, 600]])

train_input = fish_data[:35]
train_target = fish_target[:35]
test_input = fish_data[35:]
test_target = fish_target[35:]

kn = kn.fit(train_input, train_target)
kn.score(test_input, test_target)

# 샘플링 편향이라는걸 알아야한다.
# 저렇게 개수로 자르면 빙어만 앞에 들어간다.

import numpy as np
input_arr = np.array(fish_data)
target_arr = np.array(fish_target)

# print(input_arr.shape) # 샘플 수, 특성 수를 출력한다.

np.random.seed(42)
index = np.arange(49) # 0부터 48까지 1씩 증가하는 인덱스를 만들 수 있음.
np.random.shuffle(index) # 예를 들어 상자 안에 들어있던 공들을 랜덤하게 배치하는거임.

# print(input_arr[[1,3]])

# 랜덤하게 배치했던 공을 다시 뽑아서 그 index에 해당하는 값을 뽑는다.
train_input = input_arr[index[:35]]
train_target = target_arr[index[:35]]

# 랜덤하게 배치했던 공을 다시 뽑아서 그 index에 해당하는 값을 뽑는다.
test_input = input_arr[index[35:]]
test_target = target_arr[index[35:]]



fish_length = [25.4, 26.3, 26.5, 29.0, 29.0, 29.7, 29.7, 30.0, 30.0, 30.7, 31.0, 31.0, 
                31.5, 32.0, 32.0, 32.0, 33.0, 33.0, 33.5, 33.5, 34.0, 34.0, 34.5, 35.0, 
                35.0, 35.0, 35.0, 36.0, 36.0, 37.0, 38.5, 38.5, 39.5, 41.0, 41.0, 9.8, 
                10.5, 10.6, 11.0, 11.2, 11.3, 11.8, 11.8, 12.0, 12.2, 12.4, 13.0, 14.3, 15.0]
fish_weight = [242.0, 290.0, 340.0, 363.0, 430.0, 450.0, 500.0, 390.0, 450.0, 500.0, 475.0, 500.0, 
                500.0, 340.0, 600.0, 600.0, 700.0, 700.0, 610.0, 650.0, 575.0, 685.0, 620.0, 680.0, 
                700.0, 725.0, 720.0, 714.0, 850.0, 1000.0, 920.0, 955.0, 925.0, 975.0, 950.0, 6.7, 
                7.5, 7.0, 9.7, 9.8, 8.7, 10.0, 9.9, 9.8, 12.2, 13.4, 12.2, 19.7, 19.9]

# 이렇게 하면 세로 탑 두개가 쭉 쌓아진다. 즉, 마치 지퍼처럼 쭉 쌓아진다.
fish_data = np.column_stack((fish_length, fish_weight))

fish_target = np.concatenate((np.ones(35), np.zeros(14)))

from sklearn.model_selection import train_test_split

train_input, test_input, train_target, test_target = train_test_split(fish_data, fish_target, random_state=42)

kn=KNeighborsClassifier()
kn.fit(train_input, train_target)
kn.score(test_input, test_target)
kn.predict([[25,150]]) # 도미로 예측해야 하지만 그렇지 않다.

import matplotlib.pyplot as plt
'''
# 실제 그림에 찍어보면 도미에 가까운데 왜 빙어에 가깝다고 판단한지 의문을 가진다.
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25,150,marker='^')
plt.xlabel('length')
plt.ylabel('weight')
plt.show()
'''


'''
distances, indexes = kn.kneighbors([[25,150]]) # 이렇게 하면 저 점 기준 인식한 가장 가까운 점들을 찾는다.
plt.scatter(train_input[:,0], train_input[:,1])
plt.scatter(25,150,marker='^')
plt.scatter(train_input[indexes,0],train_input[indexes,1], marker='D')
plt.xlim((0,1000)) # 강제로 x축이 보이는 범위를 지정한다.
plt.xlabel('length')
plt.ylabel('weight')
'''

# 이걸 해결하기 위해서 표준점수를 사용한다.
# 표준점수 == 각 특성값이 평균에서 표준편차의 몇 배만큼 떨어져 있는지를 나타낸다.
mean = np.mean(train_input, axis=0) # axis=0으로 하면 행을 따라 각 열의 통계 값을 계산한다. (이렇게 해야 열의 평균이 나온다.)
std = np.std(train_input, axis=0)

train_scaled = (train_input - mean) / std # 이렇게 하면 브로드캐스팅이 된다.
# 브로드캐스팅이란, 넘파이 배열에서 단순 연산을 모든 원소 대상으로 해주는 작업이다.

plt.scatter(train_scaled[:,0], train_scaled[:,1])
plt.scatter(*(([25,150]-mean)/std),marker="^") # 여기서 25,150도 변환해줘야 
plt.xlabel('length')
plt.ylabel('weight')
plt.show()

kn.fit(train_scaled, train_target)

