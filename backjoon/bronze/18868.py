# 멀티버스1 브론즈2
m, n = map(int,input().split()) # m(우주의 개수), n(각 우주의 행성의 개수)
planetLi = []   # 각 우주 행성리스트
answer = 0  # 답안
# 각 우주의 행성 리스트 생성
for _ in range(m):
    planetLi.append(list(map(int,input().split())))
# 행성 크기 순서로 변환
for i in range(m):
    planetLiSort = sorted(planetLi[i])
    tmp = []
    for planet in planetLi[i]:
        tmp.append(planetLiSort.index(planet) + 1)
    planetLi[i] = tmp
# 균등한 행성 찾기
for i in range(m):
    for j in range(i+1 , m):
        if planetLi[i] == planetLi[j]:
             answer += 1
print(answer)