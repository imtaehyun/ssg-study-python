# This Python file uses the following encoding: utf-8

from collections import Counter

# from matplotlib import pyplot
from pandas import DataFrame, Series

import json
import numpy as np

path = 'example.txt'
records = [json.loads(line) for line in open(path, encoding='UTF8')]
## 파일을 열어 순회하면서 한줄씩 읽어냄

# print("records : " + str(records[0]))

## 1. Counter 객체를 사용하여 최상위 10개 시간대 출력
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
# print(time_zones[:10])

counts = Counter(time_zones)
# print(counts.most_common(10))


## 2. DataFrame으로 최상위 10개 시간대 출력
## pandas의 자료구조는 DataFrame => 스프레드시트 같은 형태
frame = DataFrame(records)
# print(frame['tz'].value_counts()[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts)


## plot메서드로 수평막대그래프 그림
tz_counts[:10].plot(kind='barh',rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])
## 브라우저 종류 파악


results.value_counts()[:8]

## 윈도우 사용자 그룹 나누기
cframe = frame[frame.a.notnull()]

operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')

print(operating_system[:5])

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)

print(agg_counts[:10])

indexer = agg_counts.sum(1).argsort()

print(indexer[:10])

count_subset = agg_counts.take(indexer)[-10:]

count_subset.plot(kind='barh', stacked=True)
normed_subset = count_subset.div(count_subset.sum(1), axis=0)

normed_subset.plot(kind='barh', stacked=True)