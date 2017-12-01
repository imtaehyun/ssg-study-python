# This Python file uses the following encoding: utf-8

import pandas as pd
import os



encoding = 'latin1'

upath = os.path.expanduser('Example_2/users.dat')
rpath = os.path.expanduser('Example_2/ratings.dat')
mpath = os.path.expanduser('Example_2/movies.dat')

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
mnames = ['movie_id', 'title', 'genres']

users = pd.read_csv(upath, sep='::', header=None, names=unames, encoding=encoding)
ratings = pd.read_csv(rpath, sep='::', header=None, names=rnames, encoding=encoding)
movies = pd.read_csv(mpath, sep='::', header=None, names=mnames, encoding=encoding)

# print(users[:5])

## 모든 데이터를 하나로 병합, 병합하는 테이블의 중복되는 열의 이름을 키로 사용
data = pd.merge(pd.merge(ratings, users), movies)
print(data)

## 성별에 따른 각 영화의 평균 평점을 구함
mean_ratings = data.pivot_table('rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:5])

## 250건 이상의 평점 정보가 들어있는 영화만 추림
ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10])
active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles)

## 색인 정보 추출
mean_ratings = mean_ratings.ix[active_titles]
print(mean_ratings)

## 여성에게 높은 평점을 받은 영화 목록을 확인
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
print(top_female_ratings)

## 남녀 평균평점 차이
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:15])
## 남성들이 선호하는 영화
print(sorted_by_diff[::-1][:15])

## 호불호가 극명한 영화
##표준편차
rating_std_by_title = data.groupby('title')['rating'].std()
##active_titles만 선택
rating_std_by_title = rating_std_by_title.ix[active_titles]
##내림차순 정렬
(rating_std_by_title.sort_values(ascending=False)[:10]).plot(kind='barh', rot=0)


