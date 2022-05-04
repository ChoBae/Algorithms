# 좌표 압축
# 입력
n = int(input())
numLi = list(map(int, input().split()))
# 중복 제거 후 오름차순 정렬
setNumLi = list(sorted(set(numLi)))
# 딕셔너리에 우선순위 추가
dict = {setNumLi[i]: i for i in range(len(setNumLi))}
# 출력
for num in numLi:
    print(dict[num], end= ' ')