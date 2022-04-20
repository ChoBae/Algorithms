# 통계학 실버3
from collections import Counter


n = int(input())
numLi = []
check = 0
count = 0 
# 솔루션 -> 딕셔너리로 빈도수체크
for _ in range(n):
    numLi.append(int(input()))
# 키값 정렬
numLi.sort()
# 출력
# 산술평균
print(round(sum(numLi)/len(numLi)))
# # 중앙값
print(numLi[len(numLi)//2])
# # 최빈값
# 최빈값 정렬-> 빈출수, 오름차순 순서로 정렬
for num in numLi:
    
    if check <= numLi.count(num):
        check = numLi.count(num)
        find = num
        count += 1
        if count == 2:
            break
    else:
        break
    
print(find)
# # 범위 -> 절대값
print(abs(max(numLi)-min(numLi)))