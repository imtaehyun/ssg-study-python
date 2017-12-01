# This Python file uses the following encoding: utf-8

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

names1880 = pd.read_csv('Example_3/babynames/yob1880.txt',names=['name','sex','births'])

print(names1880)

## 성별 출생수
print(names1880.groupby('sex').births.sum())

## 하나의 DataFrame으로 취합

years = range(1880, 2011)

pieces = []
columns = ['name', 'sex', 'births']

for year in years:
    path = 'Example_3/babynames/yob%d.txt' % year
    frame = pd.read_csv(path,names=columns)

    frame['year'] = year
    pieces.append(frame)

names = pd.concat(pieces,ignore_index=True)
print(names)

## 연도,성별 데이터 정렬
total_births = names.pivot_table('births', index='year', columns='sex', aggfunc=sum)
print(total_births.tail())

total_births.plot(title='Total births by sex and year')

## 각 이름이 전체 출생수에서 차지하는 비율 계산
def add_prop(group):
  # Integer division floors
  births = group.births.astype(float)
  group['prop'] = births / births.sum()
  return group

names = names.groupby(['year','sex']).apply(add_prop)
print(names)

## prop열이 합이 1이 맞는지 확인
print(np.allclose(names.groupby(['year','sex']).prop.sum(), 1))

## 성별에 따른 빈도수 상위 1000개 추출


def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]


grouped = names.groupby(['year','sex'])
top1000 = grouped.apply(get_top1000)
top1000.index = np.arange(len(top1000))

print(top1000)

## 남여 이름 유행 분석
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table('births', index='year', columns='name', aggfunc=sum)
total_births.info()

subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
subset.plot(subplots=True, figsize=(12, 10), grid=False, title="Number of births per year")

## 다양한 이름 사용경향 파악
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)

table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0,1.2,13), xticks=range(1880, 2020, 10))

## 전체 출생의 50프로가 되는데 필요한 이름의 수
df = boys[boys.year == 1880]
prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()

# print(prop_cumsum[:10])
print(prop_cumsum.values.searchsorted(0.5))

## 성별에 따른 연도별 색인 데이터 만들기


def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q)+1


diversity = top1000.groupby(['year','sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')

# print(diversity.head())

## 이름 마지막 글자의 변화

get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)

subtable = table.reindex(columns=[1910, 1960, 2010], level='year')

print(subtable.head())
letter_prop = subtable / subtable.sum().astype(float)


fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)

## 출생 연도와 성별로 정규화 후 남자 아이 이름의 몇글자를 선택하여 시계화
letter_prop = table / table.sum().astype(float)
dny_ts = letter_prop.ix[['d', 'n', 'y'], 'M'].T

# print(dny_ts.head())
dny_ts.plot()

## 남자이름과 여자이름이 바뀐 경우3

all_names = top1000.name.unique()
mask = np.array(['lesl' in x.lower() for x in all_names])
lesley_like = all_names[mask]
# print(lesley_like)

filtered = top1000[top1000.name.isin(lesley_like)]
filtered.groupby('name').sum()

table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
table = table.div(table.sum(1), axis=0)
print(table.tail())

table.plot(style={'M': 'k-', 'F': 'k--'})
