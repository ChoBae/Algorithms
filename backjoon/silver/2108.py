# 통계학 실버3
from collections import Counter
import sys
input = sys.stdin.readline
n = int(input())
numLi = []
tmpLi = []
count = 0 
# 솔루션 -> 딕셔너리로 빈도수체크
for _ in range(n):
    numLi.append(int(input()))
# 키값 정렬
numLi.sort()
# 출력
# 산술평균
print(round(sum(numLi)/len(numLi)))
# 중앙값
print(numLi[len(numLi)//2])
# 최빈값
# Counter(리스트).most_common->데이터의 개수가 많은순으로 정렬된 배열을 리턴
countLi = Counter(numLi).most_common()
print(countLi)
# 빈도수가 같은게 있을때 두번째로 작은값을 리턴-> 빈도수 리스트의 길이가 2이상일때
if len(countLi) > 1 and countLi[0][1] == countLi[1][1]:
    print(countLi[1][0])
# 길이가 1 일때는 첫번째값
else:
    print(countLi[0][0])
# 범위 -> 절대값
print(abs(max(numLi)-min(numLi)))